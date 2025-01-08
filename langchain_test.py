
#from openai import OpenAI
import json
from collections.abc import Callable
from dotenv import load_dotenv

from langchain.utilities import SerpAPIWrapper
from langchain.agents import Tool, load_tools, AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI

load_dotenv()

search = SerpAPIWrapper()

#intialize gpt-4
gpt4 = ChatOpenAI(model="gpt-4", temperature=0)


# create the google search tool
serp_tool = Tool(
  name="Search",
  func=search.run,
  description="useful for grabbing a website that has a walthrough solutions to a specific shrine.",
)

# Initialize tools with calculator and the model
gpt4_tools = load_tools(["llm-math"], llm=gpt4)
# add the serp tool
gpt4_tools = gpt4_tools + [serp_tool]


# initialize GPT-4 Agent
gpt4agent = initialize_agent(
  gpt4_tools,
  ChatOpenAI(model="gpt-4", temperature=0),
  agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
  verbose=True,
)

gpt4agent.run("What are the steps to solve the Riogok Shrine in Zelda: Tears of the Kingdom")