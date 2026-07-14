from chroma_client import get_collection

collection = get_collection("netflix_titles")

reference_ids = ['s1', 's2']

# Retrieve the documents for the reference_ids
reference_texts = collection.get(
  ids=reference_ids
)['documents']

# Query using reference_texts
result = collection.query(
  query_texts=reference_texts,
  n_results=3
)

print(result['documents'])