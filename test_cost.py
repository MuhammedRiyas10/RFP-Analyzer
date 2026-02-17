from agents.cost_agent import CostAgent

scope_data = {
    "materials_required": [
        {"item": "high tension copper cable", "quantity": 2000, "unit": "meters"},
        {"item": "industrial switchboards", "quantity": 5, "unit": "units"}
    ]
}

agent = CostAgent()
result = agent.run(scope_data)

print(result)
