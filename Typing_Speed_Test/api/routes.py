from fastapi import APIRouter, Request
from pydantic import BaseModel
from models.sentence_data import get_random_long_statement
from services.typing_logic import calculate_results

router = APIRouter()

class Submission(BaseModel):
    reference_text: str
    user_input: str
    start_time: float
    end_time: float

@router.get("/get-sentence")
def get_sentence():
    return{"sentence": get_random_long_statement()}

@router.post("/submit")
def submit(data: Submission):
    return calculate_results(
        given_text=data.reference_text,
        user_input=data.user_input,
        start_time=data.start_time,
        end_time=data.end_time
    )    