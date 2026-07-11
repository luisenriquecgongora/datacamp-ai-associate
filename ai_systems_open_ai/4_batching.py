from openai_client import client

measurements = [5.2, 3.1, 6.7]
messages = []
# Provide a system message and user messages to send the batch
messages.append({"role":"system", "content":"You are going to receive a list of measurements in kilometers. Please return a table with the values converted into miles: "})
# Append measurements to the message
[messages.append({"role": "user", "content": str(i) }) for i in measurements]

def get_response(messages):
    print("trying...")
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=messages
    )
    return response.choices[0].message.content

response = get_response(messages)
print(response)