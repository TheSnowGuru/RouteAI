import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def analyze_data(data):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Analyze the following data and suggest the appropriate routing endpoint: {data}",
        max_tokens=50
    )
    decision = response.choices[0].text.strip()
    return decision
