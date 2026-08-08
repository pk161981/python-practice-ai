import streamlit as st
from dotenv import load_dotenv
from google import genai

# Streamlit Chatbot with Memory - uses Google Gemini API and keeps the full
# conversation history so the model remembers earlier turns in the chat.

load_dotenv()

client = genai.Client()

MODEL = "gemini-3.5-flash"


def chat(user_message, history):
    # 1. add what the user said to memory
    history.append({"role": "user", "parts": [{"text": user_message}]})

    # 2. send the ENTIRE conversation history to the LLM
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=history
        )
        reply = response.text
    except Exception as e:
        return f"Sorry, something went wrong: {e}"

    # 3. add the AI's reply to memory too, so it remembers the conversation next time
    history.append({"role": "model", "parts": [{"text": reply}]})
    return reply


st.set_page_config(page_title="Chatbot with Memory", page_icon="🧠")
st.title("🧠 Chatbot with Memory")
st.write("Chat with Gemini - it remembers everything you've said in this session.")

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# render past turns
for msg in st.session_state.conversation_history:
    role = "user" if msg["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(msg["parts"][0]["text"])

user_message = st.chat_input("Say something...")

if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = chat(user_message, st.session_state.conversation_history)
        st.markdown(reply)

if st.session_state.conversation_history and st.button("Clear conversation"):
    st.session_state.conversation_history = []
    st.rerun()
