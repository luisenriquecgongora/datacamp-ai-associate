from openai_client import client
# Create a request to obtain embeddings
response = client.embeddings.create(
    model="text-embedding-3-small",
    input="When does Peru was selected as the best culinary destionation in the world?"
)

# Convert the response into a dictionary
response_dict = response.model_dump()
print(response_dict)