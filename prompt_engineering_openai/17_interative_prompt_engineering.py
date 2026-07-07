from get_response import get_response

# TRIAL 1: You are an expert in AI. Find the top 10 pre-trained language models
# TRIAL 2: You are an expert in AI. Find the top 10 pre-trained language models. After generate a table with three columns.
# Refine the following prompt
prompt = "You are an expert in AI. Find the top 10 pre-trained language models. After generate a table with three columns. The column names are: name, release year and owning company."

response = get_response(prompt)
print(response)