import unittest
from note import Note


class GetNameTest(unittest.TestCase):

    def test_get_name(self):
        self.assertEqual(self.note.getName(), "Matematyka")

    def setUp(self):
        self.note = Note("Matematyka", 4.5)

    def tearDown(self):
        self.note = None


if __name__ == '__main__':
    unittest.main()
