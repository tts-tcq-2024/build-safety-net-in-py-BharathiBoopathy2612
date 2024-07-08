import unittest

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(create_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(create_soundex("M"), "M000")

    def test_two_characters(self):
        self.assertEqual(create_soundex("MI"), "M000")
        self.assertEqual(create_soundex("MB"), "M100")

    def test_three_characters(self):
        self.assertEqual(create_soundex("ART"), "A630")
        self.assertEqual(create_soundex("ABC"), "A120")

    def test_name_with_similar_sounding_letters(self):
        self.assertEqual(create_soundex("Floor"), "F460")
        self.assertEqual(create_soundex("Flower"), "F460")

    def test_name_with_varying_length(self):
        self.assertEqual(create_soundex("Ml"), "M400")
        self.assertEqual(create_soundex("Ro"), "R000")
        self.assertEqual(create_soundex("Was"), "W200")
        self.assertEqual(create_soundex("Part"), "P630")
        self.assertEqual(create_soundex("Rose"), "R200")
        self.assertEqual(create_soundex("Random"), "R535")
        self.assertEqual(create_soundex("Parent"), "P653")

    def test_name_with_repeating_characters(self):
        self.assertEqual(create_soundex("Maaa"), "M000")

    def test_name_with_non_alphabetic_characters(self):
        self.assertEqual(create_soundex("A1"), "A000")
        self.assertEqual(create_soundex("B2R"), "B600")
        self.assertEqual(create_soundex("A!@#$%^&*()"), "A000")

    def test_name_with_numbers_only(self):
        self.assertEqual(create_soundex("1234"), "1000")

    def test_char_to_soundex(self):
        self.assertEqual(char_to_soundex('B'), '1')
        self.assertEqual(char_to_soundex('F'), '1')
        self.assertEqual(char_to_soundex('P'), '1')
        self.assertEqual(char_to_soundex('V'), '1')
        self.assertEqual(char_to_soundex('C'), '2')
        self.assertEqual(char_to_soundex('G'), '2')
        self.assertEqual(char_to_soundex('J'), '2')
        self.assertEqual(char_to_soundex('K'), '2')
        self.assertEqual(char_to_soundex('Q'), '2')
        self.assertEqual(char_to_soundex('S'), '2')
        self.assertEqual(char_to_soundex('X'), '2')
        self.assertEqual(char_to_soundex('Z'), '2')
        self.assertEqual(char_to_soundex('D'), '3')
        self.assertEqual(char_to_soundex('T'), '3')
        self.assertEqual(char_to_soundex('L'), '4')
        self.assertEqual(char_to_soundex('M'), '5')
        self.assertEqual(char_to_soundex('N'), '5')
        self.assertEqual(char_to_soundex('R'), '6')
        self.assertEqual(char_to_soundex('H'), '0')
        self.assertEqual(char_to_soundex('W'), '0')
        self.assertEqual(char_to_soundex('A'), '0')
        self.assertEqual(char_to_soundex('E'), '0')
        self.assertEqual(char_to_soundex('I'), '0')
        self.assertEqual(char_to_soundex('O'), '0')
        self.assertEqual(char_to_soundex('U'), '0')
        self.assertEqual(char_to_soundex('Y'), '0')
        self.assertEqual(char_to_soundex('1'), '0')
        self.assertEqual(char_to_soundex('*'), '0')

if __name__ == '__main__':
    unittest.main()
