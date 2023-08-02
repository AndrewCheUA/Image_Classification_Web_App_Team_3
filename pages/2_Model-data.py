import pandas as pd
import streamlit as st
# import json
from matplotlib import pyplot as plt

st.set_page_config(page_title="Model-data", page_icon="📊", layout="wide")

# st.header('**Model data**')
# st.subheader('Training and validation accuracy')
# st.image('model-data/DenseNet_model_accuracy.png')
# st.subheader('Training and validation loss')
# st.image('model-data/DenseNet_model_loss.png')

# # Загрузка данных из JSON файла
# with open('model-data/model_data.json', 'r') as f:
#     data = json.load(f)
#
# # Отображение данных в виде таблицы
# st.title('Model hiperparameters and accuracy')
# st.table(data)

st.header('**:blue[Model data: ]**')

data = pd.read_csv('model-data/history_updated.csv')

# Set up the plot 1
st.subheader('Training and Validation Accuracy')

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data['accuracy'], label='Training Accuracy', color='blue', linestyle='-')
ax.plot(data['val_accuracy'], label='Validation Accuracy', color='green', linestyle='--')
ax.set_xlabel('Epoch')
ax.set_ylabel('Accuracy')
ax.legend()
ax.grid(True)

plt.xticks(rotation=45)
st.pyplot(fig)

# Set up the plot 2
st.subheader('Training and Validation Loss')

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data['loss'], label='Training Loss', color='blue', linestyle='-')
ax.plot(data['val_loss'], label='Validation Loss', color='green', linestyle='--')
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
ax.legend()
ax.grid(True)

plt.xticks(rotation=45)
st.pyplot(fig)
