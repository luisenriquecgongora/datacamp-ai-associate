from uuid import uuid4

import pandas as pd

from pinecone import ServerlessSpec
from pinecone_client import pc
from openai_client import client

index = pc.Index('pinecone-datacamp')

# Read the SQuAD dataset from the CSV in this folder
df = pd.read_csv("squad_dataset.csv")

batch_limit = 100

# Slice the DataFrame into batches (np.array_split turns a DataFrame into a
# plain ndarray in newer numpy versions, which breaks .iterrows())
for start in range(0, len(df), batch_limit):
    batch = df.iloc[start:start + batch_limit]
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    # Keep embeddings as plain lists — the Pinecone client can't serialize numpy types
    embeds = [x.embedding for x in response.data]
    
    # Upsert vectors to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='squad_dataset')
