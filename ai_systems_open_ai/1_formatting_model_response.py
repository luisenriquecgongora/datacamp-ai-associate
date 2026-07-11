from openai_client import client

# Create the request
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
   {"role": "user", "content": "I have these notes with book titles and authors: New releases this week! The Beholders by Hester Musson, The Mystery Guest by Nita Prose. Please organize the titles and authors in a json file."}
  ],
  # Specify the response format
  response_format={"type": "json_object"}
)

# Print the response
print(response.choices[0].message.content)