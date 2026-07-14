from chroma_client import get_collection

new_data = [{"id": "s1001", "document": "Title: Cats & Dogs (Movie)\nDescription: A look at the top-secret, high-tech espionage war going on between cats and dogs, of which their human owners are blissfully unaware."},
 {"id": "s6884", "document": 'Title: Goosebumps 2: Haunted Halloween (Movie)\nDescription: Three teens spend their Halloween trying to stop a magical book, which brings characters from the "Goosebumps" novels to life.\nCategories: Children & Family Movies, Comedies'}]

# Retrieve the netflix_titles collection
collection = get_collection("netflix_titles")

# Update or add the new documents
collection.upsert(
    ids=[film['id'] for film in new_data],
    documents=[film['document'] for film in new_data]
)


# Delete the item with ID "s95"
collection.delete(
  ids=['s95'],
)

result = collection.query(
    query_texts=["films about dogs"],
    n_results=3
)
print(result)