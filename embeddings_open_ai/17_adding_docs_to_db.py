import csv
import os

from chroma_client import create_collection

# Anchor the CSV to this folder so the script works from any working directory
csv_path = os.path.join(os.path.dirname(__file__), "netflix_titles.csv")

ids = []
documents = []

with open(csv_path, encoding="utf-8") as csvfile:
  reader = csv.DictReader(csvfile)
  for i, row in enumerate(reader):
    ids.append(row['show_id'])
    text = f"Title: {row['title']} ({row['type']})\nDescription: {row['description']}\nCategories: {row['listed_in']}"
    documents.append(text)

# Create (or reuse) the netflix_titles collection
collection = create_collection("netflix_titles")

# Add the documents and IDs to the collection (upsert keeps reruns idempotent)
collection.upsert(ids=ids, documents=documents)

# Print the collection size and first ten items
print(f"No. of documents: {collection.count()}")
print(f"First ten documents: {collection.peek(10)}")
