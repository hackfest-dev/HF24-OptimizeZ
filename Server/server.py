from flask import Flask, jsonify
import os
import base64

app = Flask(__name__)

RES_IMAGE_FOLDER = 'resimage'
app.config['RES_IMAGE_FOLDER'] = RES_IMAGE_FOLDER

def convert_images_to_json():
    image_data = {}
    res_image_path = app.config['RES_IMAGE_FOLDER']
    for filename in os.listdir(res_image_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            with open(os.path.join(res_image_path, filename), "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data[filename] = encoded_string
    return image_data

@app.route('/getres')
def get_res_images():
    image_data = convert_images_to_json()
    return jsonify(image_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
