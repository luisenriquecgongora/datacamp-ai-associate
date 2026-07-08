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

system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(system_prompt, "My new headphones aren't connecting to my device")
print(response)