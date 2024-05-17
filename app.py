from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    image.save('/path/to/save/image')
    return 'Image uploaded successfully'