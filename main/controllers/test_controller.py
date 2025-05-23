from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


@router.get("/api/test")
async def test_api():
    return {"message": "Test API"}
