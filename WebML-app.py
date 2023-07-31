import streamlit as st

# To run APP
# Running
#python -m streamlit run WebML-app.py

# is equivalent to in enviro:
# streamlit run WebML-app.py
st.set_page_config(page_title="Web_App_Team_3", page_icon="👨‍🎓", layout="wide")

# st.markdown('<style>h1{color: green;}</style>', unsafe_allow_html=True)
st.title('Image Classification Web App Team_3')

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col2:
    st.title('Our team')
with col3:
    st.header("Андрій")
    st.image('pictures/boy.jpg', use_column_width=True)

with col4:
    st.header("Ігор")
    st.image('pictures/boy in glasses.jpg', use_column_width=True)

with col5:
    st.header("Сергій")
    st.image('pictures/boy in glasses1.jpg', use_column_width=True)

with col6:
    st.header("Ольга")
    st.image('pictures/girl.jpg', use_column_width=True)

st.write("""
# Image classification APP

This app predicts the class of image, 
Classification is based on the prediction of a trained convolutional neural network model based on the "___________"
model and pre-trained.   
""", unsafe_allow_html=True)
