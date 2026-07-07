from get_response import get_response

text= "Breaking news: AI is taking all over the physical world. Sensors have been connected to quantum chips and thow they are running by their own."
# Create the instructions
instructions = f"You are an expert in title generation for content creators. Given a piece of content, please detect the language and generate a title of a text within the triple backticks delimiters ```{text}```"

# Create the output format
output_format = """The output format should be the following:
'Text:' ____
'Language:' ____
'Title:' ___

Each one on a separate line
"""

# Create the final prompt
prompt = instructions + output_format
response = get_response(prompt)
print(response)
