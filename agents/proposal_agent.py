from agents.base_agent import BaseAgent
from agents.prompts import (
    PROPOSAL_SYSTEM_PROMPT,
    PROPOSAL_GENERATION_PROMPT
)


class ProposalAgent(BaseAgent):

    def __init__(self):
        super().__init__(system_prompt=PROPOSAL_SYSTEM_PROMPT, temperature=0.3)

    def run(self, scope_data: dict, cost_data: dict):

        prompt = PROPOSAL_GENERATION_PROMPT.format(
            scope=scope_data,
            cost=cost_data
        )

        response = self.invoke(prompt)

        return response
