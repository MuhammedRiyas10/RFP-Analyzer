# agents/scope_agent.py

from agents.base_agent import BaseAgent
from agents.prompts import SCOPE_SYSTEM_PROMPT, SCOPE_EXTRACTION_PROMPT
from agents.schemas import ScopeOutput


class ScopeAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            system_prompt=SCOPE_SYSTEM_PROMPT,
            temperature=0
        )

    def run(self, rfp_text: str) -> dict:

        prompt = SCOPE_EXTRACTION_PROMPT.format(
            rfp_text=rfp_text[:6000]  # prevent token overflow
        )

        try:
            structured_response = self.invoke_structured(
                user_prompt=prompt,
                schema=ScopeOutput
            )

            return structured_response.model_dump()

        except Exception:
            return {
                "error": "Structured scope extraction failed"
            }
