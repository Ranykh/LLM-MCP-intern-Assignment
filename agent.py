
import os
from dotenv import load_dotenv
load_dotenv()  # Loads environment variables from .env file

from langchain.agents import initialize_agent, Tool
from langchain_community.llms import OpenAI

from services.image_db import list_images_between
from services.yolo_detector import detect_cars

# Wrapper to parse tool inputs

def filter_images_wrapper(text: str) -> list[str]:
    parts = text.strip().split()
    if len(parts) != 2:
        return []
    start, end = parts
    return list_images_between(start, end)


def detect_cars_wrapper(image_name: str) -> str:
    found = detect_cars(image_name)
    return str(found)

# Define tools for the LLM agent
tools = [
    Tool(
        name="filter_images_by_time",
        func=filter_images_wrapper,
        description=(
            "Filters images by a given start and end time in HH:MM format. "
            "Input: 'HH:MM HH:MM'. Output: list of image filenames."
        )
    ),
    Tool(
        name="detect_cars_in_image",
        func=detect_cars_wrapper,
        description=(
            "Checks whether a given image contains a car. "
            "Input: image filename. Output: 'True' or 'False'."
        )
    )
]

# Initialize the LLM (requires OPENAI_API_KEY environment variable)
llm = OpenAI(temperature=0)

# Create a zero-shot-react-description agent
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)


def run_agent(mission: str) -> str:
    """
    Run the LLM agent on a free-form mission string.
    Returns the agent’s final output.
    """
    return agent.run(mission)
