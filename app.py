# import logging
import json
import re
import numpy as np
import pickle

import io

# Image Stuff
import base64
from io import BytesIO
import face_recognition

from flask import Flask, render_template, request, Response, jsonify
import db

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/recognize')
def recognize():
    return render_template('recognize.html')

@app.route('/api/add_user', methods=['POST'])
def add_user():
    data = json.loads(request.data)

    user_face_encoding = generate_face_encodings(data['photo'])
    save_user(data['name'],data['email'],user_face_encoding)
    print(user_face_encoding)

    return "200"

@app.route('/api/recognize_user', methods=['POST'])
def process_photo():
    data = json.loads(request.data)
    user_face_encoding = match_user(data['photo'])
    return user_face_encoding


def generate_face_encodings(photo):
    # We are getting teh post with the form data:image/.. and in base 64 format.
    # Sould extract the binary data
    photo_data = re.sub('^data:image/.+;base64,', '',photo)
    user_photo = BytesIO(base64.b64decode(photo_data))

    user_face = face_recognition.load_image_file(user_photo)
    user_face_locations = face_recognition.face_locations(user_face)
    # TODO catch error if no face
    user_face_encoding = face_recognition.face_encodings(user_face, user_face_locations)[0]

    return user_face_encoding

def save_user(name, email, face_encoding):
    user_exists_query = "SELECT * FROM Usuarios WHERE email='{}';".format(email)
    user_exists = db.query_db(user_exists_query)

    # Check if face exists - could be implemented by checking the face values
    if (user_exists == []):
        face_encoding_str = face_encoding.dumps() #insert string to DB
        insert_query = "INSERT INTO Usuarios (nombre, email, rostro) VALUES(%s, %s, _binary %s);"
        data_array = (name, email, face_encoding_str)
        db.insert_db(insert_query, data_array)
    return ''


def match_user(face_encoding):
    user_face_encoding = generate_face_encodings(face_encoding)
    # Get all faces from db
    known_faces_query = "SELECT nombre, rostro from Usuarios"
    known_faces = db.query_db(known_faces_query)
    # print(known_faces)
    for face in known_faces:
        current_face = np.loads(face[1])
        print(current_face)
        match_face = face_recognition.compare_faces([current_face], user_face_encoding)
        if match_face:
            return face[0]
    # print(known_faces)
    return 'No Face Found'
    # Find if t

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
