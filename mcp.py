# mcp.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY not found. Make sure it's set in your .env file.")
    # In a real app, you might raise an exception or exit
else:
    print("MCP Initialized. OpenAI API Key loaded successfully (partially hidden):", OPENAI_API_KEY[:5] + "..." + OPENAI_API_KEY[-5:])


class ModelContextProtocol:
    def __init__(self):
        self.story_context = "" # This will hold the current state of the story
        self.history = [] # Could be used for chat history or action history
        print("MCP Instance Created.")

    def update_story_context(self, new_text_segment, from_user=True):
        # For now, just append. Later, this could be more sophisticated.
        self.story_context += new_text_segment + "\n"
        source = "User" if from_user else "Agent"
        self.history.append({"source": source, "text": new_text_segment})
        print(f"MCP: Story context updated by {source}.")

    def get_story_context(self):
        return self.story_context

    def delegate_to_agent(self, agent_name, task_description):
        # This will be where we call our specific agents
        print(f"MCP: Delegating '{task_description}' to agent '{agent_name}'...")
        # In the future, this will call actual agent functions.
        # For now, just a placeholder.
        if agent_name == "plot_weaver":
            return f"Placeholder: Plot Weaver received '{task_description}'"
        elif agent_name == "character_forge":
            return f"Placeholder: Character Forge received '{task_description}'"
        elif agent_name == "scene_painter":
            return f"Placeholder: Scene Painter received '{task_description}'"
        else:
            return f"MCP Error: Agent '{agent_name}' not recognized."

# Basic test
if __name__ == "__main__":
    mcp_instance = ModelContextProtocol()
    mcp_instance.update_story_context("It was a dark and stormy night.", from_user=True)
    print("\nCurrent Story Context:")
    print(mcp_instance.get_story_context())

    suggestion = mcp_instance.delegate_to_agent("plot_weaver", "Suggest a mysterious event.")
    print(suggestion)