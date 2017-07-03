import os
import uuid

import requests
from PIL import Image
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def change_avatar():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            my_url = filename = getParams(file)
            return render_template('final.html', url="/static/image/" + my_url)
        else:
            print("文件格式不正确");
            return "出错啦"
    else:
        return render_template('index.html')


def getParams(file):
    body = {"api_key": "5vyAcgenWeFvm1y8BkzcDHeCdSM9Xs9g",
            "api_secret": "m8h-I8ZWsU5200q6vozCZmhEKcu1oA2-",
            }
    files = {'image_file': open(file.filename, 'rb')}
    r = requests.post("https://api-cn.faceplusplus.com/facepp/v3/detect", body, files=files, timeout=8);
    rectangle_ = r.json()['faces'][0]['face_rectangle']
    print(rectangle_['top']);
    print(rectangle_['width']);
    print(rectangle_['left']);
    print(rectangle_['height']);

    # 左上右下
    box = (rectangle_['left'], rectangle_['top'],
           rectangle_['left'] + rectangle_['width'], rectangle_['top'] + rectangle_['height'])
    # 裁剪脸部
    example = Image.open(file.filename)
    region = example.crop(box)
    region.thumbnail((45, 45))
    img = region.convert("RGBA")
    datas = img.getdata()
    # 把白色的部分变为透明
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    pic_id = uuid.uuid4().__str__()
    img.save(os.path.join(app.config['UPLOAD_FOLDER'])+"/static/image/"+ pic_id+ ".png", "PNG")
    return pic_id + '.png'

    # return render_template('final.html')


if __name__ == '__main__':
    app.run()
