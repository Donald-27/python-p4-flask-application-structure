#!/usr/bin/env python3

from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Index route for the root URL
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Dynamic route that accepts a username as a string
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Run the Flask app if this file is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)


# CodeGrade test placeholder (should be outside app logic)
def test_codegrade_placeholder():
    """Codegrade placeholder test"""
    assert 1 == 1
