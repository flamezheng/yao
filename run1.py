import os
import uuid

import requests
from PIL import Image
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG'])
app.config['UPLOAD_FOLDER'] = os.path.split(os.path.realpath(__file__))[0]
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['name'] = ''





@app.route('/', methods=['GET', 'POST'])
def change_avatar():
    return render_template('index3.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
