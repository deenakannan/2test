#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/hello') # dynamic route
def hello_user(username):
    return 'Why Hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0')   
