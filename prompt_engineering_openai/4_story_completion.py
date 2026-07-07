from get_response import get_response

story= "Once upon a time there was a wolf in the middle of the woods..."
# Create a prompt that completes the story
prompt = f"""
    You are an expert story teller. Please complete the story delimited by the triple backtickst:
    ```{story}```
"""

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)