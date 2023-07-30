import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.densenet import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img

# Load the trained model
model = load_model('trained_model.h5')

# Define CIFAR-10 classes
cifar10_classes = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

# Helper function to preprocess and resize the image
def preprocess_image(image):
    # Resize the image to 32x32
    image = image.resize((32, 32))
    image = img_to_array(image)
    image = preprocess_input(image)
    return image

def predict(image):
    # Preprocess the image
    image = preprocess_image(image)
    # Make a prediction
    predictions = model.predict(np.array([image]))
    # Get the predicted class index
    predicted_class_index = np.argmax(predictions)
    # Get the predicted class name
    predicted_class = cifar10_classes[predicted_class_index]
    return predicted_class

def main():
    # Set app title
    st.title("CIFAR-10 Image Classifier")
    st.write("Upload an image, and I'll predict its class from CIFAR-10 dataset.")

    # Image upload widget
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Button to make a prediction
        if st.button("Predict"):
            # Make prediction and display the result
            predicted_class = predict(image)
            st.write(f"Predicted Class: {predicted_class}")

if __name__ == '__main__':
    main()
