# agents/tools.py

from langchain.tools import StructuredTool
from agents.classifier_agent import ClassifierAgent
from agents.schemas import ClassificationOutput


classifier_agent = ClassifierAgent()


def classify_document(document_text: str) -> ClassificationOutput:
    """
    Classifies whether the uploaded document is a valid Electrical RFP.
    """
    result = classifier_agent.run(document_text)
    return ClassificationOutput(**result)


classify_document_tool = StructuredTool.from_function(
    func=classify_document,
    name="classify_document",
    description="Classifies whether a document is an Electrical RFP.",
)
