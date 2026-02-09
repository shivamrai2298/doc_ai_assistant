import streamlit as st
import requests

st.title("Doc AI Assistant")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:
    res = requests.post(
        "http://localhost:8000/ingest",
        files={"file": uploaded_file}
    )
    st.success(res.json())

query = st.text_input("Ask a question")

if query:
    res = requests.post(
        "http://localhost:8000/query",
        json={"question": query}
    )
    st.write(res.json()["answer"])

