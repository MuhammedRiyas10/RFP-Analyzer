from agents.orchestrator import RFPOrchestrator

rfp_text = """
Project: 5MW Data Center in Chennai.
Scope includes 2000 meters of high-voltage copper cables,
5 industrial switchboards,
underground wiring installation,
timeline 6 months,
must comply with IS safety standards.
"""

orchestrator = RFPOrchestrator()
result = orchestrator.run(rfp_text)

print(result["cost"])
print("\n")
print(result["proposal"])
