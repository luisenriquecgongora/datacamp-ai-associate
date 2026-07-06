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
   model="gpt-4o-mini",
   # Add in the extra examples and responses
   messages=[
       {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
       {"role": "user", "content": "Give me a quick summary of Portugal."},
       {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
       {"role": "user", "content": "Give me a quick summary of Spain"},
       {"role": "assistant", "content": "Spain is a country in Europe that borders France. The capital is Madrid." },
       {"role": "user", "content": "Give me a quick summary of Poland"},
       {"role": "assistant", "content": "Poland is a country in Europe that borders Germany. The capital is Warsaw"},
       {"role": "user", "content": "Give me a quick Summary of Germany"},
       {"role": "assistant", "content": "Germany is a country in Europe that borders Poland. The capital is Berlin"},
       {"role": "user", "content": "Give me a quick summary of Greece."}
   ]
)

print(response.choices[0].message.content)