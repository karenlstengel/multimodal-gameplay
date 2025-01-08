'''
When player enters a shrine, they request to initiat the Shrine agent the previous X frames of video 
will be searched to to grab the shrine name. Then steps will be grabbed and stored for use when player asks

To do: create game state class instead of json
To do: keep track of which step player is on.
'''

from openai import OpenAI
import json
from collections.abc import Callable
from dotenv import load_dotenv

load_dotenv()

def load_json(jfile):
    with open(jfile, "r") as file:
        output_dict = json.load(file)
        return output_dict
    
    
assistant_prompt_instruction= """
You are a patient teacher and expert at solving shrines in the game Zelda:Tears of the Kingdom. 
Your goal is to grab the instructions on how to solve a given shrine from the internet, summarize them, and explain them to the player in a 
helpful, concise, yet informative manner. You must use the --- search API function to find online relevant information.
You should never use your own knowledge to answer questions.
Output the main steps, each with substeps, on how to solve the shrine. Offer the main steps then use the substeps if the player needs more help.
"""

# Load config file
config = load_json("config.json")

#load game state file
game_state = load_json("game_state.json")
shrine = game_state['current_activity']

# Initialize the OpenAI client
client = OpenAI(api_key=config["apiKey"])

# Prompt to get shrine steps
shrine_query = """
Using the website https://www.polygon.com/ find the entry for the %s from tears of the kingdom. Print out its url.
""" % (shrine)

# Create an assistant
assistant = client.beta.assistants.create(
    instructions=assistant_prompt_instruction,
    model="gpt-4-1106-preview",
    tools=[{
        "type": "function",
        "function": {
            "name": "shrine_search",
            "description": "Get solution for solving a shrine using the web",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": shrine_query},
                },
                "required": ["query"]
            }
        }
    }]
)



# Make the API call
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": prompt_url}
    ],
    max_tokens=2000,
    temperature=0.7
)

# Print the response
response_data = response.to_dict()  # Convert to a dictionary if necessary
print("Response:")
print(response_data["choices"][0]["message"]["content"])

