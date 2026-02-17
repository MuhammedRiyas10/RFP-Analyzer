# agents/orchestrator.py

from langchain_core.runnables import RunnableLambda

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

        # Build LCEL pipeline
        self.pipeline = (
            RunnableLambda(self.classify_step)
            | RunnableLambda(self.scope_step)
            | RunnableLambda(self.cost_step)
            | RunnableLambda(self.proposal_step)
        )

    # -------------------------
    # STEP 1: Classification
    # -------------------------
    def classify_step(self, input_data: dict):

        rfp_text = input_data["rfp_text"]

        classification = self.classifier.run(rfp_text)

        if not classification.get("is_rfp"):
            return {
                "error": "Uploaded document is NOT an Electrical RFP",
                "classification": classification
            }

        return {
            "rfp_text": rfp_text,
            "classification": classification
        }

    # -------------------------
    # STEP 2: Scope Extraction
    # -------------------------
    def scope_step(self, input_data: dict):

        if "error" in input_data:
            return input_data

        rfp_text = input_data["rfp_text"]

        scope = self.scope_agent.run(rfp_text)

        if "error" in scope:
            return {"error": "Scope extraction failed", "details": scope}

        input_data["scope"] = scope
        return input_data

    # -------------------------
    # STEP 3: Cost Calculation
    # -------------------------
    def cost_step(self, input_data: dict):

        if "error" in input_data:
            return input_data

        scope = input_data["scope"]

        cost = self.cost_agent.run(scope)

        input_data["cost"] = cost
        return input_data

    # -------------------------
    # STEP 4: Proposal Generation
    # -------------------------
    def proposal_step(self, input_data: dict):

        if "error" in input_data:
            return input_data

        scope = input_data["scope"]
        cost = input_data["cost"]

        proposal = self.proposal_agent.run(scope, cost)

        return {
            "scope": scope,
            "cost": cost,
            "proposal": proposal
        }

    # -------------------------
    # Public Run Method (Full Pipeline)
    # -------------------------
    def run(self, rfp_text: str):

        return self.pipeline.invoke({
            "rfp_text": rfp_text
        })

    # -------------------------
    # NEW: Step 1 Only (Classify + Scope)
    # -------------------------
    def extract_scope_only(self, rfp_text: str):
        # Build partial LCEL pipeline
        partial_pipeline = (
            RunnableLambda(self.classify_step)
            | RunnableLambda(self.scope_step)
        )
        return partial_pipeline.invoke({"rfp_text": rfp_text})

    # -------------------------
    # NEW: Step 2 Only (Cost + Proposal)
    # -------------------------
    def generate_from_scope(self, scope_data: dict):
        # Resume pipeline from Cost step
        # Input must mimic output of scope_step
        input_data = {
            "scope": scope_data,
            # We preserve original text if available, or empty string if not strictly needed by cost/proposal agents
            # (Cost/Proposal agents usually only need 'scope' dict)
        }
        
        partial_pipeline = (
            RunnableLambda(self.cost_step)
            | RunnableLambda(self.proposal_step)
        )
        return partial_pipeline.invoke(input_data)
