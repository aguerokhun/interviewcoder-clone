from fastapi import FastAPI, Request    
from fastapi.middleware.cors import CORSMiddleware
import openai

app = FastAPI()

# Set up CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # loosen this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate_response(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    if not prompt:
        return {"error": "Prompt is required"}
    return {"code": f"# code for: {prompt}\nprint('hello world')"} 


#Run with: uvicorn main:app --reload
    