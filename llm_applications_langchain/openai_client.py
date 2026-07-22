"""Shared OpenAI setup for LangChain: UTF-8 stdout, .env loading, API key check."""
import os
import sys

from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")

# Load variables from the .env file into the environment
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Add it to the .env file (never commit it)."
    )
