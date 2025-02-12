# from flask import Flask, request, jsonify
# import util

# app = Flask(__name__)


# @app.route('/classify_image', methods=['GET', 'POST'])
# def classify_image():
#     image_data = request.files['image_data']

#     response = jsonify(util.classify_image(image_data))

#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

# if __name__ == "__main__":
#     print("Starting Python Flask Server For Sports Celebrity Image Classification")
#     util.load_saved_artifacts()
#     app.run(port=5000)
from flask import Flask, request, jsonify
import util
import base64

app = Flask(__name__)

@app.route('/classify_image', methods=['POST'])
def classify_image():
    if 'image_data' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image_data']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Read file data and convert it to base64 string
    image_data = base64.b64encode(file.read()).decode('utf-8')

    response = jsonify(util.classify_image(image_data))  # Pass base64 string
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
