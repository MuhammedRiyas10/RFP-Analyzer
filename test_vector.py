from vector_store.material_store import MaterialVectorStore

store = MaterialVectorStore()

query = "high tension copper cable"

result = store.search_material(query)

print(result)
