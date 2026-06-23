import streamlit as st
from auth import register_user, login_user

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login_page():
    st.title("🔐 Login - RAG Chatbot")

    menu = st.selectbox(
        "Select",
        ["Login", "Register"]
    )

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if menu == "Register":
        if st.button("Register"):
            if register_user(username, password):
                st.success("Registration successful!")
            else:
                st.error("User already exists")

    if menu == "Login":
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")


def rag_app():
    st.title("RAG Chatbot")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    question = st.text_input("Ask Question")

    if st.button("Ask"):
        st.write("Answer comes here")


if st.session_state.logged_in:
    rag_app()
else:
    login_page()