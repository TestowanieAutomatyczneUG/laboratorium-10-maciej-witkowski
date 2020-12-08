import unittest
from mock import patch
from notes_service import NotesService
from notes_storage import NotesStorage


class ClearTest(unittest.TestCase):

    @patch.object(NotesStorage, 'get_all_notes_of')
    def test_clear(self, mock):
        # prepare mock
        mock.return_value = []

        # testing
        self.note_service.clear()
        self.assertEqual(len(self.note_service.notes.get_all_notes_of("Maciej")), 0)

    def setUp(self):
        self.note_service = NotesService()


if __name__ == '__main__':
    unittest.main()
