# agents/classifier_agent.py

from agents.base_agent import BaseAgent
from agents.prompts import (
    CLASSIFIER_SYSTEM_PROMPT,
    CLASSIFICATION_PROMPT
)
from agents.schemas import ClassificationOutput


class ClassifierAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            system_prompt=CLASSIFIER_SYSTEM_PROMPT,
            temperature=0
        )

    def run(self, document_text: str) -> dict:

        prompt = CLASSIFICATION_PROMPT.format(
            document_text=document_text[:4000]
        )

        try:
            structured_response = self.invoke_structured(
                user_prompt=prompt,
                schema=ClassificationOutput
            )

            return structured_response.model_dump()

        except Exception:
            return {
                "is_rfp": False,
                "confidence": 0.0,
                "reason": "Structured classification failed"
            }
