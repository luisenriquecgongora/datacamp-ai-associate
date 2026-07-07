from get_response import get_response

text = "The sun was setting behind the mountains, casting a warm golden glow across the landscape."
# Create the instructions
instructions = "You are an expert in written content creation. Given a text delimited by the triple backticks delimiters, please infer the language and the number of sentences. If the text contains more than one sentence generate a title for it; otherwise, the title should be 'N/A'."

# Create the output format
output_format = """The output format should be like the following:
'Text:' ___,
'Language:' ___,
'Number of Sentences:' ___,
'Title:' ___,
"""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)