from openai_client import client

message = "Can you show some example sentences in the past tense in French?"

# Use the moderation API
moderation_response = client.moderations.create(input=message) 

# Print the response
print(moderation_response.results[0].categories)