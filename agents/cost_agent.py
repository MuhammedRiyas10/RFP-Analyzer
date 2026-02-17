# agents/cost_agent.py

from agents.schemas import CostOutput
from vector_store.material_store import MaterialVectorStore


class CostAgent:
    """
    Deterministic cost calculation agent.
    Integrated into LangChain LCEL pipeline as a runnable step.
    No LLM usage here — pure business logic.
    """

    def __init__(self):
        self.material_store = MaterialVectorStore()

        # Business logic constants
        self.labor_rate_per_unit = 200
        self.contingency_percent = 0.1  # 10%

    def run(self, scope_data: dict) -> dict:

        materials = scope_data.get("materials_required", [])

        total_material_cost = 0.0
        cost_breakdown = []

        for material in materials:
            item_name = material.get("item")
            quantity = material.get("quantity", 0)

            matched_material = self.material_store.search_material(item_name)

            if not matched_material:
                continue

            price_per_unit = float(matched_material["price_per_unit"])

            item_cost = quantity * price_per_unit
            total_material_cost += item_cost

            cost_breakdown.append({
                "item": matched_material["item"],
                "quantity": quantity,
                "unit_price": price_per_unit,
                "total_cost": item_cost
            })

        # Labor logic
        total_quantity = sum(m.get("quantity", 0) for m in materials)
        labor_cost = total_quantity * self.labor_rate_per_unit

        # Contingency
        contingency = (total_material_cost + labor_cost) * self.contingency_percent
        total_cost = total_material_cost + labor_cost + contingency

        # Return validated structured output
        return CostOutput(
            material_cost=total_material_cost,
            labor_cost=labor_cost,
            contingency=contingency,
            total_estimated_cost=total_cost,
            cost_breakdown=cost_breakdown
        ).model_dump()
