from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import uuid
from AlefDifferent import questions

app = FastAPI()


class InputModel(BaseModel):
    category: str
    quantity: int

    class Config:
        schema_extra = {
            "example": {
                "category": "Trapezoid",
                "quantity": 3,
            }
        }


class OutputModel(BaseModel):
    uid: int
    creation_date: datetime
    questions: str
    category: str
    some_meta_data: str


@app.get("/")
async def root():
    return {"Alef Question Generation"}


@app.post('/question_gen', response_model=OutputModel)
async def create_item(request_input: InputModel):
    questionsList = questions(request_input.category, request_input.quantity)
    return {
        'uid': uuid.uuid4().int,
        'creation_date': datetime.today(),
        'category': request_input.category,
        'some_meta_data': 'meta data',
        'questions': questionsList
    }
