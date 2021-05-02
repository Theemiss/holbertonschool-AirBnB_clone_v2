#!/usr/bin/python3
"""
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hbnb():
    """
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def index():
    """
    """
    return 'HBNB'


@app.route('/c/<text>')
def C_is(text):
    """
    """
    return 'C is {:s}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """
    """
    return 'Python {:s}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)