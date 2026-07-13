import json

import requests

from openai_client import client


# Call the external exchange rate API with the extracted currency code
def get_exchange_rate(currency_code):
    url = f"https://open.er-api.com/v6/latest/{currency_code}"
    api_response = requests.get(url)
    return api_response.text


messages = [
    {
        "role": "system",
        "content": "Identify the currency code the user is asking about so the exchange rates can be looked up.",
    },
    {"role": "user", "content": "What are the current exchange rates for the euro?"},
]


def get_response(function_definition):
    # Ask the model to extract the currency code from the user message
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=function_definition,
    )
    # Only call the external API if the model actually requested our tool
    tool_calls = response.choices[0].message.tool_calls
    if not tool_calls:
        return f"No tool was called. Model replied: {response.choices[0].message.content}"

    tool_call = tool_calls[0]
    if tool_call.function.name != "get_exchange_rate":
        return f"Unexpected tool requested: {tool_call.function.name}"

    arguments = json.loads(tool_call.function.arguments)
    return get_exchange_rate(arguments["currency_code"])


# Define the function to pass to tools
function_definition = [{"type": "function",
                        "function" : {"name": "get_exchange_rate",
                                "type": "object",
                                "parameters": {"type": "object", "properties": {"currency_code": {"type": "string", "description": "curency code"}} }, 
                                "result": {"type": "string"} }}]

response = get_response(function_definition)
print(response)