import itertools
import random

from pinecone_client import pc


def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    # Convert the iterable into an iterator
    it = iter(iterable)
    # Slice the iterator into chunks of size batch_size
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        # Yield the chunk
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))


# Define 250 vectors so the upsert is split into 3 chunks (100 + 100 + 50)
vectors = [
    {
        "id": str(i),
        "values": [random.uniform(-1, 1) for _ in range(1536)],
    }
    for i in range(250)
]

# Connect to your index
index = pc.Index("datacamp-index")

# Upsert the vectors in chunks
for chunk in chunks(vectors):
    index.upsert(vectors=chunk)

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())
