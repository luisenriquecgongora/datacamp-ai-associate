from chroma_client import get_collection

# Retrieve the netflix_titles collection
collection = get_collection("netflix_titles")

# Query the collection for "films about dogs"
result = collection.query(
  query_texts=["films about dogs"],
  n_results=3
)

print(result)