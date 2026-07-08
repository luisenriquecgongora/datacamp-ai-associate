from openai_client import client

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt},
      		  {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content
# Define the purpose of the chatbot
chatbot_purpose = "You are a customer support chatbot for an e-commerce company specializing in electronics. This chatbot will assist users with inquiries, order tracking, and troubleshooting common issues. "

# Define audience guidelines
audience_guidelines = "Our target audience are tech-savvy individuals interested in purchasing electronic gadgets. "

# Define tone guidelines
tone_guidelines = "Use a professional and user-friendly tone while interacting with customers"

base_system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines

# Define the order number condition
order_number_condition = "If they submitted a query about an order without specifying an order number, please ask the user for their order number."

# Define the technical issue condition
technical_issue_condition = "If the user is reporting a technical issue, start the response with I'm sorry to hear about your issue with ... "

# Create the refined system prompt
refined_system_prompt = base_system_prompt + order_number_condition + technical_issue_condition

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)