from chroma_client import get_collection

collection = get_collection("netflix_titles")

reference_texts = ["children's story about a car", "lions"]

# Query two results using reference_texts
result = collection.query(
  query_texts=reference_texts,
  n_results=2,
  # Filter for titles with a G rating released before 2019
  where={
    '$and': [
        {"rating": 
        	{'$eq': 'G'}
        },
        {"release_year": 
         	{'$gt': 2019}
        }
    ]
  }
)

print(result['documents'])