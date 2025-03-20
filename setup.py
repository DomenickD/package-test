from setuptools import setup, find_packages

setup(
    name="my_streamlit_app",
    version="0.1.0",
    packages=find_packages(
        include=["my_streamlit_app", "my_streamlit_app.*"]
    ),  # Ensures sub-packages are included
    install_requires=[
        "streamlit",
    ],
)
