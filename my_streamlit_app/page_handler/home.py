import my_streamlit_app.streamlit as st


def show(header1: str, option2: int):
    st.header(header1)
    st.write("Welcome to my Streamlit app!")

    st.write(option2)
    st.caption("This is a caption")
