from fastapi import FastAPI, Request
import asyncio
from ai_model import analyze_data, generate_initial_output, generate_diff_output
from diff_generator import generate_diff, diff_to_json
from utils import apply_diff
from commands import fetch_url

app = FastAPI()

@app.post("/data")
async def receive_data(request: Request):
    data = await request.json()
    if data["type"] == "analyze":
        routing_decision = await analyze_data(data)
        # Route to the appropriate endpoint based on the decision
        return {"status": "processed", "routing_decision": routing_decision}
    elif data["type"] == "fetch_url":
        result = fetch_url(data["url"])
        return {"status": "processed", "result": result}


#relates to the new feature to become fast and save tokens
@app.post("/initial_request")
async def initial_request(request: Request):
    data = await request.json()
    initial_output = await generate_initial_output(data['input_text'])
    return {"status": "processed", "output": initial_output}

@app.post("/request_changes")
async def request_changes(request: Request):
    data = await request.json()
    diff_output = await generate_diff_output(data['initial_text'], data['changed_text'])
    return {"status": "processed", "diff": diff_output}

@app.post("/apply_diff")
async def apply_diff_endpoint(request: Request):
    data = await request.json()
    updated_text = apply_diff(data['initial_text'], data['diff_json'])
    return {"status": "processed", "updated_text": updated_text}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
