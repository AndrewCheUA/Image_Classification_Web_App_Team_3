import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from function.function import get_image_dimensions, is_image, preprocess_image
from PIL import Image
import numpy as np

st.set_page_config(page_title="Web_App_Team_3", page_icon="👨‍🎓", layout="wide")

st.title(':red[Download picture/Завантажте картинку]', help='help')
image = st.file_uploader("", help='help')

if image:
    if is_image(image):
        st.balloons()
        st.image(image)
        width, height = get_image_dimensions(image)
        st.write("Width:", width)
        st.write("Height:", height)

        # Check if the user has clicked the prediction button
        if st.button("Predict"):
            # Load the trained model
            model_path = 'trained_model.h5'  # Replace with the actual path to the saved model
            loaded_model = load_model(model_path)

            # Preprocess the image for prediction
            processed_image = preprocess_image(image)

            # Make prediction using the loaded model
            predictions = loaded_model.predict(processed_image)

            cifar10_classes = [
                'airplane', 'automobile', 'bird', 'cat', 'deer',
                'dog', 'frog', 'horse', 'ship', 'truck'
            ]

            predicted_class_index = np.argmax(predictions)
            predicted_class_label = cifar10_classes[predicted_class_index]

            st.write("Predicted Class:", predicted_class_label)
    else:
        st.error('This file is not a picture, try again', icon="🚨")
