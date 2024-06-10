import openai
import os
from dotenv import load_dotenv
from payload_storage import save_payload, get_payload

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
    save_payload(f"analyze_data:{data}", decision)
    return decision

async def generate_initial_output(input_text):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=input_text,
        max_tokens=1000
    )
    output = response.choices[0].text.strip()
    save_payload(f"generate_initial_output:{input_text}", output)
    return output
