"""Main module for running the Flask application."""
import random
from datetime import datetime
import re

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

from string_generator import StringGenerator


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
        has_lowercase = request.form.get('lowercase')
        has_uppercase = request.form.get('uppercase')
        has_numeric = request.form.get('numeric')
        has_special_chars = request.form.get('special-chars')
        error = None

        if type(num_strings) is float:
            num_strings = int(num_strings)
        elif type(num_strings) is not int:
            error = "A numeric value is required for number of strings."
        elif num_strings not in range(1, 101):
            error = "A number of strings between 1 and 100 is required."

        if type(string_length) is float:
            string_length = int(string_length)
        elif type(string_length) is not int:
            error ="A numeric value is required for string length."
        elif string_length not in range(1, 100):
            error = "A string length between 1 and 100 is required."

        if not any(
            (
                has_lowercase, has_uppercase,
                has_numeric, has_special_chars
            )
        ):
            error = "At least one type of character is required."

        # Generate strings
        string_generator = StringGenerator(
            num_strings=num_strings, string_length=string_length,
            has_lowercase=has_lowercase, has_uppercase=has_uppercase,
            has_numeric=has_numeric, has_special_chars=has_special_chars
        )

        if not error:
            string_generator.print_strings()
    else:
        flash(error)

    return render_template('get_strings.html')


if __name__ == '__main__':
    app.run(debug=True)
