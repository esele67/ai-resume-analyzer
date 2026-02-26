from setuptools import setup, find_packages

setup(
    name="ai_resume_analyzer",
    version="1.0",
    description="AI-powered Resume Analyzer that evaluates resumes against job descriptions and provides ATS optimization suggestions.",
    author="God'swill Andrew",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "nltk",
        "scikit-learn",
        "pandas",
        "pdfplumber",
        "python-docx",
        "matplotlib"
    ],
)