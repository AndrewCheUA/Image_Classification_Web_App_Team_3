import streamlit as st
from function.function import get_image_dimensions, is_image


st.set_page_config(page_title="Web_App_Team_3", page_icon="👨‍🎓", layout="wide")

st.title(':red[Download picture/Завантажте картинку]', help='help')
image = st.file_uploader("", help='help')
if image:
    if is_image(image):
        st.balloons()
        st.image(image)
        width, height = get_image_dimensions(image)
        st.write("Ширина:", width)
        st.write("Высота:", height)
    else:
        st.error('This file is not picture, try again', icon="🚨")
st.title(':blue[Predict:]', help='help')
# if image:
#     # Путь к файлу сохраненной модели
#     model_path = 'path/to/your/model.h5'
#     # Загрузка модели
#     # loaded_model = load_model(model_path)
#     # Apply model to make predictions
#     # prediction = loaded_model.predict(image)