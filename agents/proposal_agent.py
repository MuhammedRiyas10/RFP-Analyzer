# agents/proposal_agent.py

from agents.base_agent import BaseAgent
from agents.prompts import (
    PROPOSAL_SYSTEM_PROMPT,
    PROPOSAL_GENERATION_PROMPT
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage


class ProposalAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            system_prompt=PROPOSAL_SYSTEM_PROMPT,
            temperature=0.3
        )

        # LCEL Prompt Template
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", PROPOSAL_SYSTEM_PROMPT),
            ("human", PROPOSAL_GENERATION_PROMPT),
        ])

        # LCEL Chain
        self.chain = self.prompt_template | self.llm

    def run(self, scope_data: dict, cost_data: dict) -> str:

        response = self.chain.invoke({
            "scope": scope_data,
            "cost": cost_data
        })

        # Clean accidental markdown fences
        cleaned = (
            response.content
            .replace("```markdown", "")
            .replace("```", "")
            .strip()
        )

        return cleaned
