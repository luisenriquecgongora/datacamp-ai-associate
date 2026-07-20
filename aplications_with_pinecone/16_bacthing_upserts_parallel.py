import itertools
import random

from pinecone_client import pc, pc_w_threads


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
index = pc_w_threads.Index("datacamp-index")

# Upsert vectors in batches of 200 vectors
with pc.Index('datacamp-index', pool_threads=20) as index:
    async_results = [index.upsert(vectors=chunk, async_req=True) for chunk in chunks(vectors, batch_size=200)]
    [async_result.get() for async_result in async_results]

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())
