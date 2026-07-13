import numpy as np
from scipy.spatial import distance

from openai_client import client

# A small set of news articles. The goal: given a search query, find the
# article whose meaning is closest to it — not by matching keywords, but
# by comparing embeddings.
articles = [
    {"headline": "Economic Growth Continues Amid Global Uncertainty", "topic": "Business"},
    {"headline": "Interest Rates Hit New Highs, Affecting Mortgage Rates", "topic": "Business"},
    {"headline": "Scientists Make Breakthrough Discovery in Renewable Energy", "topic": "Science"},
    {"headline": "India Successfully Lands Rover on Moon", "topic": "Science"},
    {"headline": "New Particle Discovered at CERN", "topic": "Science"},
    {"headline": "Tech Company Launches Innovative Product to Improve Online Accessibility", "topic": "Tech"},
    {"headline": "Tech Giant Buys 49% Stake In AI Startup", "topic": "Tech"},
    {"headline": "New Social Media Platform Has Everyone Talking!", "topic": "Tech"},
    {"headline": "The Blues Beat The Reds In Thrilling Match", "topic": "Sport"},
    {"headline": "Local Team Wins Championship After Dramatic Final", "topic": "Sport"},
]


def create_embeddings(texts):
    """Embed a list of texts (or a single string) with the OpenAI API.

    Returns a list of embedding vectors, one per input text.
    Batching all texts into a single API call is cheaper and faster
    than calling the API once per text.
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )
    response_dict = response.model_dump()
    return [item["embedding"] for item in response_dict["data"]]


# Embed every headline in one batched request and store each vector
# alongside its article
headline_embeddings = create_embeddings([article["headline"] for article in articles])
for article, embedding in zip(articles, headline_embeddings):
    article["embedding"] = embedding

# Embed the search query. Note the query shares no keywords with the
# best-matching headline — the match works purely on meaning.
search_text = "computer"
search_embedding = create_embeddings(search_text)[0]

# Compute the cosine distance between the query and every article.
# Cosine distance = 1 - cosine similarity: it measures the angle between
# two vectors, ignoring their length. 0 means identical direction (same
# meaning), values near 1 mean unrelated. Because it ignores magnitude,
# it's the standard choice for comparing text embeddings.
distances = []
for article in articles:
    dist = distance.cosine(search_embedding, article["embedding"])
    distances.append(dist)

# The article with the SMALLEST distance is the most semantically
# similar to the query — argmin gives its index.
min_dist_ind = np.argmin(distances)
print(f"Search query: {search_text!r}")
print(f"Closest headline: {articles[min_dist_ind]['headline']}")
print(f"Cosine distance: {distances[min_dist_ind]:.4f}")

# Show the full ranking so you can see how the other headlines compare
print("\nAll articles ranked by similarity (smallest distance first):")
for ind in np.argsort(distances):
    print(f"  {distances[ind]:.4f}  [{articles[ind]['topic']:8}] {articles[ind]['headline']}")
