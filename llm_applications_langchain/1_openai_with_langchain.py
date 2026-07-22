from langchain_openai import ChatOpenAI

from openai_client import api_key

# Define the LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

# Predict the words following the text in question
prompt = 'Three reasons for using LangChain for LLM application development.'
response = llm.invoke(prompt)

print(response.content)