import numpy as np
from scipy.spatial import distance

from create_embeddings import create_embeddings

# Product catalog. The search query "soap" shares no keywords with any
# description — the match must come from meaning, and the skincare set
# should win because it is the most semantically related to soap.
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
        "short_description": "Elegant necklace featuring genuine diamonds, perfect for special occasions.",
        "price": 1499.99,
        "category": "Beauty",
        "features": [
            "18k white gold chain",
            "0.5 carat diamond pendant",
            "Adjustable chain length",
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
            "65-inch 4K UHD display",
            "Dolby Vision and HDR10+ support",
            "Smart TV with streaming apps",
            "Voice remote included"
        ]
    },
    {
        "title": "Glamorous Makeup Set",
        "short_description": "Complete makeup set for a glamorous look, including eyeshadows, lipsticks, and more.",
        "price": 59.99,
        "category": "Beauty",
        "features": [
            "20 eyeshadow shades",
            "6 vibrant lipstick colors",
            "Contour and highlight palette",
            "Makeup brushes included"
        ]
    },
    {
        "title": "Luxury Skincare Set",
        "short_description": "Nourish your skin with this luxurious skincare set, including cleanser, moisturizer, and serum.",
        "price": 129.99,
        "category": "Beauty",
        "features": [
            "Gentle cleanser",
            "Hydrating moisturizer",
            "Anti-aging serum",
            "Suitable for all skin types"
        ]
    },
]

# Embed all product descriptions in one batched API call and store each
# embedding on its product dictionary
descriptions = [product['short_description'] for product in products]
product_embeddings = create_embeddings(descriptions)
for product, embedding in zip(products, product_embeddings):
    product['embedding'] = embedding

# Embed the search text
search_text = "soap"
search_embedding = create_embeddings(search_text)[0]

distances = []

print(products[0].keys())
for product in products:
    # Compute the cosine distance for each product description
    dist = distance.cosine(search_embedding, product['embedding'])
    distances.append(dist)

# Find and print the most similar product short_description
min_dist_ind = np.argmin(distances)
print(f"\nSearch query: {search_text!r}")
print(f"Most similar product: {products[min_dist_ind]['short_description']}")

# Full ranking, most similar first, to see how the rest compare
print("\nAll products ranked by similarity (smallest distance first):")
for ind in np.argsort(distances):
    print(f"  {distances[ind]:.4f}  {products[ind]['title']}")
