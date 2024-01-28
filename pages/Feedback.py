import streamlit as st

from utils.css import icon_style, hide_elements
from Chat import collector, model

try:
    st.set_page_config(page_title='Feedback • ViewIt.AI',
                       initial_sidebar_state='collapsed', page_icon='📝', layout='wide')
except:
    st.rerun()

# Add Viewit logo image to the center of page
col1, col2, col3 = st.columns([1,1.2,1])
with col2:
    # st.image("https://i.postimg.cc/Nfz5nZ8G/Logo.png", width=300)
    st.image("imgs/Viewit ai Logo.png", width=300)
    st.subheader('⭐ Rate your experience!')

st.write('---')

# The feedback component
feed = collector.st_feedback(
            component="general-feedback",
            feedback_type="textbox",
            textbox_type="text-area",
            model=model,
            user_id=None,
            open_feedback_label="Share your overall experience with our chatbot",
            align="center",
        )

# Sidebar
with st.sidebar:
    # st.write("---")

    # Social Icons
    st.write(f'''
    <div class="social-icons">
        <a href="https://viewit.ae" class="icon viewit" aria-label="ViewIt"></a>
        <!-- <a href="https://github.com/viewitai" class="icon github" aria-label="GitHub"></a> -->
        <a href="https://facebook.com/View1T" class="icon facebook" aria-label="Facebook"></a>
        <a href="https://instagram.com/viewit.ae" class="icon instagram" aria-label="Instagram"></a>
        <a href="https://twitter.com/aeviewit" class="icon twitter" aria-label="Twitter"></a>
    </div>''', unsafe_allow_html=True)
    st.write('---')

    st.caption('© 2023 ViewIt. All rights reserved.')

# Hide `Made with Streamlit`
hide_elements()
# CSS for social icons
icon_style()