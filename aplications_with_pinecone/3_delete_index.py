# Import ServerlessSpec
from pinecone_client import pc


# Delete your Pinecone index
pc.delete_index("my-first-index")

# List your indexes
print(pc.list_indexes())