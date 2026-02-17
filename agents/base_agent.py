from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

class BaseAgent:
    def __init__(self, system_prompt=None, temperature=0.4):
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile",
            temperature=temperature
        )
        self.system_prompt = system_prompt

    def invoke(self, user_prompt):
        if self.system_prompt:
            full_prompt = f"{self.system_prompt}\n\n{user_prompt}"
        else:
            full_prompt = user_prompt

        return self.llm.invoke(full_prompt).content
