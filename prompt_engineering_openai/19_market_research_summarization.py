from get_response import get_response

# Craft a prompt to summarize the report
prompt = f"""You are an expert in market research. You are going to receive a report delimited by the triple backticks delimiters. You need to summarize the report while focusing on AI and data privacy to see their effect on customers. Please use maximum five sentences ```{report}``` """
response = get_response(prompt)

print("Summarized report: \n", response)