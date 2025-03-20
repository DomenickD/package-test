import streamlit as st
from page_handler import home


class MyStreamlitApp:
    def __init__(self, title: str = "My Streamlit App", layout: str = "wide"):
        self.title = title
        self.layout = layout
        # st.set_page_config(page_title="My Streamlit App", layout="wide")

    def run_home(self, header: str = "Home Page", option2: int = 10):
        home.show(header, option2)


# st.subheader("Test app Page")

# st.set_page_config(page_title="My Streamlit App", layout="wide")
# MyStreamlitApp().run_home("Home Page", 10)
