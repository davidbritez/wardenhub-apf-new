from flask import Flask, render_template, request, Response

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/add_user', methods=['POST'])
def add_user():
    return 200
