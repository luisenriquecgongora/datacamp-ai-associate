from get_response import get_response


# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: {10,4,2}. Adding them: 10+4+2=16"""

# Define the question
question = """Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14} 
              A:"""

# Create the final prompt
prompt = example + question
response = get_response(prompt)
print(response)