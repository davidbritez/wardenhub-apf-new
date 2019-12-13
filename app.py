import logging
import json

from flask import Flask, render_template, request, Response, jsonify
# import face_recognition

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/api/add_user', methods=['POST'])
def add_user():
    data = json.loads(request.data)
    photo = data['photo']
    email = data['email']
    print(photo)
    return "200"

@app.route('/api/process_photo', methods=['POST'])
def process_photo():
    return str(200)

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 8080
    app.run(HOST, PORT, debug=True) 