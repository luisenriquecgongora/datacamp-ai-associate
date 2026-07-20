from pinecone import ServerlessSpec
from pinecone_client import pc

# Create Pinecone index
pc.create_index(
    name='pinecone-datacamp', 
    dimension=1536,
    spec=ServerlessSpec(cloud='aws', region='us-east-1')
)

# Connect to index and print the index statistics
index = pc.Index("pinecone-datacamp")
print(index.describe_index_stats())
