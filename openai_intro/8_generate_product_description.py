import sys
sys.stdout.reconfigure(encoding="utf-8")

import os

from dotenv import load_dotenv
from openai import OpenAI

# Load variables from the .env file into the environment
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Add it to the .env file (never commit it)."
    )

# Create the OpenAI client
client = OpenAI(api_key=api_key)

# Create a detailed prompt
prompt = """
You are a marketing expert.
You're writing marketing copy for SonicPro headphones.
Your goal is to generate a persuasive product description.
The copy should mention: Active noise cancellation (ANC), 40-hour battery life and Foldable design
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=300,
    temperature=1.5
)

print(response.choices[0].message.content)