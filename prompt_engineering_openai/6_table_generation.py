from get_response import get_response

# Create a prompt that generates the table
prompt = "You are a science fiction book expert. Please generate a table with 10 recommended books that are a must read for science fiction lovers. The table should contain the following columns: title, author and year"

# Get the response
response = get_response(prompt)
print(response)