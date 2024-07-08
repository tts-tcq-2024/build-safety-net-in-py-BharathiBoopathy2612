import unittest
from Soundex import generate_soundex
from Soundex import get_soundex_code

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("Z"), "Z000")

    def test_two_characters(self):
        self.assertEqual(generate_soundex("Li"), "L000")
        self.assertEqual(generate_soundex("Bo"), "B000")

    def test_three_characters(self):
        self.assertEqual(generate_soundex("Sim"), "S500")
        self.assertEqual(generate_soundex("Ken"), "K500")

    def test_name_with_similar_sounding_letters(self):
        self.assertEqual(generate_soundex("Jon"), "J500")
        self.assertEqual(generate_soundex("Jen"), "J500")

    def test_name_with_varying_length(self):
        # Names shorter than 4 characters
        self.assertEqual(generate_soundex("Ax"), "A200")
        self.assertEqual(generate_soundex("Yu"), "Y000")
        self.assertEqual(generate_soundex("Ed"), "E300")

        # Names of exactly 4 characters
        self.assertEqual(generate_soundex("Elma"), "E450")
        self.assertEqual(generate_soundex("Lana"), "L500")

        # Names longer than 4 characters
        self.assertEqual(generate_soundex("Olive"), "O410")
        self.assertEqual(generate_soundex("Elean"), "E450")

    def test_name_with_repeating_characters(self):
        self.assertEqual(generate_soundex("Lllll"), "L000")
        self.assertEqual(generate_soundex("Mmmmm"), "M000")

    def test_name_with_non_alphabetic_characters(self):
        self.assertEqual(generate_soundex("A1B2C3"), "A120")
        self.assertEqual(generate_soundex("D@E#F$G"), "D120")
        self.assertEqual(generate_soundex("H!I^J*K"), "H200")

    def test_name_with_numbers_only(self):
        self.assertEqual(generate_soundex("5678"), "5000")

    def test_mixed_case_input(self):
        self.assertEqual(generate_soundex("LeNa"), "L500")
        self.assertEqual(generate_soundex("MiTcHeLl"), "M324")

    def test_name_with_hyphens(self):
        self.assertEqual(generate_soundex("Ann-Marie"), "A560")
        self.assertEqual(generate_soundex("Jean-Paul"), "J514")

    def test_name_with_apostrophes(self):
        self.assertEqual(generate_soundex("O'Conor"), "O256")
        self.assertEqual(generate_soundex("D'Anglo"), "D524")

    def test_get_soundex_code(self):
        # Test for '1' mappings
        self.assertEqual(get_soundex_code('P'), '1')
        self.assertEqual(get_soundex_code('V'), '1')

        # Test for '2' mappings
        self.assertEqual(get_soundex_code('K'), '2')
        self.assertEqual(get_soundex_code('X'), '2')

        # Test for '3' mappings
        self.assertEqual(get_soundex_code('D'), '3')
        self.assertEqual(get_soundex_code('T'), '3')

        # Test for '4' mapping
        self.assertEqual(get_soundex_code('L'), '4')

        # Test for '5' mappings
        self.assertEqual(get_soundex_code('N'), '5')
        self.assertEqual(get_soundex_code('M'), '5')

        # Test for '6' mapping
        self.assertEqual(get_soundex_code('R'), '6')

        # Test for characters that should return '0'
        self.assertEqual(get_soundex_code('H'), '0')
        self.assertEqual(get_soundex_code('W'), '0')
        self.assertEqual(get_soundex_code('E'), '0')
        self.assertEqual(get_soundex_code('O'), '0')
        self.assertEqual(get_soundex_code('U'), '0')
        self.assertEqual(get_soundex_code('Y'), '0')
        self.assertEqual(get_soundex_code('5'), '0')
        self.assertEqual(get_soundex_code('&'), '0')

if __name__ == '__main__':
    unittest.main()
