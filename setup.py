from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Joheb Dani',
    author_email='johebdani@gmail.com',
    install_requires=["google-generativeai","langchain-community","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)