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

# Add the example to the prompt
prompt = """Classify sentiment as 1-5 (negative to positive):
1. Love these! = 5
2. Unbelievably good! ____
3. Shoes fell apart on the second use. ____
4. The shoes look nice, but they aren't very comfortable. ____
5. Can't wait to show them off! ____"""

response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
print(response.choices[0].message.content)