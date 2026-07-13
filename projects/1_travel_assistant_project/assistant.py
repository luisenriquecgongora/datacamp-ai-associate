# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# Start coding here
# Add as many cells as you like

# Define System Prompt
system_prompt = """
Act as a virtual Parisian expert working for a company Peterman Reality Tours, delivering valuable insights into the city's iconic landmarks and hidden treasures. You will respond intelligently and directly to client inquiries. Use a user-friendly tone. 
"""
questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]
conversation = [
    {"role": "system", "content": system_prompt}
]

for q in questions:
    conversation.append({"role": "user", "content": q})
    response = client.chat.completions.create(
    model= model,
    messages=conversation, 
    temperature = 0,
    max_completion_tokens= 100)
    conversation.append({"role": "assistant", "content": response.choices[0].message.content})

print(conversation)