import json
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document


class MaterialVectorStore:

    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vector_store = None
        self._load_store()

    def _load_store(self):
        file_path = os.path.join(
            os.path.dirname(__file__),
            "material_data.json"
        )

        with open(file_path, "r") as f:
            materials = json.load(f)

        documents = []
        for material in materials:
            content = f"{material['item']} costs {material['price_per_unit']} per {material['unit']}"
            documents.append(
                Document(
                    page_content=content,
                    metadata=material
                )
            )

        self.vector_store = FAISS.from_documents(
            documents,
            self.embedding_model
        )

    def search_material(self, query):
        results = self.vector_store.similarity_search(query, k=1)
        return results[0].metadata if results else None
