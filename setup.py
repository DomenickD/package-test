from setuptools import setup, find_packages

setup(
    name="my_streamlit_app",
    version="0.1.0",
    author="Domenick Dobbs",
    author_email="Domenick.dobbs@gmail.com",
    description="A Python package for a modular Streamlit app",
    packages=find_packages(include=["page_handler", "page_handler.*"]),
    install_requires=[
        "streamlit",
    ],
    entry_points={
        "console_scripts": [
            "my-streamlit-app=my_streamlit_app.app:MyStreamlitApp",
        ],
    },
)
