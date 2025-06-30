import streamlit as st
import random

st.set_page_config(page_title="AI Interview Question Generator", page_icon="🧠", layout="centered")

st.title("🧠 AI Interview Question Generator")

# Question Bank
questions = {
    "Python": [
        "What is a Python decorator?",
        "Explain the difference between list and tuple.",
        "What is the Global Interpreter Lock (GIL)?",
        "What is a lambda function in Python?",
        "How does exception handling work in Python?"
    ],
    "Machine Learning": [
        "Explain the bias-variance trade-off.",
        "What is overfitting and how can you prevent it?",
        "Difference between supervised and unsupervised learning?",
        "What is cross-validation in machine learning?",
        "Explain the difference between classification and regression."
    ],
    "AI Fundamentals": [
        "What is an artificial neural network?",
        "Explain reinforcement learning in simple terms.",
        "What is the Turing Test?",
        "What is the difference between AI, Machine Learning, and Deep Learning?",
        "Explain the concept of Natural Language Processing (NLP)."
    ],
    "Data Science": [
        "What are the steps of a typical data science project?",
        "Difference between structured and unstructured data.",
        "What is data cleaning and why is it important?",
        "Explain exploratory data analysis (EDA).",
        "What is feature engineering?"
    ]
}

# User Inputs
domain = st.selectbox("Select Domain", list(questions.keys()))
difficulty = st.radio("Select Difficulty Level", ["Easy", "Medium", "Hard"])

if st.button("Generate Question"):
    selected_question = random.choice(questions[domain])
    st.success(f"**{selected_question}**")

st.markdown("---")
st.caption("Developed with ❤️ using Streamlit for SOAI 2025")
