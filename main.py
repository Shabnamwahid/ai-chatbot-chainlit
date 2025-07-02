
import os
import chainlit as cl
from dotenv import load_dotenv
import google.generativeai as genai

# Load Gemini API key from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not set")

# Configure Gemini API
genai.configure(api_key=gemini_api_key)

# Start chatbot
@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Hello! Ask me anything in Urdu or English!").send()

# Handle user messages
@cl.on_message
async def on_message(message: cl.Message):
    try:
        # Use Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(message.content)
        # Send response to user
        await cl.Message(content=response.text).send()
    except Exception as e:
        # Send error message
        await cl.Message(content=f"Error: {str(e)}").send()





        
# run in the terminal 
# .venv\Scripts\activate
# uv run --active chainlit run main.py --port 8001 