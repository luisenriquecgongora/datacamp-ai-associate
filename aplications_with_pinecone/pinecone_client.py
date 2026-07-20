"""Shared Pinecone client setup: UTF-8 stdout, .env loading, API key check."""
import os
import sys

from dotenv import load_dotenv
from pinecone import Pinecone

sys.stdout.reconfigure(encoding="utf-8")

# Load variables from the .env file into the environment
load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
if not api_key:
    raise RuntimeError(
        "PINECONE_API_KEY is not set. Add it to the .env file (never commit it)."
    )

# Create the Pinecone client
pc = Pinecone(api_key=api_key)
pc_w_threads = Pinecone(api_key=api_key, pool_threads=20)
