"""Chatbot module using Groq API"""

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

class GroqChatbot:
    def __init__(self):
        """Initialize the chatbot with Groq API"""
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file")

        # Initialize Groq client
        self.client = Groq(api_key=api_key)

        # Initialize conversation history
        self.chat_history = []

    def chat(self, user_message):
        """Send a message and get a response"""
        try:
            # Add user message to history
            self.chat_history.append({"role": "user", "content": user_message})

            # Call Groq API with conversation history
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",  # Latest Groq model
                messages=self.chat_history,
                max_tokens=1024,
                temperature=0.7,
            )

            # Extract response text
            response_text = response.choices[0].message.content

            # Add assistant response to history
            self.chat_history.append({"role": "assistant", "content": response_text})

            return response_text

        except Exception as e:
            error_msg = f"Error: {type(e).__name__}: {str(e)}"
            print(error_msg)
            return error_msg

    def get_chat_history(self):
        """Get conversation history"""
        return self.chat_history

    def clear_history(self):
        """Clear conversation history"""
        self.chat_history = []
