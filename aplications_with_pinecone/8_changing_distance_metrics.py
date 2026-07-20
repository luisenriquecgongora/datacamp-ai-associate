from pinecone import ServerlessSpec
from pinecone_client import pc

# FIRST CREATION
# index = pc.create_index(
#     name="dotproduct-index",
#     dimension=1536,
#     metric="dotproduct",
#     spec=ServerlessSpec(
#         cloud='aws',
#         region='us-east-1'
#     )
# )

index = pc.Index("dotproduct-index")

# Print a list of your indexes
print(index.describe_index_stats())