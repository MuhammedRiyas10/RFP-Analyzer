from agents.scope_agent import ScopeAgent

sample_rfp = """
Project: 5MW Data Center in Chennai.
Scope includes 2000 meters of high-voltage copper cables,
5 industrial switchboards,
underground wiring installation,
timeline 6 months,
must comply with IS safety standards.
"""

agent = ScopeAgent()
result = agent.run(sample_rfp)

print(result)
