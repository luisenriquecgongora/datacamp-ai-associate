# Querying vectors is foundational to so many AI applications. 
# It involves embedding a user input, comparing it to the vectors in the database, and returning the most similar vectors.
# In this exercise, you've been provided with a mystery vector called vector and you'll use it to query your index called 'datacamp-index'.

import random

from pinecone import ServerlessSpec
from pinecone_client import pc

# Mystery vector to query the index with (same dimensionality as the index: 1536)
vector = [random.uniform(-1, 1) for _ in range(1536)]

index = pc.Index('datacamp-index')

# Retrieve the top three most similar records
query_result = index.query(
    vector = vector,
    top_k=3
)

print(query_result)