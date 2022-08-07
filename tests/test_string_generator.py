"""Unit test for the string_generator module."""
import re
import unittest

import pyperclip

from string_generator import StringGenerator


class TestStringGenerator(unittest.TestCase):
    """This class tests the methods of the StringGenerator class."""

    def test_no_args(self):
        """Test instantiating a StringGenerator object with no arguments."""
        # Define expected values
        num_strings_exp = 10
        string_length_exp = 20

        # Instantiate StringGenerator with no arguments
        string_generator = StringGenerator()

        # Check default num_strings and string_length
        self.assertEqual(num_strings_exp, string_generator.num_strings)
        self.assertEqual(string_length_exp, string_generator.string_length)

        # Check default character types
        self.assertTrue(string_generator.has_lowercase)
        self.assertTrue(string_generator.has_uppercase)
        self.assertTrue(string_generator.has_numeric)
        self.assertTrue(string_generator.has_special_chars)

        # Checks the values in the char_types dict
        self.assertEqual(len(string_generator.char_types), 4)
        self.assertIn('lowercase', string_generator.char_types)
        self.assertIn('uppercase', string_generator.char_types)
        self.assertIn('numeric', string_generator.char_types)
        self.assertIn('special_chars', string_generator.char_types)

    def test_get_string(self):
        """Test the get_string method."""
        # Define the expected values
        string_type_exp = str
        string_length_exp = 14
        char_types_exp = ['lowercase', 'numeric']
        string_match_exp = True

        # Instantiate a StringGenerator object with string_length of 14
        # including only lowercase letters and numeric digits
        string_generator = StringGenerator(
            string_length=14, has_uppercase=False, has_special_chars=False
        )

        # Record the length and content of the generated string
        string_result = string_generator.get_string()
        string_match = re.sub('[a-z0-9]', '', string_result)
        string_match_result = len(string_match) == 0

        # Check the type and length of the result
        self.assertIs(string_type_exp, type(string_result))
        self.assertEqual(string_length_exp, len(string_result))

        # Check the character types
        self.assertIn('lowercase', string_generator.char_types.keys())
        self.assertIn('numeric', string_generator.char_types.keys())
        self.assertNotIn('uppercase', string_generator.char_types.keys())
        self.assertNotIn('special_chars', string_generator.char_types.keys())

        # Check that only lowercase letters and digits are in the result
        self.assertEqual(string_match_exp, string_match_result)

    def test_get_strings(self):
        """Test the get_strings method."""
        # Define the expected values
        strings_type_exp = list
        num_strings_exp = 5
        string_length_exp = 50
        char_type_exp = 'uppercase'
        string_match_exp = True

        # Instantiate a StringGenerator object producing 5 strings,
        # string length of 50, and including only uppercase letters
        string_generator = StringGenerator(
            num_strings=5, string_length=50,
            has_lowercase=False, has_numeric=False, has_special_chars=False
        )

        # Record the length and content of the results
        strings_result = string_generator.get_strings()
        string_result = strings_result[0]
        string_match = re.sub('[^A-Z]', '', string_result)
        string_match_result = string_result == string_match

        # Check the type, number, and length of the string results
        self.assertIs(strings_type_exp, type(strings_result))
        self.assertEqual(num_strings_exp, len(strings_result))
        self.assertEqual(string_length_exp, len(string_result))

        # Check the result character types
        self.assertIn(char_type_exp, string_generator.char_types.keys())
        self.assertNotIn('lowercase', string_generator.char_types.keys())
        self.assertNotIn('numeric', string_generator.char_types.keys())
        self.assertNotIn('special_chars', string_generator.char_types.keys())

        # Check that only uppercase letters are in the results
        self.assertEqual(string_match_exp, string_match_result)


if __name__ == '__main__':
    unittest.main()
