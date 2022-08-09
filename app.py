"""Main module for running the Flask application."""
import uuid

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

from string_generator import StringGenerator


app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())
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

        try:
            string_generator = StringGenerator(
                num_strings=num_strings, string_length=string_length,
                has_lowercase=has_lowercase, has_uppercase=has_uppercase,
                has_numeric=has_numeric, has_special_chars=has_special_chars
            )
            strings = string_generator.get_strings()

            return redirect(url_for('get_strings'), num_strings=num_strings, strings=strings)

        except ValueError as error:
            flash(error.args[0])
            return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
