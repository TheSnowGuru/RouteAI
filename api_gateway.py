from fastapi import FastAPI, Request
import asyncio
from ai_model import analyze_data

app = FastAPI()

@app.post("/data")
async def receive_data(request: Request):
    data = await request.json()
    routing_decision = await analyze_data(data)
    # Route to the appropriate endpoint based on the decision
    return {"status": "processed", "routing_decision": routing_decision}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
