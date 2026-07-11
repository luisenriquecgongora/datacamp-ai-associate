from openai_client import client


# Returns the full response object; extract_dictionary below digs into it
def get_response(messages, function_definition):
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=function_definition,
    )


review = """
I recently upgraded to the TechCorp ProMax and I'm loving it so far!
The powerful processor handles everything I throw at it without any lag.
It would be great if TechCorp offered more color options, though.
"""

messages = [
    {
        "role": "system",
        "content": "Extract the product name, customer sentiment, product features mentioned, and any customer suggestions from the review provided by the user.",
    },
    {"role": "user", "content": review},
]

function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_review_info",
            "description": "Get the product, sentiment, features, and suggestions from the body of the input review",
            "parameters": {
                "type": "object",
                "properties": {
                    "product": {
                        "type": "string",
                        "description": "Name of the product being reviewed",
                    },
                    "sentiment": {
                        "type": "string",
                        "description": "Overall sentiment of the review: positive, negative, or mixed",
                    },
                    "features": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Product features mentioned in the review, e.g. powerful processor",
                    },
                    "suggestions": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Suggestions or improvements the customer proposes, e.g. offer more color options",
                    },
                },
                "required": ["product", "sentiment", "features", "suggestions"],
            },
        },
    }
]

response = get_response(messages, function_definition)

# Define the function to extract the data dictionary
def extract_dictionary(response):
  return response.choices[0].message.tool_calls[0].function.arguments

# Print the data dictionary
print(extract_dictionary(response))