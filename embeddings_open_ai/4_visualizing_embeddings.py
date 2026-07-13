import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

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
    
categories = [product['category'] for product in products]
embeddings = [product['embedding'] for product in products]

# Reduce the number of embeddings dimensions to two using t-SNE
# perplexity must be less than the number of samples (5 products here)
tsne = TSNE(n_components=2, perplexity=2)
embeddings_2d = tsne.fit_transform(np.array(embeddings))

# Create a scatter plot from embeddings_2d
plt.scatter(embeddings_2d[:,0], embeddings_2d[:,1])

for i, category in enumerate(categories):
    plt.annotate(category, (embeddings_2d[i, 0], embeddings_2d[i, 1]))

plt.show()

# Why must perplexity be less than the number of samples?
#
# t-SNE works by looking at each point and asking "who are my neighbors?"
# For every point, it builds a probability distribution over all the OTHER
# points, where nearby points get high probability. Perplexity is roughly
# the effective number of neighbors each point should consider — a
# perplexity of 5 means "treat each point as having about 5 meaningful
# neighbors."
#
# With 5 products, each point only has 4 other points in the entire
# dataset. You can't ask a point to consider ~5 neighbors when only 4
# exist — the math for calibrating that neighbor distribution has no
# solution. Internally, t-SNE searches for a bandwidth (a Gaussian sigma)
# for each point such that the entropy of its neighbor distribution
# matches log(perplexity), and the maximum entropy possible with n - 1
# neighbors is log(n - 1). If perplexity >= n - 1, that target is
# unreachable, so scikit-learn refuses upfront with
# "perplexity must be less than n_samples".
#
# Practical notes:
# - The typical recommendation is perplexity between 5 and 50, but that
#   assumes hundreds or thousands of points. With tiny datasets you're
#   forced to go lower — hence perplexity=2 for the 5 products here.
# - Low perplexity makes t-SNE focus on very local structure, high
#   perplexity on more global structure. With 5 points there isn't much
#   structure either way, so the plot is really just a sanity check that
#   similar categories land near each other.
# - With the full DataCamp product list (~30+ items), perplexity=5
#   becomes valid again and is a reasonable choice.

# What does np.array(embeddings) do?
#
# embeddings is a Python list of lists (5 products x 1536 floats each,
# since that's text-embedding-3-small's dimension), and np.array()
# converts it into a NumPy 2D array of shape (5, 1536).
#
# It's needed because tsne.fit_transform() expects an array-like in a
# specific shape (n_samples, n_features). Modern scikit-learn would
# actually accept the plain list of lists too and convert it internally,
# so the explicit conversion is partly stylistic — but it's a good habit
# because:
# - It makes the shape explicit — you can check
#   np.array(embeddings).shape to confirm you have (5, 1536) and not
#   something ragged.
# - It's a real data structure change, not just a cast — a list of lists
#   is scattered pointers to Python float objects all over memory; the
#   NumPy array is one contiguous block of raw numbers, which is what
#   makes the vectorized math inside t-SNE fast.
# - It fails loudly on bad data — if one embedding had a different
#   length, the conversion would produce a warning/error, instead of the
#   mismatch surfacing deeper inside scikit-learn.
#
# So: functionally "just a list -> array conversion," but under the hood
# it changes how the numbers are stored, not just what type wraps them.