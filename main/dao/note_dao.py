from http.client import HTTPException

from main.utils.db_conn import DBConnection
from main.dao.base_dao import BaseDao
from main.models.note import Note
from main.utils.singleton import singleton


@singleton
class NoteDao(BaseDao):

    def get_note_by_id(self, id) -> Note:
        with DBConnection() as cursor:
            cursor.execute("SELECT id, title, content, created_at FROM note WHERE id = %s", (id,))
            note_data = cursor.fetchone()
            if note_data is None:
                raise HTTPException(status_code=404, detail="Note not found")
            return Note(**note_data)

    def get_all_notes(self) -> list:
        with DBConnection() as cursor:
            cursor.execute("SELECT id, title, content, created_at FROM note")

            note_list = []
            for row in cursor.fetchall():
                n = Note(**row)
                note_list.append(n)
            return note_list

    def add_note(self, note: Note):
        print(note.title)
        with DBConnection() as cursor:
            cursor.execute("INSERT INTO note (title, content) VALUES (%s, %s)", (note.title, note.content))

    def delete_note(self, note: Note):
        with DBConnection() as cursor:
            cursor.execute("DELETE FROM note WHERE id = %s", (note.id,))
