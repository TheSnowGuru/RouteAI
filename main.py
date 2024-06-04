from fastapi import FastAPI, Request
from api_gateway import app
from message_queue import send_message
from ai_model import analyze_data
from endpoint_registry import update_endpoint, get_endpoint_metadata
from load_balancer import update_traefik_config
from monitor_logging import process_request
from api_gateway import app
from message_queue import send_message
from ai_model import generate_initial_output, generate_diff_output
from endpoint_registry import update_endpoint, get_endpoint_metadata
from load_balancer import update_traefik_config
from monitor_logging import process_request
from diff_generator import generate_diff, diff_to_json, apply_diff
import asyncio

app = FastAPI()

@app.post("/data")
async def receive_data(request: Request):
    data = await request.json()
    routing_decision = await analyze_data(data)
    # Route to the appropriate endpoint based on the decision
    return {"status": "processed", "routing_decision": routing_decision}


# For demonstration purposes, here we only run the API Gateway
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
