# from flask import Flask, jsonify, request
# import os
# import base64
# from main_func import main_mod  # Importing main function from main_func.py

# app = Flask(__name__)

# RES_IMAGE_FOLDER = 'output'
# app.config['RES_IMAGE_FOLDER'] = RES_IMAGE_FOLDER
# UPLOAD_FOLDER = 'Image'
# OP_UPLOAD_FOLDER = 'output'

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['OP_UPLOAD_FOLDER'] = OP_UPLOAD_FOLDER

# # Function to convert images to base64 encoded JSON
# def convert_images_to_json():
#     image_data = {}
#     res_image_path = app.config['RES_IMAGE_FOLDER']
#     for filename in os.listdir(res_image_path):
#         if filename.endswith(('.jpg', '.jpeg', '.png')):
#             with open(os.path.join(res_image_path, filename), "rb") as img_file:
#                 encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
#                 image_data[filename] = encoded_string
#     return image_data

# # Route to receive image and process it
# @app.route('/post_img', methods=['GET', 'POST'])
# def upload_image():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return 'No file part'
#         file = request.files['file']
#         if file.filename == '':
#             return 'No selected file'
#         if file:
#             if not os.path.exists(app.config['UPLOAD_FOLDER']):
#                 os.makedirs(app.config['UPLOAD_FOLDER'])
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'wound_ana.jpg'))
#             main_mod()

#             return 'File successfully uploaded'
            

# # Route to get pre-processed images
# @app.route('/getres')
# def get_res_images():
#     image_data = convert_images_to_json()
#     return jsonify(image_data)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
import json
from flask import Flask, jsonify, request, send_from_directory
import os
import base64
from main_func import main_mod  # Importing main function from main_func.py

app = Flask(__name__)

RES_IMAGE_FOLDER = 'output'
app.config['RES_IMAGE_FOLDER'] = RES_IMAGE_FOLDER
UPLOAD_FOLDER = 'Image'
OP_UPLOAD_FOLDER = 'output'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OP_UPLOAD_FOLDER'] = OP_UPLOAD_FOLDER

# Function to convert images to base64 encoded JSON
def convert_images_to_json():
    image_data = {}
    res_image_path = app.config['RES_IMAGE_FOLDER']
    for filename in os.listdir(res_image_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            with open(os.path.join(res_image_path, filename), "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
                image_data[filename] = encoded_string
    return image_data

# Route to receive image and process it
@app.route('/post_img', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'wound_ana.jpg'))
        main_mod()  # Call the main_mod function to process the image
        return jsonify({"message": "File successfully uploaded and processed"}), 200

# Route to get pre-processed images
@app.route('/getres')
def get_res_images():
    image_data = convert_images_to_json()
    return jsonify(image_data)

# Route to get output JSON
@app.route('/get_output_json')
def get_output_json():
    output_path = os.path.join(app.config['OP_UPLOAD_FOLDER'], 'output.json')
    if os.path.exists(output_path):
        with open(output_path, 'r') as json_file:
            output_data = json.load(json_file)
        return jsonify(output_data)
    else:
        return jsonify({"error": "Output JSON file not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
