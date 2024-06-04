import requests

BASE_URL = 'http://localhost:8000'

def initial_request(input_text):
    response = requests.post(f"{BASE_URL}/initial_request", json={"input_text": input_text})
    return response.json()

def request_changes(initial_text, changed_text):
    response = requests.post(f"{BASE_URL}/request_changes", json={"initial_text": initial_text, "changed_text": changed_text})
    return response.json()

def apply_diff(initial_text, diff_json):
    response = requests.post(f"{BASE_URL}/apply_diff", json={"initial_text": initial_text, "diff_json": diff_json})
    return response.json()
