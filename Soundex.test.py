import unittest

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(create_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(create_soundex("A"), "A000")

    def test_common_name(self):
        self.assertEqual(create_soundex("Smith"), "S530")

    def test_repeating_letters(self):
        self.assertEqual(create_soundex("Babbitt"), "B130")

    def test_different_letters_same_code(self):
        self.assertEqual(create_soundex("Jackson"), "J250")

    def test_short_name(self):
        self.assertEqual(create_soundex("Li"), "L000")

    def test_non_letter_characters(self):
        self.assertEqual(create_soundex("O'Brien"), "O165")

    def test_name_starts_with_vowel(self):
        self.assertEqual(create_soundex("Ellis"), "E420")

    def test_silent_letters(self):
        self.assertEqual(create_soundex("Knight"), "K523")

if __name__ == '__main__':
    unittest.main()
