import numpy as np
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.densenet import preprocess_input
from PIL import Image
import io

# Load the trained model
model = load_model('trained_model.h5')

# Create a Flask app
app = Flask(__name__)

# Define a function to preprocess the uploaded image
def preprocess_image(image):
    img = Image.open(io.BytesIO(image))
    img = img.resize((32, 32))
    img_array = np.array(img)
    img_array = img_array.astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# Define the route for the upload page
@app.route('/', methods=['GET'])
def upload_page():
    return render_template('upload.html')

# Define the route for image prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        image = file.read()
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        class_index = np.argmax(predictions)
        class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
        predicted_class = class_names[class_index]
        return render_template('response.html', predicted_class=predicted_class)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run()
