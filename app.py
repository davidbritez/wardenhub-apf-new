# import logging
import json
import re
from PIL import Image
from io import BytesIO
import base64
from flask import Flask, render_template, request, Response, jsonify
import face_recognition

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

    user_face_encoding = generate_photo_encodings(data['photo'])
    print(user_face_encoding)
    
    return "200"

@app.route('/api/process_photo', methods=['POST'])
def process_photo():

    data = json.loads(request.data)
    user_face_encoding = generate_photo_encodings(data['photo'])
    print(user_face_encoding)

    return str(200)


def generate_photo_encodings(photo):
    # We are getting teh post with the form data:image/.. and in base 64 format. 
    # Sould extract the binary data

    photo_data = re.sub('^data:image/.+;base64,', '',photo)
    user_photo = BytesIO(base64.b64decode(photo_data))
    
    user_face = face_recognition.load_image_file(user_photo)
    user_face_encoding = face_recognition.face_encodings(user_face)[0]
    return user_face_encoding


def match_user(photo):
    user_face_encoding = generate_photo_encodings(photo)
    # Find if t

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 8080
    app.run(HOST, PORT, debug=True) 