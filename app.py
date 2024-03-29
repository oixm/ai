"""Simple Flash app."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Response text"""
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)
