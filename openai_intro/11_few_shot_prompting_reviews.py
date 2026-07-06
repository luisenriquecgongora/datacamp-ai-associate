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

# Add the final example
prompt = """Classify sentiment as 1-5 (negative to positive):
1. Comfortable, but not very pretty = 2
2. Love these! = 5
3. Unbelievably good! = 
4. Shoes fell apart on the second use. = 
5. The shoes look nice, but they aren't very comfortable. = 
6. Can't wait to show them off! = """

response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
print(response.choices[0].message.content)