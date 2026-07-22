from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from openai_client import api_key

llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

# Define the tools
tools = load_tools(["wikipedia"])

# Define the agent
agent = create_react_agent(llm, tools)

# Invoke the agent
response = agent.invoke({"messages": [("human", "How many people live in New York City?")]})
print(response['messages'][-1].content)