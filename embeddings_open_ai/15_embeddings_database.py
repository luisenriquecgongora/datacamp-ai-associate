from chroma_client import client, create_collection

# Create a netflix_title collection using the OpenAI Embedding function
collection = create_collection("netflix_titles")

# List the collections
print(client.list_collections())
