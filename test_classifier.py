from agents.classifier_agent import ClassifierAgent

# ---------- Test Case 1: Valid Electrical RFP ----------
rfp_text = """
Request for Proposal (RFP)

Project: 5MW Data Center Electrical Installation
Location: Chennai, India

We invite qualified electrical contractors to submit proposals for the
design, supply, installation, and commissioning of electrical systems.

Scope includes:
- 2000 meters of high-voltage copper cables
- 5 industrial switchboards
- Underground wiring installation

Project timeline: 6 months
All work must comply with IS electrical safety standards.
"""

# ---------- Test Case 2: Non-RFP Document ----------
non_rfp_text = """
SPORTS AUTHORITY OF INDIA
Detention Certificate

This is to certify that Mr. Mohamed Naseem A,
Rank: Sepoy, attended the Diploma in Sports Coaching program
from 10 January 2023 to 15 March 2023.

This certificate is issued for official purposes.
"""

# Initialize classifier
classifier = ClassifierAgent()

print("---- Testing Valid RFP ----")
rfp_result = classifier.run(rfp_text)
print(rfp_result)

print("\n---- Testing Non-RFP Document ----")
non_rfp_result = classifier.run(non_rfp_text)
print(non_rfp_result)
