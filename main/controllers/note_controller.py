from fastapi import APIRouter, HTTPException

from main.models.note import Note
from main.services.note_service import NoteService

router = APIRouter()


@router.get("/api/note/{id}")
async def get_note(id: int):
    return NoteService().get_note_by_id(id)


@router.get("/api/notes")
async def get_all_notes():
    return NoteService().get_all_notes()


@router.post("/api/note/add")
async def add_note(note: dict):
    print("---->> Add Note <<----", note)
    NoteService().add_note(note)
    return {"message": "SUCCESS"}


@router.post("/api/note/delete")
async def delete_note(note: dict):
    print("---->> Delete Note <<----", note)
    NoteService().delete_note(note)
    return {"message": "SUCCESS"}
