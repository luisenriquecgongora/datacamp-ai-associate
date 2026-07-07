from get_response import get_response

# Create a prompt detailing steps to plan the trip
prompt = """You are an expert trip planner. I need assistance planning my beach vacation. Please proceed doing the following:

1. Please include four potential locations
2. Per each of them show me some accommodation options
3. Research for some activities per location
4. Evaluation of the pros and cons of each destination

"""

response = get_response(prompt)
print(response)