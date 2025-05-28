from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


@router.get("/public/test")
async def test_api():
    return {"message": "Test GET API"}


@router.post("/public/test")
async def add_note(test_data: dict):
    print("---->> Test input data <<----", test_data)
    return {
        "message": "Test POST API",
        "data": test_data
    }
