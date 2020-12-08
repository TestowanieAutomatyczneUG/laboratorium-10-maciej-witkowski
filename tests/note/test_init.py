import unittest
import pytest
from note import Note


class InitTest(unittest.TestCase):

    def test_name_not_string(self):
        with pytest.raises(TypeError, match="Name cannot be null!"):
            Note({'name': "Matematyka"}, 2)

    def test_name_empty(self):
        with pytest.raises(TypeError, match="Name cannot be null!"):
            Note("", 2)

    def test_note_not_int_or_float(self):
        with pytest.raises(TypeError, match="Note cannot be null!"):
            Note("Matematyka", "4")

    def test_note_greater_than_6(self):
        with pytest.raises(ValueError, match="Note must be between 2 and 6!"):
            Note("Matematyka", 8)

    def test_note_lower_than_2(self):
        with pytest.raises(ValueError, match="Note must be between 2 and 6!"):
            Note("Matematyka", 1.5)

    def test_right_name_and_note(self):
        note = Note("Matematyka", 3)
        self.assertEqual((note.name, note.note), ("Matematyka", 3))


if __name__ == '__main__':
    unittest.main()
