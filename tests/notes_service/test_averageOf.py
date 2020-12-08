import unittest
import pytest
from mock import patch
from notes_service import NotesService
from notes_storage import NotesStorage
from note import Note


class InitTest(unittest.TestCase):

    @patch.object(NotesStorage, 'get_all_notes_of')
    def test_averageOf(self, mock):
        # prepare mock
        mock.return_value = [Note("Maciej", 4.5), Note("Maciej", 5), Note("Maciej", 2.5)]

        # testing
        self.assertEqual(self.note_service.averageOf("Maciej"), 4)

    @patch.object(NotesStorage, 'get_all_notes_of')
    def test_averageOf_raise(self, mock):
        # prepare mock
        mock.return_value = []

        # testing
        with pytest.raises(Exception, match="This student has no grades!"):
            self.note_service.averageOf("Marcin")

    def setUp(self):
        self.note_service = NotesService()


if __name__ == '__main__':
    unittest.main()
