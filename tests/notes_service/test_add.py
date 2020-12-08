import unittest
from mock import patch
from notes_service import NotesService
from notes_storage import NotesStorage
from note import Note


class InitTest(unittest.TestCase):

    @patch.object(NotesStorage, 'get_all_notes_of')
    def test_add_note(self, mock):
        # prepare mock
        mock.return_value = [Note("Maciej", 4), Note("Marcin", 5)]

        # testing
        self.note_service.add(Note("Marcin", 5))
        self.assertEqual(len(self.note_service.notes.get_all_notes_of("Maciej")), 2)

    @patch.object(NotesStorage, 'add')
    def test_add_note_raise(self, mock):
        # prepare mock
        mock.return_value = TypeError("Input has to be object of Note class")

        # testing
        self.assertRaises(TypeError, self.note_service.add, {'name': "Marcin", 'note': 5})

    def setUp(self):
        self.note_service = NotesService()


if __name__ == '__main__':
    unittest.main()
