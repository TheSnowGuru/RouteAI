import requests

# Define the base URL of your API
BASE_URL = "http://localhost:8000/api"

# Define different payloads to test the routing
payloads = [
    {"type": "analyze", "data": "some data to analyze"},
    {"type": "generate_initial", "input_text": "some input text"},
    {"type": "generate_diff", "original_text": "original text", "modified_text": "modified text"},
]

# Function to test the API with different payloads
def test_api():
    for payload in payloads:
        response = requests.post(BASE_URL, json=payload)
        print(f"Payload: {payload}")
        print(f"Response: {response.json()}\n")

if __name__ == "__main__":
    test_api()
