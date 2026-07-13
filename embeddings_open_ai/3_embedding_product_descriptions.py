from openai_client import client

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
]

# Extract a list of product short descriptions from products
product_descriptions = [product['short_description'] for product in products]

# Create embeddings for each product description
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=product_descriptions
)
response_dict = response.model_dump()

# Extract the embeddings from response_dict and store in products
for i, product in enumerate(products):
    product['embedding'] = response_dict["data"][i]["embedding"]
    
print(products[0].items())