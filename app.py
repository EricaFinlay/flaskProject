"""
CP1404 2022 Prac 10
Erica Finlay
"""

from flask import Flask

app = Flask(__name__)


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)<h1>'


@app.route('/convert')
@app.route('/convert/<celsius>')
def convert(celsius=""):
    """Get user input and display celsius to fahrenheit conversion."""
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    return f"Fahrenheit = {fahrenheit}"


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    celsius = float(celsius)
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
