from create_embeddings import create_embeddings
from scipy.spatial import distance

# Sample products
products = [
    {
        "title": "Smartphone X1",
        "short_description": "The latest flagship smartphone with AI-powered features and 5G connectivity.",
        "price": 799.99,
        "category": "Electronics",
        "features": [
            "6.5-inch AMOLED display",
            "Quad-camera system with 48MP main sensor",
            "Face recognition and fingerprint sensor",
            "Fast wireless charging"
        ]
    },
    {
        "title": "Luxury Diamond Necklace",
        "short_description": "Elegant necklace featuring a stunning diamond pendant on an 18k gold chain.",
        "price": 1499.99,
        "category": "Beauty",
        "features": [
            "0.5 carat diamond pendant",
            "18k gold chain",
            "Adjustable length",
            "Gift box included"
        ]
    },
    {
        "title": "RC Racing Car",
        "short_description": "High-speed remote-controlled racing car for adrenaline-packed fun.",
        "price": 89.99,
        "category": "Toys",
        "features": [
            "Top speed of 30 mph",
            "Responsive remote control",
            "Rechargeable battery",
            "Durable construction"
        ]
    },
    {
        "title": "Ultra HD 4K TV",
        "short_description": "Immerse yourself in stunning visuals with this 65-inch 4K TV.",
        "price": 1299.99,
        "category": "Electronics",
        "features": [
            "65-inch 4K display",
            "Dolby Atmos sound",
            "Smart TV apps",
            "Voice remote included"
        ]
    },
    {
        "title": "Glowing Skin Serum",
        "short_description": "Revitalize your skin with this nourishing serum for a radiant glow.",
        "price": 39.99,
        "category": "Beauty",
        "features": [
            "Hyaluronic acid and vitamin C",
            "Hydrates and reduces fine lines",
            "Suitable for all skin types",
            "Cruelty-free"
        ]
    }
]

def find_n_closest(query_vector, embeddings, n=3):
  distances = []
  for index, embedding in enumerate(embeddings):
    # Calculate the cosine distance between the query vector and embedding
    dist = distance.cosine(query_vector, embedding)
    # Append the distance and index to distances
    distances.append({"distance": dist, "index": index})
  # Sort distances by the distance key
  distances_sorted = sorted(distances, key=lambda x: x['distance'])
  # Return the first n elements in distances_sorted
  return distances_sorted[:n]

# Define a function to combine the relevant features into a single string
def create_product_text(product):
  return f"""Title: {product["title"]}
Description: {product["short_description"]}
Category: {product["category"]}
Features: {", ".join(product["features"])}"""

# The last product the customer visited
last_product = {
    "title": "Wireless Noise-Canceling Headphones",
    "short_description": "Premium over-ear headphones with active noise cancellation and long battery life.",
    "price": 249.99,
    "category": "Electronics",
    "features": [
        "Active noise cancellation",
        "30-hour battery life",
        "Bluetooth 5.3 connectivity",
        "Built-in microphone for calls"
    ]
}

# Combine the features for each product
product_texts = [create_product_text(product) for product in products]

# Create the embeddings from product_texts
product_embeddings = create_embeddings(product_texts)

# Combine the features for last_product and get the embedding
last_product_text = create_product_text(last_product)
last_product_embedding = create_embeddings(last_product_text)[0]

# Find the three smallest cosine distances and their indexes
hits = find_n_closest(last_product_embedding, product_embeddings)

print(f'Recommendations based on "{last_product["title"]}"')
for hit in hits:
  # Extract the product at each index in hits
  product = products[hit['index']]
  print(product["title"])