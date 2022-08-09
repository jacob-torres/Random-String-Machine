"""Main module for running the Flask application."""
from uuid import uuid4

from dotenv import load_dotenv
from flask import Flask, flash, render_template, request

from string_generator import StringGenerator


app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid4())
load_dotenv()


@app.route('/', methods=['GET', 'POST'])
def index():
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

            return render_template('strings.html', num_strings=num_strings, strings=strings)

        except ValueError as error:
            flash(error.args[0])

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
