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

messages = [
    {"role": "system", "content": "You are a helpful math tutor that speaks concisely."},
    {"role": "user", "content": "Explain what pi is."}
]

# Send the chat messages to the model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    max_completion_tokens=100
)

# Extract the assistant message from the response
assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}

# Add assistant_dict to the messages dictionary
messages.append(assistant_dict)
print(messages)