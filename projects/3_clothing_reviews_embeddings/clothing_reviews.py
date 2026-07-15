from chroma_client import create_collection
from openai_client import client
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from scipy.spatial import distance


# Load the dataset
import pandas as pd
reviews = pd.read_csv("womens_clothing_e-commerce_reviews.csv")

# Display the first few entries
reviews.head()

# INSET REVIEWS INTO DB
ids = []
documents = []

for _, row in reviews.iterrows():
    ids.append(str(row['Review ID']))
    documents.append(row['Review Text'])

collection = create_collection("store_reviews")

# Add the documents and IDs to the collection (upsert keeps reruns idempotent)
collection.upsert(ids=ids, documents=documents)


print(collection.peek(5))


######
######
# Dimensionality reduction & visualization
######
######


# Create embeddings for each review
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

response_dict = response.model_dump()

embeddings = []

for idx, row in reviews.iterrows():
    embeddings.append(response_dict["data"][idx]["embedding"])

# Reduce the number of embeddings dimensions to two using t-SNE
# perplexity must be less than the number of samples (5 products here)
tsne = TSNE(n_components=2, perplexity=2)
embeddings_2d = tsne.fit_transform(np.array(embeddings))

# Create a scatter plot from embeddings_2d
plt.scatter(embeddings_2d[:,0], embeddings_2d[:,1])

# plt.show()


######
######
# Identify the topic each review discusses
######
######

topics = ["quality", "fit", "style", "comfort"]

# Embed the topic keywords
topic_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=topics
)

topic_embeddings = [data["embedding"] for data in topic_response.model_dump()["data"]]

# Label each review with the topic whose embedding is closest (cosine distance)
for document, embedding in zip(documents, embeddings):
    distances = [distance.cosine(embedding, topic_embedding) for topic_embedding in topic_embeddings]
    closest_topic = topics[np.argmin(distances)]
    print(f"[{closest_topic}] {document}")

## GET CLOSEST REVIEWS
def closes_3_review(query_text):
    result = collection.query(
      query_texts=[query_text],
      n_results=3
    )
    return result
most_similar_reviews = closes_3_review("Absolutely wonderful - silky and sexy and comfortable")['documents'][0]
print(most_similar_reviews)