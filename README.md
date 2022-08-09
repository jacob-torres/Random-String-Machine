# Random String Machine
## Generate random strings for passwords, access keys, user ID's, and more.

In the age of increasingly sophisticated security breaches, having secure and constantly changing access credentials on the internet is more important than ever. I strongly recommend using a password manager for not only storing hundreds or thousands of random passwords and access keys, but also generating new ones and changing them as regularly as possible.

In that spirit, this application generates between 1 and 100 strings of between 1 and 100 random characters based on user specifications:

* Lowercase letters
* Uppercase letters
* Numeric digits
* Special characters

The frontend of the application is only HTML for the moment, but CSS and JavaScript will be added later.

## Usage

Clone the repository on Github.

```
 $ git clone https://github.com/jacob-torres/random-string-machine/
 $ cd random-string-machine
```

Create a new Python environment and install the requirements.

```
 $ python -m venv .venv
 $ source .venv/bin/activate
 $ pip install -r requirements.txt
```

Add the FLASK_APP environment variable:

` $ export FLASK_APP='app.py' `

Alternatively, to avoid needing to set this variable with each terminal process, copy the following into a file called .env in the root directory:

` $ echo 'FLASK_APP=app.py' > .env `

Then, start the Flask app.

` $ flask run `

Open up a browser and navigate to localhost:5000.

## Commandline Tool

The string generator is functional as both a simple (and temporarily ugly) GUI, and a commandline utility.
With a single command, it will copy a random string to the clipboard. The string_generator module is runnable with the following syntax:

` $ python string_generator/string_generator.py `

The above command copies a string of random characters to the clipboard, using all default arguments:

* num_strings = 10
* string_length = 20
* has_lowercase = True
* has_uppercase = True
* has_numeric = True
* has_special_chars = True

To pass arguments to the generator, simply add the desired arguments after the module name:

` $ python string_generator.py 10 20 True True True True `

## Future Updates

Soon, the string machine will be deployed on AWS using Lightsail. Instructions will be updated accordingly.

## Tech Stack

* Python 3
* Flask 2
* Docker
* AWS Lightsail

---
