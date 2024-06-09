from fastapi import FastAPI, Request
from fastapi import FastAPI, Request
from ai_model import analyze_data, generate_initial_output, generate_diff_output

app = FastAPI()

@app.post("/data")
async def receive_data(request: Request):
    data = await request.json()
    if data["type"] == "analyze":
        result = await analyze_data(data["data"])
    elif data["type"] == "generate_initial":
        result = await generate_initial_output(data["input_text"])
    elif data["type"] == "generate_diff":
        result = await generate_diff_output(data["original_text"], data["modified_text"])
    else:
        result = {"error": "Invalid type"}
    
    return {"status": "processed", "result": result}


# For demonstration purposes, here we only run the API Gateway
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
