from pinecone import ServerlessSpec
from pinecone_client import pc
import random

vector = [random.uniform(-1, 1) for _ in range(1536)]

index = pc.Index('datacamp-index')

# Update the metadata of vector ID 7
fetched_vector = index.update(
    id="7",
    set_metadata={
        "genre":"thriller",
        "year": "2024"
    }
)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=["7"])

print(fetched_vector)