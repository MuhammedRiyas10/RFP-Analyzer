from agents.proposal_agent import ProposalAgent

scope_data = {
    "project_type": "Data Center",
    "location": "Chennai",
    "timeline_months": 6,
    "materials_required": [
        {"item": "high-voltage copper cable", "quantity": 2000, "unit": "meters"},
        {"item": "industrial switchboard", "quantity": 5, "unit": "units"}
    ],
    "special_requirements": ["underground wiring installation"],
    "compliance_requirements": ["IS safety standards"]
}

cost_data = {
    "material_cost": 2775000,
    "labor_cost": 401000,
    "contingency": 317600,
    "total_estimated_cost": 3493600,
    "cost_breakdown": [
        {"item": "high-voltage copper cable", "quantity": 2000, "unit_price": 1200, "total_cost": 2400000},
        {"item": "industrial switchboard", "quantity": 5, "unit_price": 75000, "total_cost": 375000}
    ]
}

agent = ProposalAgent()
proposal = agent.run(scope_data, cost_data)

print(proposal)
