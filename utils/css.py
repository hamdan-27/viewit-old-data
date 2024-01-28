import streamlit as st

@st.cache_data(show_spinner=False)
def hide_elements():
    """Hides the Github icon, Fork repo button, and `Made with Streamlit` footer."""
    hide_footer = """
                <style>
                    .stActionButton {visibility: hidden;}
                    .css-a8fn66, .st-emotion-cache-a8fn66 {
                        text-align: left;
                    }
                </style>"""
    st.write(hide_footer, unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def icon_style():
    """CSS styles for the social icons in the sidebar."""
    icon_style = """           
                <style>
                    .social-icons {
                        display: flex;
                        flex-wrap: wrap;
                        justify-content: space-between;
                        align-items: center;
                        max-width: 100%; /* Adjust as needed */
                        width: 100%;
                        padding: 0 10px; 
                        /* Some padding to ensure icons aren't at the very edge on small devices */
                    }

                    .icon {
                        display: block;
                        width: 25px;
                        height: 25px;
                        margin: 5px;
                        /* Adjusted margin to make it symmetrical */
                        background-size: cover;
                        background-position: center;
                        transition: transform 0.3s;
                    }

                    .icon:hover {
                        transform: scale(1.1);
                    }

                    .viewit {
                        background-image: url('https://viewit.ae/_nuxt/img/viewit-logo-no-text.25ba9bc.png');
                    }

                    /* .github {
                        background-image: url('https://cdn2.iconfinder.com/data/icons/social-icons-33/128/Github-1024.png');
                    } */

                    .facebook {
                        background-image: url('https://cdn2.iconfinder.com/data/icons/social-icons-33/128/Facebook-1024.png');
                    }

                    .twitter {
                        background-image: url('https://cdn2.iconfinder.com/data/icons/social-icons-33/128/Twitter-1024.png');
                    }

                    .instagram {
                        background-image: url('https://cdn2.iconfinder.com/data/icons/social-icons-33/128/Instagram-1024.png');
                    }

                    .css-1r6slb0, .e1f1d6gn1 {
                        display: flex;
                        justify-content: center; /* Horizontal centering */
                    }
                </style>
                """

    st.markdown(icon_style, unsafe_allow_html=True)

st.cache_data(show_spinner=False)
def ai_chatbox_style():
    """Custom CSS styling for the AI message container."""
    css = """
    <style>
        .css-4oy321, .st-emotion-cache-4oy321 {
            background-color: #0c43bc;
        } /*  #0a3696 */
        .css-4oy321 p, .st-emotion-cache-4oy321 p, .css-4oy321 ol, .st-emotion-cache-4oy321 ol{
            color: #fafafa;
        }
        .css-4oy321 p a, .st-emotion-cache-4oy321 p a {
            color: lightgreen;
        }
    </style>"""

    st.write(css, unsafe_allow_html=True)


st.cache_data(show_spinner=False)
def user_chatbox_style(**kwargs):
    """Custom CSS styling for the user message container.
    
    Params:
    - kwargs: css property-vlaue pairs passed as keyword arguments.
    """
    
    properties = []

    for k, v in kwargs.items():
        k = k.replace("_", "-")
        properties.append(f"{k}: {v};")
    
    css = "<style> .css-1c7y2kd, .st-emotion-cache-1c7y2kd {"
    css += "\n".join(properties)
    css += "} </style>"

    st.write(css, unsafe_allow_html=True)


# @st.cache_data(show_spinner=False)
# def chatbox_color(ai_color: str = "rgba(0,0,0,0)", user_color: str = "rgba(240, 242, 246, 0.5)"):
#     """Change the background color of the chat message.
#     Use css supported codes, and use hex code with the `#` symbol."""
    
#     chat_css = f"""
#     <style>
#         .css-4oy321, .st-emotion-cache-4oy321 {{
#             background-image: linear-gradient(#4daff6, #3d7af8);
#             padding: 16px 16px 16px 16px;
#         }}
#         /*.css-4oy321, .st-emotion-cache-4oy321 {{
#             background-color: {ai_color};
#             padding: 16px 16px 16px 16px;
#         }}
#         .css-1c7y2kd, .st-emotion-cache-1c7y2kd {{
#             background-color: {user_color};
#         }} */
#     </style>"""
#     st.write(chat_css, unsafe_allow_html=True)



# unfix chat_input from bottom
# chat_input_override = """
# <style>
# .css-17f9rl5 {
#     /* position: fixed; */
#     bottom: 0px;
#     padding-bottom: 70px;
#     padding-top: 1rem;
#     background-color: rgb(10, 54, 150);
#     z-index: 99;
# }
# .element-container, .css-1hynsf2, .e1f1d6gn2 {
#     position: fixed;
#     bottom: 0px;
# }
# </style>"""
# st.write(chat_input_override, unsafe_allow_html=True)

# FOOTER #
# st.write('---')
# caption = """
# <footer>
#     <div class="stMarkdown" style="width: 704px;">
#         <div data-testid="stCaptionContainer" class="css-1wncz92 e1nzilvr5">
#             <p>Made by ViewIt.</p>
#         </div>
#     </div>
#     <div class="stMarkdown" style="width: 704px;">
#         <div data-testid="stCaptionContainer" class="css-1wncz92 e1nzilvr5">
#             <p>
#             By using this chatbot, you agree that the chatbot is provided on an 
#             "as is" basis and that we do not assume any liability for any errors, 
#             omissions or other issues that may arise from your use of the chatbot.
#             </p>
#         </div>
#     </div>
# </footer>"""
# st.write(caption, unsafe_allow_html=True)
