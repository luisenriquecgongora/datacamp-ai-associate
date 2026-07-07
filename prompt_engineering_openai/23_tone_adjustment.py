from get_response import get_response

marketing_message = """
Introducing our latest collection of premium leather handbags. Each bag is meticulously crafted using the finest leather, ensuring durability and elegance. With a variety of designs and colors, our handbags are perfect for any occasion. Shop now and experience the epitome of style and quality.
Sure! Please provide the marketing message you'd like me to translate.
"""
# Craft a prompt that translates
prompt = f"You are an expert multilingual copywriter. You are going to receive a marketing message delimited by the three backticks. You will need to take this message and generate translations on three languages: French, Spanish and Japanese. The message is the following: ```{marketing_message}```"
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)