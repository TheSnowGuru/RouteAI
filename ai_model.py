import openai
import os
from diff_generator import apply_diff as diff_gen_apply_diff
from utils import apply_diff as utils_apply_diff
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

async def analyze_data(data):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Analyze the following data and suggest the appropriate routing endpoint: {data}",
        max_tokens=50
    )
    decision = response.choices[0].text.strip()
    return decision

async def generate_initial_output(input_text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input_text,
        max_tokens=1000
    )
    output = response.choices[0].text.strip()
    return output

#relates to the new feature to become fast and save tokens
async def generate_diff_output(original_text, modified_text):
    prompt = f"Given the original text:\n{original_text}\n\nAnd the modified text:\n{modified_text}\n\nProvide a JSON-formatted diff that includes the operations and text changes."
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    diff_output = response.choices[0].text.strip()
    # Apply the diff using both diff_generator and utils
    diff_gen_result = diff_gen_apply_diff(original_text, diff_output)
    utils_result = utils_apply_diff(original_text, diff_output)
    
    return {
        "diff_output": diff_output,
        "diff_gen_result": diff_gen_result,
        "utils_result": utils_result
    }
