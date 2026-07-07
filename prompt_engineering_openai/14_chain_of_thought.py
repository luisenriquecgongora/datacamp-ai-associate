from get_response import get_response


# Create the chain-of-thought prompt
prompt = "You are going to determine the age of your friends'father in 10 years. For that you now that your friend's father is twice your friend age and your friend is currently 20. Show the process of calculation step-by-step"

response = get_response(prompt)
print(response)