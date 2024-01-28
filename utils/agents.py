from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain_experimental.tools.python.tool import PythonAstREPLTool
from langchain.agents import ZeroShotAgent, AgentExecutor#, load_tools
from langchain.tools.google_places.tool import GooglePlacesTool
# from langchain_core.messages import HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
# from langchain.memory import ReadOnlySharedMemory
from langchain.chains.llm import LLMChain

from utils.prompts import *

import streamlit as st
import pandas as pd


@st.cache_data(show_spinner=False)
def load_data(filename) -> pd.DataFrame:
    """Loads the csv data that will be used as a knowledge base for the chatbot
    
    Args:
        filename: The name of the file in the `data` directory

    Returns:
        A pandas DataFrame of the data
    """
    df = pd.read_csv(f"data/{filename}")
    
    # for col_name in df.columns:
    #     if 'date' in col_name.lower():
    #         df[col_name] = pd.to_datetime(df[col_name], dayfirst=True)
    
    return df


pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

prefix_map = {
    'reidin_new.csv': REIDIN_PREFIX,
}

@st.cache_data(show_spinner=False)
def df_prefix(filename):
    return load_data(filename), prefix_map[filename]


# @st.cache_resource
def create_pandas_dataframe_agent(
        llm,
        df: pd.DataFrame,
        prefix: str,
        suffix: str,
        format_instructions: str,
        verbose: bool,
        **kwargs) -> AgentExecutor:

    """Construct a pandas agent from an LLM and dataframe.
    
    Parameters:
    - llm: The large language model to use.
    - df: The dataframe to use as knowledge base.
    - prefix: Prefix of the prompt.
    - suffix: Suffix of the prompt.
    - format_instructions: The format to be followed by the agent.
    - verbose: Whether to display the chain of thought.
    - **kwargs: 
    
    Returns:
    - An AgentExecutor object
    """

    if not isinstance(df, pd.DataFrame):
        raise ValueError(f"Expected pandas object, got {type(df)}")

    input_variables = ["df", "input", "chat_history", "agent_scratchpad"]

    # Set up memory
    msgs = StreamlitChatMessageHistory(key="langchain_messages")
    memory = ConversationBufferMemory(
        chat_memory=msgs, memory_key="chat_history")

    python_repl_ast = PythonAstREPLTool(locals={"df": df})

    tools = [python_repl_ast, GooglePlacesTool()]

    prompt = ZeroShotAgent.create_prompt(
        tools=tools,
        prefix=prefix,
        suffix=suffix,
        format_instructions=format_instructions,
        input_variables=input_variables
    )
    partial_prompt = prompt.partial(df=str(df.head()))

    llm_chain = LLMChain(
        llm=llm,
        prompt=partial_prompt
    )
    tool_names = [tool.name for tool in tools]

    agent = ZeroShotAgent(llm_chain=llm_chain,
                          allowed_tools=tool_names, verbose=verbose)

    return AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        verbose=verbose,
        memory=memory,
        **kwargs
    )