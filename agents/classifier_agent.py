import json
import re
from agents.base_agent import BaseAgent
from agents.prompts import (
    CLASSIFIER_SYSTEM_PROMPT,
    CLASSIFICATION_PROMPT
)


class ClassifierAgent(BaseAgent):

    def __init__(self):
        super().__init__(system_prompt=CLASSIFIER_SYSTEM_PROMPT, temperature=0)

    def run(self, document_text: str):

        prompt = CLASSIFICATION_PROMPT.format(
            document_text=document_text[:4000]  # limit size
        )

        response = self.invoke(prompt)

        cleaned = re.sub(r"```(?:json)?", "", response, flags=re.IGNORECASE)
        cleaned = cleaned.replace("```", "").strip()

        try:
            return json.loads(cleaned)
        except:
            return {
                "is_rfp": False,
                "confidence": 0.0,
                "reason": "Invalid classification output"
            }
