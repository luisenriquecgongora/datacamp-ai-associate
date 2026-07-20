from pinecone import ServerlessSpec
from pinecone_client import pc
import random

vector = [random.uniform(-1, 1) for _ in range(1536)]

index = pc.Index('datacamp-index')

# Retrieve the MOST similar vector with the year 2024
query_result = index.query(
    vector=vector,
    top_k=1,
    filter={
        "genre": { "$eq": "thriller"},
        "year": {"$lt": 2018}
    }
)
print(query_result)