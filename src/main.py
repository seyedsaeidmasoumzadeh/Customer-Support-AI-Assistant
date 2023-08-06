" API imolimenatation"
import os

from fastapi import FastAPI
from pydantic import BaseModel
from model import GenerativeModel
import uvicorn


app = FastAPI()

gen_model = GenerativeModel()
gen_model.load_model()


# request body schema using Pydantic
class CommentRequest(BaseModel):
    comment: str


# API endpoint
@app.post("/multiple_response")
def complete_comment(comment: CommentRequest):

    result = gen_model.generate_response(comment)
    return {"response": result}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
