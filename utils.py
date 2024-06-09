import requests

BASE_URL = 'http://localhost:8000'

def initial_request(input_text):
    response = requests.post(f"{BASE_URL}/initial_request", json={"input_text": input_text})
    return response.json()

def request_changes(initial_text, changed_text):
    response = requests.post(f"{BASE_URL}/request_changes", json={"initial_text": initial_text, "changed_text": changed_text})
    return response.json()

def apply_diff(original_text, diffs_json):
    diffs = [(d["operation"], d["text"]) for d in diffs_json]
    patched_texts = dmp.patch_make(original_text, diffs)
    patched_text = dmp.patch_apply(patched_texts, original_text)
    return patched_text[0]
