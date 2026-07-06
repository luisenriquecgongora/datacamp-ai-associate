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

response = client.chat.completions.create(
  # Specify the model
  model="gpt-4o-mini",
  messages=[
    # Assign the correct role
    {"role": "user", 
     "content": "Announce my new AI Engineer role on LinkedIn."}]
)

print(response.choices[0])
print(response.choices[0].message.content)