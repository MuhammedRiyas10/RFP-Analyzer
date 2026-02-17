# agents/schemas.py

from pydantic import BaseModel, Field
from typing import List


class ClassificationOutput(BaseModel):
    is_rfp: bool = Field(description="Whether the document is an Electrical RFP")
    confidence: float = Field(description="Confidence score between 0 and 1")
    reason: str = Field(description="Short explanation for the classification decision")

class MaterialItem(BaseModel):
    item: str
    quantity: int
    unit: str

class ScopeOutput(BaseModel):
    project_type: str
    location: str
    timeline_months: int
    materials_required: List[MaterialItem]
    special_requirements: List[str]
    compliance_requirements: List[str]

class CostBreakdownItem(BaseModel):
    item: str
    quantity: int
    unit_price: float
    total_cost: float


class CostOutput(BaseModel):
    material_cost: float
    labor_cost: float
    contingency: float
    total_estimated_cost: float
    cost_breakdown: List[CostBreakdownItem]
