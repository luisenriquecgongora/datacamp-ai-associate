# Import ServerlessSpec
from pinecone_client import pc

# Connect to your index
index = pc.Index("my-first-index")

# Print the index statistics
print(index.describe_index_stats())