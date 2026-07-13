from openai_client import client

listing_description = """
Charming single-family home for sale in Springfield, USA. Priced at
$350,000, this property features 4 bedrooms, 2 bathrooms, a spacious
backyard, and an updated kitchen. Close to schools, parks, and shopping.
"""

message_listing = [
    {
        "role": "system",
        "content": "Extract the real estate listing information from the text provided by the user.",
    },
    {"role": "user", "content": listing_description},
]

function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_listing_info",
            "description": "Get the real estate listing information from the body of the input text",
            "parameters": {
                "type": "object",
                "properties": {
                    "home type": {
                        "type": "string",
                        "description": "Type of home, e.g. single-family, condo, apartment",
                    },
                    "location": {
                        "type": "string",
                        "description": "City and country of the property",
                    },
                    "price": {
                        "type": "integer",
                        "description": "Asking price of the property in dollars",
                    },
                    "bedrooms": {
                        "type": "integer",
                        "description": "Number of bedrooms",
                    },
                },
                "required": ["home type", "location", "price", "bedrooms"],
            },
        },
    }
]

response= client.chat.completions.create(
    model="gpt-4o-mini",
    # Add the message 
    messages=message_listing,
    # Add your function definition
    tools=function_definition
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)