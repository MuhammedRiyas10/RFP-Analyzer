"""
Prompt templates for Electrical RFP AI Agents
"""

# =========================
# SYSTEM PROMPTS
# =========================

SCOPE_SYSTEM_PROMPT = """
You are an expert electrical project analyst.

Your role:
1. Read and understand RFP documents.
2. Extract structured project data.
3. Identify materials, quantities, compliance requirements, and timelines.
4. Return strictly valid JSON.
"""

PROPOSAL_SYSTEM_PROMPT = """
You are an expert proposal writer and senior electrical contractor with 15+ years of experience winning municipal and government bids for electrical maintenance & repair services. Your proposals are always compliant, professional, persuasive, concise, and customer-focused. You NEVER use zero or placeholder totals unless explicitly instructed — instead, use realistic example numbers with clear [PLACEHOLDERS] for the user to customize.
"""

# =========================
# TASK PROMPTS
# =========================

SCOPE_EXTRACTION_PROMPT = """
Analyze the following RFP document and extract structured data.

RFP:
{rfp_text}

Return strictly this JSON format:

{{
  "project_type": "",
  "location": "",
  "timeline_months": 0,
  "materials_required": [
    {{
      "item": "",
      "quantity": 0,
      "unit": ""
    }}
  ],
  "special_requirements": [],
  "compliance_requirements": []
}}

Return only JSON.
"""

PROPOSAL_GENERATION_PROMPT = """
Task: Generate a complete, professional bid proposal document in response to the City of Abilene, Texas – Electrical Maintenance & Repair Services RFP (CB-2462). Structure it exactly as a real editable proposal document would appear in Word/PDF.

Project Scope Context:
{scope}

Cost Breakdown Context:
{cost}

Output format rules (strictly follow):
- Use clean Markdown for structure: # for main title, ## for sections, ### for subsections.
- Use **bold** for emphasis, *italics* sparingly.
- Use proper tables for cost breakdowns (with | --- | separators).
- Include realistic but placeholder-based content where specifics are unknown (e.g., company name = [Your Company Name], labor rates = [e.g., $85–$125/hr], totals = [calculated or estimated]).
- End with signature block and contact placeholders.
- Make it persuasive: highlight reliability, safety, quick response, compliance (Texas Master Electrician License, background checks, permits, TPIA, Chapter 176), and value to the City.
- Keep total length 3–5 pages worth of content (detailed but not bloated).

Required sections in this exact order:
1. Title Page / Cover (include proposal title, RFP reference, date, company info placeholders)
2. Executive Summary (1–2 paragraphs: who we are, commitment, key differentiators, response time promise)
3. Understanding of Scope & Requirements (demonstrate deep RFP comprehension — mirror key RFP points like 24/7 emergency 1-hr response, regular hours, marked vehicles, police clearance, Master License, permits, codes)
4. Technical Approach & Methodology (how we deliver: team qualifications, tools/equipment, processes for routine maintenance, repairs, installations, troubleshooting, safety protocols, quality assurance)
5. Project Team & Qualifications (brief bios/roles placeholders, licensing proof, experience with municipal contracts)
6. Timeline & Service Delivery Schedule (realistic for on-call/term contract — not rigid monthly phases; emphasize flexibility, on-demand response, annual review)
7. Pricing & Cost Breakdown (detailed table: hourly labor rates by classification, material markup %, emergency rates, example estimates for common tasks, total not-to-exceed or estimated annual value if applicable. Use realistic Texas rates with [PLACEHOLDERS]. Include notes on T&M basis, no mobilization fees, etc.)
8. Assumptions, Exclusions & Risks
9. Conclusion & Call to Action
10. Signature & Contact Block

Be specific to electrical services: mention NEC compliance, arc flash safety, lockout/tagout, EV charger readiness if relevant, emergency generator support, etc.

Make the language confident, professional, and benefit-oriented.

Output ONLY the formatted proposal document — no extra explanations.
"""
CLASSIFIER_SYSTEM_PROMPT = """
You are a document classification expert.

Your job:
Determine whether the given document is an Electrical Request for Proposal (RFP).

An Electrical RFP typically:
- Requests bids or proposals
- Mentions project scope
- Lists materials or quantities
- Specifies timeline
- Invites contractors

Return strictly JSON in this format:

{
  "is_rfp": true or false,
  "confidence": 0.0 to 1.0,
  "reason": "Short explanation"
}
"""

CLASSIFICATION_PROMPT = """
Analyze the following document and classify it.

Document:
{document_text}

Return only JSON.
"""
