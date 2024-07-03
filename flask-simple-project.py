# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello,this is a simple python flask project!"

if __name__ == '__main__':
    app.run(debug=True)
