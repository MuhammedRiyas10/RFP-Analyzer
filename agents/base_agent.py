# agents/base_agent.py

import os
from dotenv import load_dotenv
from typing import Type, Optional

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

load_dotenv()


class BaseAgent:
    def __init__(
        self,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2,
        model_name: str = "llama-3.3-70b-versatile",
    ):
        self.system_prompt = system_prompt

        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name=model_name,
            temperature=temperature,
        )

    def invoke(self, user_prompt: str) -> str:
        """
        Standard text invocation (for proposal generation etc.)
        """
        messages = []

        if self.system_prompt:
            messages.append(SystemMessage(content=self.system_prompt))

        messages.append(HumanMessage(content=user_prompt))

        response = self.llm.invoke(messages)
        return response.content

    def invoke_structured(
        self,
        user_prompt: str,
        schema: Type[BaseModel],
    ) -> BaseModel:
        """
        Structured output invocation using Pydantic schema.
        This ensures clean JSON outputs (no hallucinated keys).
        """

        parser = PydanticOutputParser(pydantic_object=schema)

        format_instructions = parser.get_format_instructions()

        full_prompt = f"""
{user_prompt}

{format_instructions}
"""

        messages = []

        if self.system_prompt:
            messages.append(SystemMessage(content=self.system_prompt))

        messages.append(HumanMessage(content=full_prompt))

        response = self.llm.invoke(messages)

        return parser.parse(response.content)
