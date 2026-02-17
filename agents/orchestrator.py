from agents.classifier_agent import ClassifierAgent
from agents.scope_agent import ScopeAgent
from agents.cost_agent import CostAgent
from agents.proposal_agent import ProposalAgent


class RFPOrchestrator:

    def __init__(self):
        self.classifier = ClassifierAgent()
        self.scope_agent = ScopeAgent()
        self.cost_agent = CostAgent()
        self.proposal_agent = ProposalAgent()

    def run(self, rfp_text):

        # 🔥 Step 1: Classification
        classification = self.classifier.run(rfp_text)

        if not classification.get("is_rfp"):
            return {
                "error": "Uploaded document is NOT an Electrical RFP",
                "classification": classification
            }

        # Step 2: Scope Extraction
        scope = self.scope_agent.run(rfp_text)

        if "error" in scope:
            return {"error": "Scope extraction failed", "details": scope}

        # Step 3: Cost Calculation
        cost = self.cost_agent.run(scope)

        # Step 4: Proposal Generation
        proposal = self.proposal_agent.run(scope, cost)

        return {
            "scope": scope,
            "cost": cost,
            "proposal": proposal
        }
