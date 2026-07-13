import openai
from openai import OpenAI

client = OpenAI(api_key="123")

message = {"role": "user", "content": "I have these notes with book titles and authors: New releases this week! The Beholders by Hester Musson, The Mystery Guest by Nita Prose. Please organize the titles and authors in a json file."}

# Use the try statement
try:
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[message]
    )
    print(response.choices[0].message.content)
# Use the except statement
except openai.AuthenticationError:
    print("Please double check your authentication key and try again, the one provided is not valid.")