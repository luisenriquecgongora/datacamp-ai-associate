from get_response import get_response

# Refine the following prompt
# TRIAL 1
# prompt = """
# Receiving a promotion at work made me feel on top of the world -> Happiness
# The movie's ending left me with a heavy feeling in my chest -> Sadness
# Walking alone in the dark alley sent shivers down my spine -> Fear
# ____
# ____
# They sat and ate their meal ->
# """

#TRIAL 2

prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
All together started listening to the music -> no explicit emotion
They all lay in the sofa  -> no explicit emotion
They sat and ate their meal ->
"""

response = get_response(prompt)
print(response)