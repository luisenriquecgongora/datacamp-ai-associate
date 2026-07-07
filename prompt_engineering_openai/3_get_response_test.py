from get_response import get_response

# Craft a prompt that follows the instructions
prompt = "You are an expert in poetry. Please generate a poem about ChatGPT while ensuring the language you use can be understoof by a child and make sure it is in english language"

# Get the response
response = get_response(prompt=prompt)

print(response)