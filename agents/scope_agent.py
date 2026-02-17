import json
import re
from agents.base_agent import BaseAgent
from agents.prompts import SCOPE_SYSTEM_PROMPT, SCOPE_EXTRACTION_PROMPT


class ScopeAgent(BaseAgent):

    def __init__(self):
        super().__init__(system_prompt=SCOPE_SYSTEM_PROMPT, temperature=0)

    def run(self, rfp_text):
        prompt = SCOPE_EXTRACTION_PROMPT.format(rfp_text=rfp_text)
        response = self.invoke(prompt)

        cleaned = self._clean_response(response)

        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON", "raw": response}

    def _clean_response(self, text: str) -> str:
        # Remove triple backticks and optional "json"
        text = re.sub(r"```(?:json)?", "", text, flags=re.IGNORECASE)
        text = text.replace("```", "")
        return text.strip()
