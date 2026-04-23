# 🤖 Gemini Chatbot with Streamlit

A simple yet powerful chatbot built with LangChain, Google Gemini API, and Streamlit.

## Features

- ✨ Real-time chat interface using Streamlit
- 🧠 Powered by Google's Gemini AI model
- 💾 Conversation memory for context-aware responses
- 🎨 Clean and intuitive UI
- 🔄 Easy to clear chat history

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Get API Key"
3. Create a new API key
4. Copy the API key

### 3. Configure .env File

Open `.env` file and replace `your_api_key_here` with your actual Gemini API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run the Chatbot

```bash
streamlit run app.py
```

The chatbot will open in your browser at `http://localhost:8501`

## Files

- **app.py** - Main Streamlit UI application
- **chatbot.py** - Chatbot logic using LangChain and Gemini
- **.env** - Environment variables (add your API key here)
- **requirements.txt** - Python dependencies

## Usage

1. Type your message in the input field
2. Click "Send ➤" or press Enter
3. Wait for the bot's response
4. Use "Clear Chat History" button to reset the conversation

## Customization

You can modify the following in `chatbot.py`:
- `temperature=0.7` - Adjust response creativity (0-1)
- `model="gemini-pro"` - Use different Gemini models
- Memory type - Switch from `ConversationBufferMemory` to other memory types

## Troubleshooting

- **API Key Error**: Make sure your .env file has the correct API key
- **Module Not Found**: Run `pip install -r requirements.txt`
- **Port Already in Use**: Run `streamlit run app.py --server.port 8502`

## Requirements

- Python 3.8 or higher
- Active internet connection
- Valid Gemini API key

Enjoy chatting with Gemini! 🚀
