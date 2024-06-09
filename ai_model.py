import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

async def analyze_data(data):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"Analyze the following data and suggest the appropriate routing endpoint: {data}",
        max_tokens=50
    )
    decision = response.choices[0].text.strip()
    return decision

async def generate_initial_output(input_text):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=input_text,
        max_tokens=1000
    )
    output = response.choices[0].text.strip()
    return output
