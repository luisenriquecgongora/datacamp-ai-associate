from pinecone import ServerlessSpec
from pinecone_client import pc
import random

vector = [random.uniform(-1, 1) for _ in range(1536)]

index = pc.Index('datacamp-index')

# Update the metadata of vector ID 7
fetched_vector = index.delete(
    ids=["10", "11"]
)

print(index.describe_index_stats())