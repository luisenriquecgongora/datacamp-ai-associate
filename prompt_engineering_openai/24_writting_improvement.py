from get_response import get_response

text = """
Hey guys, wanna know a cool trick? Here's how u can up your productivity game! First, download this awesome app, it's like the best thing ever! Then, just start using it and u'll see the difference. Its super easy and fun, trust me! So, what are u waiting for? Try it out now!
"""

# Craft a prompt to transform the text
prompt = f"You are a online community moderator. You are going to receive a text limited by the three backticks. You need to transform the text by doing the following steps. 1. fix grammar errors so it is proofread  2. adjust the tone to be formal and friendly. ```{text}```"

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)