from uuid import uuid4

import pandas as pd

from pinecone import ServerlessSpec
from pinecone_client import pc
from openai_client import client

index = pc.Index('pinecone-datacamp')

query = "What is in front of the Notre Dame Main Building?"

# Create the query vector
query_response = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
)
query_emb = query_response.data[0].embedding

# Query the index and retrieve the top five most similar vectors
retrieved_docs = index.query(
    vector=query_emb,
    top_k=5,
    namespace="squad_dataset"
)

for result in retrieved_docs['matches']:
    print(f"{result['id']}: {round(result['score'], 2)}")
    print('\n')