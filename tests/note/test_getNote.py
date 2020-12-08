import unittest
from note import Note


class GetNoteTest(unittest.TestCase):

    def test_get_note(self):
        self.assertEqual(self.note.getNote(), 4.5)

    def setUp(self):
        self.note = Note("Matematyka", 4.5)

    def tearDown(self):
        self.note = None


if __name__ == '__main__':
    unittest.main()
