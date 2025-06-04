import json

from main.models.note import Note
from main.dao.note_dao import NoteDao
from main.utils.redis_cache import read_redis_data, write_redis_data
from retry import retry


class NoteService:

    @retry(exceptions=Exception, tries=3, delay=2)
    def get_note_by_id(self, id: int):
        note_data_redis = read_redis_data(f"note_{id}")
        if note_data_redis:
            print(f"-->>note_{id} found in redis, data: {note_data_redis}")
            return note_data_redis
        note_data_db = NoteDao().get_note_by_id(id)
        if note_data_db:
            print(f"-->>Save note_{id} in redis")
            write_redis_data(f"note_{id}", note_data_db.dict())

        return note_data_db

    def get_all_notes(self):
        return NoteDao().get_all_notes()

    def add_note(self, note: Note):
        return NoteDao().add_note(note)

    def delete_note(self, note: Note):
        return NoteDao().delete_note(note)
