import streamlit as st
import json

st.set_page_config(page_title="Web_App_Team_3", page_icon="👨‍🎓", layout="wide")

st.header('**:blue[Дані навченої моделі]**')
st.subheader('Точність навчання та валідації')
st.image('model-data/Training and validation accuracy.png')
st.subheader('Втрати на навчання та валідацію')
st.image('model-data/Training and validation loss.png')

# Загрузка данных из JSON файла
with open('model-data/model_data.json', 'r') as f:
    data = json.load(f)

# Отображение данных в виде таблицы
st.title(':blue[Table: model data]', help='help')
st.table(data)