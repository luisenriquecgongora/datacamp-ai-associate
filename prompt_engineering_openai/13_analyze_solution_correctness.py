from get_response import get_response

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f"""You are a coding expert. Your task is to analyze the correctness of a piece of code delimited by the triple backticks delimiters. Here are the steps you need to take:
1. Check that the code has correct syntax
2. Check that the code receives two inputs
3. Check that the code returns one output
```{code}```
"""

response = get_response(prompt)
print(response)