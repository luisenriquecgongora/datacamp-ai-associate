# In this exercise, you'll practice querying the 'datacamp-index' Pinecone index. 
# You'll connect to the index and query it using the vector provided to retrieve similar vectors. 
# You'll also use metadata filtering to optimize your querying and return the most relevant search results.

from pinecone import ServerlessSpec
from pinecone_client import pc
import random

vector = [random.uniform(-1, 1) for _ in range(1536)]

index = pc.Index('datacamp-index')

# Retrieve the MOST similar vector with the year 2024
query_result = index.query(
    vector=vector,
    filter={
        'year': {'$eq': 2024},
    },
    top_k=1
)
print(query_result)