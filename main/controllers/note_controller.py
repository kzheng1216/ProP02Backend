from fastapi import APIRouter, HTTPException, Request
from main.security.auth_required import AuthRequired
from main.models.note import Note
from main.services.note_service import NoteService

router = APIRouter()


@router.get("/api/note/{id}")
@AuthRequired()
async def get_note(request: Request, id: int):
    return NoteService().get_note_by_id(id)


@router.get("/api/notes")
@AuthRequired()
async def get_all_notes(request: Request):
    return NoteService().get_all_notes()


@router.post("/api/note/add")
@AuthRequired()
async def add_note(request: Request, note: Note):
    print("---->> Add Note <<----", note)
    NoteService().add_note(note)
    return {"message": "SUCCESS"}


@router.post("/api/note/delete")
@AuthRequired()
async def delete_note(request: Request, note: Note):
    print("---->> Delete Note <<----", note)
    NoteService().delete_note(note)
    return {"message": "SUCCESS"}
