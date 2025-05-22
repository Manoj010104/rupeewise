# llama_api.py

import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

def call_groq_llama_api(prompt: str) -> str:
    """Uses LangChain and ChatGroq to send the prompt and get response."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment")

    llm = ChatGroq(
        temperature=0.2,
        groq_api_key=api_key,
        model_name="llama3-70b-8192"
    )

    # You can use simple prompt as-is or wrap with PromptTemplate
    full_response = llm.invoke(prompt)

    if isinstance(full_response, AIMessage):
        return full_response.content

    return str(full_response)
