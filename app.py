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

    # We are getting teh post with the form data:image/.. and in base 64 format. 
    # Sould extract the binary data
    photo_data = re.sub('^data:image/.+;base64,', '',data['photo'])
    photo = BytesIO(base64.b64decode(photo_data))
    email = data['email']

    user_face = face_recognition.load_image_file(photo)
    user_face_encoding = face_recognition.face_encodings(user_face)[0]
    print(user_face_encoding)
    return "200"

@app.route('/api/process_photo', methods=['POST'])
def process_photo():
    return str(200)

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 8080
    app.run(HOST, PORT, debug=True) 