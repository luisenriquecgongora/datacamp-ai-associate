# In this exercise, you've been provided with a list of ids containing IDs of different records in your 'datacamp-index' index. 
# You'll use these IDs to retrieve the associated records and explore their metadata.

from pinecone import ServerlessSpec
from pinecone_client import pc

index = pc.Index('datacamp-index')
ids = ['2', '5', '8']

# Fetch the vectors from the connected Pinecone index
fetched_vectors = index.fetch(ids=ids)

print(fetched_vectors)

# Extract the metadata from each result in fetched_vectors
metadatas = [fetched_vectors['vectors'][id]['metadata'] for id in ids]
print(metadatas)