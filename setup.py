from setuptools import setup, find_packages

setup(
    name="my_streamlit_app",
    version="0.1.0",
    packages=find_packages(),  # Automatically finds all packages with __init__.py
    install_requires=[
        "streamlit",
    ],
    entry_points={
        "console_scripts": [
            "my-streamlit-app=my_streamlit_app.app:MyStreamlitApp",
        ],
    },
)
