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

prompt = """
There is a perpertuity of 100 dollars a month what is the current value
"""

max_completion_tokens = 100
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=max_completion_tokens
)

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens
# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Estimated cost: ${cost}")