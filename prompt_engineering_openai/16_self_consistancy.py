from get_response import get_response


# Create the self_consistency instruction
self_consistency_instruction = """
 Imagine 3 experts applying different calculations to find the final number of devices. The final answer is obtained by majority vote. The questions is: 
"""

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = problem_to_solve + self_consistency_instruction

response = get_response(prompt)
print(response)