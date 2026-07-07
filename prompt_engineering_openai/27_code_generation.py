from get_response import get_response

# Craft a prompt that asks the model for the function
prompt = "You are an expert software engineer specialized in python language. You need to create a function that receives a list of 12 floats representing monthly sales data as input and, returns the month with the highest sales value as output."

response = get_response(prompt)
print(response)