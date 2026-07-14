from create_embeddings import create_embeddings
from scipy.spatial import distance
import numpy as np

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
    },
    {
        "title": "Velvet Matte Lipstick Set",
        "short_description": "A set of five long-lasting matte lipsticks in rich, versatile shades.",
        "price": 49.99,
        "category": "Beauty",
        "features": [
            "Five bold matte shades",
            "Up to 12 hours of wear",
            "Enriched with vitamin E",
            "Smudge-proof formula"
        ]
    },
    {
        "title": "Rose Gold Hair Dryer",
        "short_description": "Professional ionic hair dryer for fast drying and a frizz-free shine.",
        "price": 129.99,
        "category": "Beauty",
        "features": [
            "Ionic technology reduces frizz",
            "Three heat and two speed settings",
            "Lightweight ergonomic design",
            "Includes diffuser and concentrator nozzles"
        ]
    },
    {
        "title": "Botanical Face Mask Collection",
        "short_description": "A soothing collection of plant-based face masks for weekly self-care.",
        "price": 24.99,
        "category": "Beauty",
        "features": [
            "Aloe vera, green tea, and lavender masks",
            "Deeply hydrates and purifies",
            "Made with natural ingredients",
            "Suitable for sensitive skin"
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

# Products the user has previously browsed
user_history = [
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

# Prepare and embed the user_history, and calculate the mean embeddings
history_texts = [create_product_text(article) for article in user_history]
history_embeddings = create_embeddings(history_texts)
mean_history_embeddings = np.mean(history_embeddings, axis=0)

# Filter products to remove any in user_history
products_filtered = [product for product in products if product not in user_history ]

# Combine product features and embed the resulting texts
product_texts = [create_product_text(product) for product in products_filtered]
product_embeddings = create_embeddings(product_texts)

hits = find_n_closest(mean_history_embeddings, product_embeddings)

for hit in hits:
  product = products_filtered[hit['index']]
  print(product['title'])