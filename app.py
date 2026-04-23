"""Streamlit UI for Gemini Chatbot"""

import streamlit as st
from chatbot import GroqChatbot
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Kalpraj AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        background-color: black;
    }
    .chat-container {
        max-width: 900px;
        margin: 0 auto;
    }
    .user-message {
        background-color: #1e3a8a;
        padding: 12px 16px;
        border-radius: 12px;
        margin: 8px 0;
        border-left: 4px solid #2196f3;
        color: white;
    }
    .bot-message {
        background-color: #1f2937;
        padding: 12px 16px;
        border-radius: 12px;
        margin: 8px 0;
        border-left: 4px solid #4caf50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "chatbot" not in st.session_state:
    try:
        st.session_state.chatbot = GroqChatbot()
        st.session_state.messages = []
    except ValueError as e:
        st.error(f"⚠️ {str(e)}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.title("🤖 Groq Chatbot")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chatbot.clear_history()
        st.session_state.messages = []
        st.success("Chat history cleared!")

    st.markdown("---")
    st.markdown("### About")
    st.info(
        "This chatbot uses Groq's LLaMA 3.1 70B model for fast AI inference. "
        "It maintains conversation history for context-aware responses."
    )

    # Show message count
    st.markdown(f"### Messages: {len(st.session_state.messages)}")

# Main chat area
col1, col2 = st.columns([4, 1])
with col1:
    st.subheader("💬 Chat")

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(
                f'<div class="user-message"><b>You:</b> {message["content"]}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="bot-message"><b>Bot:</b> {message["content"]}</div>',
                unsafe_allow_html=True
            )

# Input area
st.markdown("---")
col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input(
        "Type your message here...",
        placeholder="Ask me anything!",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("Send ➤", use_container_width=True)

# Process user input
if send_button and user_input:
    # Add user message to chat
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Get bot response with loading spinner
    with st.spinner("🤔 Thinking..."):
        try:
            bot_response = st.session_state.chatbot.chat(user_input)
            st.session_state.messages.append({
                "role": "bot",
                "content": bot_response
            })
        except Exception as e:
            st.error(f"Error getting response: {str(e)}")

    # Rerun to update chat display
    st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit and Groq API</p>",
    unsafe_allow_html=True
)
