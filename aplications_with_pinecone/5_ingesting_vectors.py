# Import ServerlessSpec
import random

from pinecone import ServerlessSpec
from pinecone_client import pc

metadatas = [
    {"genre": "action", "year": 2024},
    {"genre": "comedy", "year": 2023},
    {"genre": "drama", "year": 2022},
    {"genre": "thriller", "year": 2024},
    {"genre": "sci-fi", "year": 2021},
    {"genre": "romance", "year": 2020},
]

vectors = [
    {
        "id": str(i),
        "values": [random.uniform(-1, 1) for _ in range(1536)],
        "metadata": meta
    }
    for i, meta in enumerate(metadatas)
]


# Connect to your index
index = pc.Index("datacamp-index")

# Ingest the vectors and metadata
index.upsert(vectors=vectors)

# Print the index statistics
print(index.describe_index_stats())