import pandas as pd
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from openai_client import api_key

llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

customers = pd.DataFrame([
    {"name": "Peak Performance Co.", "customer_id": 1, "subscription_type": "Premium", "active": True},
    {"name": "Summit Ventures", "customer_id": 2, "subscription_type": "Basic", "active": True},
    {"name": "Blue Horizon LLC", "customer_id": 3, "subscription_type": "Premium", "active": False},
])

# Define a function to retrieve customer info by-name
@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    # Filter customers for the customer's name
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()

# Call the function on Peak Performance Co.
print(retrieve_customer_info("Peak Performance Co."))

# Print the tool's arguments
print(retrieve_customer_info.args)

# Define the agent
agent = create_react_agent(llm, [retrieve_customer_info])

# Invoke the agent on the input
messages = agent.invoke({"messages": [("human", "Create a summary of our customer: Peak Performance Co.")]})
print(messages['messages'][-1].content)