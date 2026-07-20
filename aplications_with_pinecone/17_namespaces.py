import itertools
import random

from pinecone_client import pc

index = pc.Index('datacamp-index')

# Two sets of 1536-dimensional vectors, one per namespace
vector_set1 = [
    {
        "id": f"set1-{i}",
        "values": [random.uniform(-1, 1) for _ in range(1536)],
    }
    for i in range(5)
]

vector_set2 = [
    {
        "id": f"set2-{i}",
        "values": [random.uniform(-1, 1) for _ in range(1536)],
    }
    for i in range(5)
]

# Upsert vector_set1 to namespace1
index.upsert(
  vectors=vector_set1,
  namespace='namespace1'
)

# Upsert vector_set2 to namespace2
index.upsert(
  vectors=vector_set2,
  namespace='namespace2'
)

# Print the index statistics
print(index.describe_index_stats())
