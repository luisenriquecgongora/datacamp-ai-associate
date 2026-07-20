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

# Create your Pinecone index
# pc.create_index(
#     name="datacamp-index", 
#     dimension=1536, 
#     spec=ServerlessSpec(
#         cloud='aws', 
#         region='us-east-1'
#     )
# )

# Check that each vector has a dimensionality of 1536
vector_dims = [len(vector['values']) == 1536 for vector in vectors]
print(all(vector_dims))