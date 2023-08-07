import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

st.set_page_config(page_title="Model-data", page_icon="📊", layout="wide")

st.header('**:blue[Model data: ]**')

data = pd.read_csv('model-data/history_updated.csv')

st.write("The plot below shows the training and validation loss over epochs:")
st.write("- Test loss: 0.36%")
st.write("- Test accuracy: 0.90%")
st.write("- Train loss: 0.04%")
st.write("- Train accuracy: 0.99%")

# Set up the plot 1
centered_header = "<h1 style='text-align: center; font-size: 24px;'>Training and Validation Accuracy</h1>"
st.write(centered_header, unsafe_allow_html=True)

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
centered_header = "<h1 style='text-align: center; font-size: 24px;'>Training and Validation Loss</h1>"
st.write(centered_header, unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data['loss'], label='Training Loss', color='blue', linestyle='-')
ax.plot(data['val_loss'], label='Validation Loss', color='green', linestyle='--')
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
ax.legend()
ax.grid(True)

plt.xticks(rotation=45)
st.pyplot(fig)
