"""Shared ChromaDB client setup: UTF-8 stdout, .env loading, API key check."""
import os
import sys

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

# Load variables from the .env file into the environment
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Add it to the .env file (never commit it)."
    )

# Create a persistent client
client = chromadb.PersistentClient()


def create_collection(name, model_name="text-embedding-3-small"):
    """Create (or reuse) a collection embedded with the OpenAI embedding function."""
    return client.get_or_create_collection(
        name=name,
        embedding_function=OpenAIEmbeddingFunction(
            model_name=model_name, api_key=api_key
        ),
    )

def get_collection(name, model_name="text-embedding-3-small"):
    """Get collection embedded with the OpenAI embedding function."""
    return client.get_collection(
        name=name,
        embedding_function=OpenAIEmbeddingFunction(
            model_name=model_name, api_key=api_key
        ),
    )
