from openai_client import client
import tiktoken
input_message = {"role": "user", "content": "I'd like to buy a shirt and a jacket. Can you suggest two color pairings for these items?"}

# Use tiktoken to create the encoding for your model
encoding = tiktoken.encoding_for_model("gpt-4o-mini")

encoded_message = encoding.encode(input_message["content"])
# Check for the number of tokens
num_tokens = len(encoded_message)

# Run the chat completions function and print the response
if num_tokens <= 15:
    response = client.chat.completions.create(model="gpt-4o-mini", messages=[input_message])
    print(response.choices[0].message.content)
else:
    print("Message exceeds token limit")