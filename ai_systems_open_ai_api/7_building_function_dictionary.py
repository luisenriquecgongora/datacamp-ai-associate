from openai_client import client


def get_response(messages, function_definition):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=function_definition,
    )
    return response.choices[0].message.tool_calls[0].function.arguments


abstract = """
'Machine Learning Applications in Climate Science: A Review', published
in 2023, surveys recent advances in applying deep learning to climate
modeling, extreme weather prediction, and emissions analysis. The authors
highlight open challenges around data scarcity and model interpretability.
"""

messages = [
    {
        "role": "system",
        "content": "Extract the publication information from the text provided by the user.",
    },
    {"role": "user", "content": abstract},
]

# Function definition skeleton: the parameters dictionary starts empty
# and is filled in step by step below
function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_publication_info",
            "description": "Get the publication information from the body of the input text",
            "parameters": {},
        },
    }
]

# Define the function parameter type
function_definition[0]['function']['parameters']['type'] = "object"

# Define the function properties
function_definition[0]['function']['parameters']['properties'] = {
    "title": {
        "type": "string",
        "description": "title of the publication"
    },
    "year of publication": {
        "type": "string",
        "description": "year of publication"
    }
}

response = get_response(messages, function_definition)
print(response)