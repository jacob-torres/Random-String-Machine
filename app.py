import random
from datetime import datetime
import re

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
load_dotenv()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/strings', methods=('GET', 'POST'))
def get_strings():
    if request.method == 'POST':
        num_strings = request.form.get('string-number')
        string_length = request.form.get('string-length')
        lowercase = request.form.get('lowercase')
        uppercase = request.form.get('uppercase')
        numeric = request.form.get('numeric')
        special_chars = request.form.get('special-chars')
        error = None

        if not num_strings:
            error = "Please specify a number of strings to generate."
        elif not string_length:
            error = "Please specify the length of strings to generate."
        elif not lowercase and not uppercase and not numeric and not special_chars:
            error = "Please select at least one type of character."
        elif not(num_strings.isnumeric() or num_strings in range(1, 101)):
            error = "Please specify a number of strings between 1 and 100."
        elif not(string_length.isnumeric() or string_length in range(1, 101)):
            error = "Please specify a string length between 1 and 100."

        if not error:
            char_types = []

            if lowercase:
                char_types.append([x for x in range(97, 123)])
            if uppercase:
                char_types.append([x for x in range(65, 91)])
            if numeric:
                strings = []
                char_types.append([x for x in range(48, 58)])
            if special_chars:
                char_types.append([33, 35, 36, 37, 38, 42, 43, 44, 45, 46, 47, 94, 95])

            for string in range(int(num_strings)):
                strings.append(
                    ''.join(
                        chr(random.choice(random.choice(char_types)))
                        for char in range(int(string_length))
                    )
                )

        else:
            flash(error)

    return render_template('get_strings.html')


if __name__ == '__main__':
    app.run(debug=True)
