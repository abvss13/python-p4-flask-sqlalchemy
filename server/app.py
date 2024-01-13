# server/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask with SQLAlchemy and Migrate!'

if __name__ == '__main__':
    app.run(port=5555)
