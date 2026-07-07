from get_response import get_response

# Create a one-shot prompt
prompt = """Extract the odd numbers from the following set : {1,3,7,12,19}. Answer: {1,3,7,19}. Extract the odd numbers from  the following set: {3, 5, 11, 12, 16} """

response = get_response(prompt)
print(response)