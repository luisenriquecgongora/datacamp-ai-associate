import itertools
import random

from pinecone_client import pc

index = pc.Index('datacamp-index')

# Vector to query the index with (same dimensionality as the index: 1536)
vector = [random.uniform(-1, 1) for _ in range(1536)]

# Query namespace1 with the vector provided
query_result = index.query(
    vector=vector,
    namespace="namespace1",
    top_k=3
)
print(query_result)