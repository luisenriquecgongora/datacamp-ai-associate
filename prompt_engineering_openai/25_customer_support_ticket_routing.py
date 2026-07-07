from get_response import get_response

ticket = """
Subject: Urgent - Login Error

Hi Support Team,

I'm having trouble accessing my account with the username "example_user." Every time I try to log in, I encounter an error message. I've already attempted to reset my password, but the issue persists. I need to resolve this problem urgently, as I have pending tasks that require immediate attention.

Please investigate and assist promptly.

Thanks,
John.
"""

# Craft a prompt to classify the ticket
prompt = f"You are an expert in customer support. You are going to receive a customer support ticket delimited by the three backticks. You need to analyze it and defined whether it is a technical issue, billing inquiry, or product feedback. ```{ticket}```"

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)