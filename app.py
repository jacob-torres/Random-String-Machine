import random
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask


app = Flask(__name__)
load_dotenv()


@app.route('/')
def main():
    return "Testing 1 2 3 ..."


if __name__ == '__main__':
    app.run(debug=True)
