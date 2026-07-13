from openai_client import client

# Define a create_embeddings function
def create_embeddings(texts):
    """Embed a single string OR a list of strings with the OpenAI API.

    The Embeddings endpoint accepts both, which is what makes this helper
    reusable: it always returns a LIST of embedding vectors — one vector
    for a single string, several for a list. Batching a list into one API
    call is cheaper and faster than calling the API once per text.
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    response_dict = response.model_dump()

    return [data['embedding'] for data in response_dict['data']]


# A single product description to embed
short_description = "The latest flagship smartphone with AI-powered features and 5G connectivity."

# Several descriptions to embed in one batched API call
list_of_descriptions = [
    "Charge your devices conveniently with this sleek wireless charging dock.",
    "Elevate your gaming experience with this powerful gaming laptop.",
]

# Embed short_description and print
# create_embeddings() always returns a list, so [0] takes the single
# vector out of it. Each vector has 1536 numbers (the dimensionality of
# text-embedding-3-small), so we print just the first 5 to keep the
# output readable.
embedding = create_embeddings(short_description)[0]
print(f"Single text -> 1 vector of {len(embedding)} dimensions")
print(f"First 5 values: {embedding[:5]}\n")

# Embed list_of_descriptions and print
# One API call embeds both texts; the vectors come back in the same
# order as the input list.
embeddings = create_embeddings(list_of_descriptions)
print(f"List of {len(list_of_descriptions)} texts -> {len(embeddings)} vectors")
for description, emb in zip(list_of_descriptions, embeddings):
    print(f"  {description[:50]}... first 3 values: {emb[:3]}")
