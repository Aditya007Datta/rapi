from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Variable to store the last answer
last_answer = None

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/answer/{user}")
async def get_answer(user: str):
    global last_answer
    if user == "yes":
        last_answer = {"answer": "yes"}
        return last_answer
    if user == "no":
        last_answer = {"answer": "no"}
        return last_answer

@app.get("/api/answer/")
async def get_last_answer():
    global last_answer
    if last_answer:
        return last_answer
    else:
        # return {"error": "No answer has been set yet"}
        return {"answer": "yes"}
