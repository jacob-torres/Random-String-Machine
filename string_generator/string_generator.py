"""Main random string generation methods."""
import random
import sys

import pyperclip


class StringGenerator:
    """The random string generator class."""

    def __init__(self, num_strings=10, string_length=20,
                has_lowercase=True, has_uppercase=True,
            has_numeric=True, has_special_chars=True):
        """
        The random string generator class accepts 6 required parameters,
        (`num_strings`, `string_length`, `has_lowercase`, `has_uppercase`,
        `has_numeric`, and `has_special_chars`,) which are used to
        determine the type of strings which will be generated.

        At least one character type value must be True.

        parameters
        ----------
        num_strings : int, default = 20
        The number of strings to generate

        string_length : int, default = 20
        The desired length of each string

        has_lowercase : bool, default = True
        Whether or not the strings will contain lowercase letters

        has_uppercase : bool, default = True
        Whether or not the strings will contain uppercase letters

        has_numeric : bool, default = True
        Whether or not the strings will contain numeric digits

        has_special_chars : bool, default = True
        Whether or not the strings will contain special characters

        raises
        ------
        ValueError : If `num_strings` or `string_length` are not
        numeric values between 1 and 100, or if all of the
        character types are False
        """
        self.num_strings = num_strings
        self.string_length = string_length
        self.has_lowercase = has_lowercase
        self.has_uppercase = has_uppercase
        self.has_numeric = has_numeric
        self.has_special_chars = has_special_chars
        self.char_types = {}

        # Check argument validity
        if self.num_strings.isnumeric():
            self.num_strings = int(self.num_strings)
        else:
            raise ValueError("A numeric value is required for number of strings.")

        if self.string_length.isnumeric():
            self.string_length = int(self.string_length)
        else:
            raise ValueError("A numeric value is required for string length.")

        if self.num_strings not in range(1, 101):
            raise ValueError("The number of strings must be between 1 and 100.")
        if self.string_length not in range(1, 101):
            raise ValueError("The string length must be between 1 and 100.")

        # Determine which types of characters will be included
        if self.has_lowercase:
            self.char_types['lowercase'] = [chr(code) for code in range(97, 123)]
        if self.has_uppercase:
            self.char_types['uppercase'] = [chr(code) for code in range(65, 91)]
        if self.has_numeric:
            self.char_types['numeric'] = [chr(code) for code in range(48, 58)]
        if self.has_special_chars:
            self.char_types['special_chars'] = [
                '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                '_', '-', '+', '=', '\\', '|', '[', ']', '{', '}',
                ' ', ',', '<', '.', '>', '/', '?', '\'', '"', ';', ':'
            ]

        if not self.char_types:
            raise ValueError("At least one character type is required.")

    def get_char_type(self):
        """
        This method randomly selects a character type.

        returns
        -------
        char_type : str
        A randomly selected character type
        """
        try:
            return random.choice(list(self.char_types.keys()))
        except IndexError:
            print("No character types have been selected to generate strings with.")

    def get_char(self):
        """
        This method selects a random character of a random type.

        returns
        -------
        char : str
        A randomly selected character
        """
        char_type = self.get_char_type()
        chars = self.char_types[char_type]
        char = random.choice(chars)
        return char

    def get_string(self):
        """
        This method generates a string of random characters.

        returns
        -------
        string : str
        A string of random characters
        """
        string = ''
        for i in range(self.string_length):
            char = self.get_char()
            string += str(char)

        return string

    def get_strings(self):
        """
        This method gets a list of a specified number of random strings.

        returns
        -------
        strings : str array
        A list of random strings
        """
        strings = []
        for i in range(self.num_strings):
            string = self.get_string()
            strings.append(string)

        return strings

    def print_strings(self):
        """This method prints a list of randomly generated strings."""
        strings = self.get_strings()
        for string in strings:
            print(string)

    def copy_string(self):
        """This method copies a single string
        of random characters to the clipboard.
        """
        string = self.get_string()
        try:
            pyperclip.copy(string)
            print("Copied to the clipboard!")
        except pyperclip.PyperclipException:
            print("Something went wrong, please try again.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        string_generator = StringGenerator()
        string_generator.copy_string()
    elif len(sys.argv) == 7:
        num_strings = sys.argv[1]
        string_length = sys.argv[2]
        has_lowercase = sys.argv[3]
        has_uppercase = sys.argv[4]
        has_numeric = sys.argv[5]
        has_special_chars = sys.argv[6]
        string_generator = StringGenerator(
            num_strings, string_length,
            has_lowercase, has_uppercase,
            has_numeric, has_special_chars
        )
        string_generator.print_strings()
    else:
        print("Wrong number of arguments.")
