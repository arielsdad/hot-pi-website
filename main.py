from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/validation-key.txt')
def serve_validation():
    return send_from_directory('', 'validation-key.txt')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('', path)

app.run(host='0.0.0.0', port=3000)
