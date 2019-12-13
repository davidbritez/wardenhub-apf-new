from flask import Flask, request, Response

app = Flask(__name__)
@app.route('/')
def index():
    return 'hello world'

@app.route('/api/add_user', methods=['POST'])
def add_user():
    return 200
