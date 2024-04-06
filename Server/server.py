from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'Image'
OP_UPLOAD_FOLDER = 'Op_Image'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OP_UPLOAD_FOLDER'] = OP_UPLOAD_FOLDER

@app.route('/get_img', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'wound_ana.jpg'))
            return 'File successfully uploaded'
    return render_template('index.html')

@app.route('/op_image', methods=['GET', 'POST'])  # Allow POST requests for /op_image
def op_image():
    if request.method == 'GET':
        op_image_path = os.path.join(app.config['OP_UPLOAD_FOLDER'], 'Op_wound.jpg')
        return send_from_directory(app.config['OP_UPLOAD_FOLDER'], 'Op_wound.jpg')
    elif request.method == 'POST':
        # Handle POST request for /op_image if needed
        return 'POST request handled for /op_image'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
