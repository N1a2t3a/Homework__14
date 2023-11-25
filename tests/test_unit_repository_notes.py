import unittest
from src.database.models import Note
from src.database import db_session


class TestNotes(unittest.TestCase):
    def setUp(self):
        self.user = create_test_user()  
        self.db = create_test_database()  


    def tearDown(self):
        self.db.rollback()


    def test_get_notes(self):
        notes = get_notes(0, 10, user_instance, db_session)
        self.assertIsInstance(notes, list)  


    def test_create_note(self):     
        note = create_note(NoteModel(title='Test', description='Testing'), user_instance, db_session)
        self.assertIsInstance(note, Note)  
        

    def test_get_notes(self):
        note = create_note("Title", "Description", self.user, self.db)  
        notes = get_notes(0, 10, self.user, self.db)  

        self.assertTrue(note in notes)  


    def test_create_note(self):
        note = create_note("Title", "Description", self.user, self.db)  

        self.assertIsNotNone(note)  


    def test_remove_note(self):
        note = create_note("Title", "Description", self.user, self.db) 
        removed_note = remove_note(note.id, self.user, self.db)  

        self.assertEqual(note, removed_note)  


if __name__ == '__main__':
    unittest.main()

