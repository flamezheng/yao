from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from flask import request, Flask, redirect, url_for, render_template
import os
app = Flask(__name__)

app.config['UPLOADED_PHOTO_DEST'] = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES
photos = UploadSet('PHOTO')
configure_uploads(app, photos)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/note')
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return redirect(url_for('show', name=filename))
    return render_template('index.html')

@app.route('/photo/<name>')
def show(name):
    if name is None:
        os.abort(404)
    url = photos.url(name)
    return render_template('show.html', url=url, name=name)


if __name__ == '__main__':
    app.run()