import pandas as pd
import streamlit as st
import json

st.set_page_config(page_title="Web_App_Team_3", page_icon="👨‍🎓", layout="wide")

st.header('**Model data**')
st.subheader('Training and validation accuracy')
st.image('model-data/DenseNet_model_accuracy.png')
st.subheader('Training and validation loss')
st.image('model-data/DenseNet_model_loss.png')

# Загрузка данных из JSON файла
with open('model-data/model_data.json', 'r') as f:
    data = json.load(f)

# Отображение данных в виде таблицы
st.title('Model hiperparameters and accuracy')
st.table(data)
