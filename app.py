import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI Interview Question Generator", page_icon="🧠")

st.title("🧠 AI-Powered Interview Question Generator")

HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(provider="novita", api_key=HF_TOKEN)

DOMAINS = ["Python", "Machine Learning", "Data Science", "Web Development", "Cybersecurity"]
DIFFICULTIES = ["Easy", "Medium", "Hard"]

domain = st.selectbox("Select Language/Domain", DOMAINS)
difficulty = st.selectbox("Select Difficulty Level", DIFFICULTIES)
additional_context = st.text_area("Additional Context (optional)", placeholder="E.g., focus on OOP concepts, deep learning, etc.")

if "question" not in st.session_state:
    st.session_state.question = ""
if "solution" not in st.session_state:
    st.session_state.solution = ""

if st.button("🎯 Generate Interview Question"):
    with st.spinner("Generating your interview question..."):
        prompt = (
            f"Generate a {difficulty.lower()} level interview question for {domain}.\n"
            f"{f'Focus on: {additional_context}' if additional_context else ''}\n"
            "The question should be practical, technical, and avoid yes/no format."
        )

        try:
            completion = client.chat.completions.create(
                model="meta-llama/Llama-3.1-8B-Instruct",
                messages=[{"role": "user", "content": prompt}]
            )
            st.session_state.question = completion.choices[0].message.content.strip()
            st.session_state.solution = ""  # Reset solution
            st.success("### Generated Interview Question:")
            st.markdown(f"> {st.session_state.question}")

        except Exception as e:
            st.error(f"⚠️ Error generating question: {e}")

if st.session_state.question:
    if st.button("💡 Show Suggested Solution"):
        with st.spinner("Generating solution..."):
            try:
                solution_prompt = f"Provide a detailed suggested solution for the following interview question:\n{st.session_state.question}"
                completion = client.chat.completions.create(
                    model="meta-llama/Llama-3.1-8B-Instruct",
                    messages=[{"role": "user", "content": solution_prompt}]
                )
                st.session_state.solution = completion.choices[0].message.content.strip()
            except Exception as e:
                st.error(f"⚠️ Error generating solution: {e}")

if st.session_state.solution:
    st.info("### Suggested Solution:")
    st.markdown(f"> {st.session_state.solution}")
