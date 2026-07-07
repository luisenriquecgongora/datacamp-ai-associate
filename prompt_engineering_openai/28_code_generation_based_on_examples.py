from get_response import get_response

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = "You are an expert sofware engineer specialized in python language. Your task is to develop a Python function to calculate the project completion time based on the given input-output examples. You are given a set of examples in the examples string where different factors are associated with project completion time. Each example includes the factors' numerical values and the corresponding estimated completion time"

response = get_response(prompt)
print(response)