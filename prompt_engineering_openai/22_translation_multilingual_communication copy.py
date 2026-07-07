from get_response import get_response

sample_email = """
Subject: Check out our latest products!
    
    Dear Customer,
    
    We are excited to introduce our latest product line that includes a wide range of items to suit your needs. Whether you're looking for electronics, home appliances, or fashion accessories, we have it all!
    
    Hurry and visit our website to explore the fantastic deals and discounts we have for you. Don't miss out on the opportunity to get the best products at unbeatable prices.
    
    Thank you for being a valued customer, and we look forward to serving you soon!
    
    Best regards,
    The Marketing Team
"""

# Craft a prompt to change the email's tone
prompt = f"You are an expert copywriter. You are going to receive a marketing email on the text delimited by the three backticks. Now I need you to generate 3 email by changing the tone or the original email. These are the three tones you need to vary: professional, positive and user-centric. ```{sample_email}```"

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)