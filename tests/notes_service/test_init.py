import unittest
from notes_service import NotesService


class InitTest(unittest.TestCase):

    def test_notes_exists(self):
        notes_service = NotesService()
        self.assertEqual(notes_service.notes.notes, [])


if __name__ == '__main__':
    unittest.main()
