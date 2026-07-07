from get_response import get_response

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"You are an expert software engineer specialized in python language. You are going to receive an initial function delimited by the three backticks. This function accepts the floor width and length and returns its area. I need you to make the following modifications to the code: 1. test if the inputs to the functions are positive, and if not, display appropriate error messages. 2. if inputs are correct return the area and perimeter of the rectangle. ```{function}```"

response = get_response(prompt)
print(response)