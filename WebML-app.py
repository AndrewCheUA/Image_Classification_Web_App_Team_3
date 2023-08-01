import streamlit as st

# To run APP
# Running
#python -m streamlit run WebML-app.py

# is equivalent to in enviro:
# streamlit run WebML-app.py
st.set_page_config(page_title="Web_App_Team_3", page_icon="👨‍🎓", layout="wide")

# st.markdown('<style>h1{color: green;}</style>', unsafe_allow_html=True)
_, col, _ = st.columns([1,6,1])
col.title('*GoIt*: **group** *"Python 8"* **block** *"Data Science"*')
st.divider()
_, col, _ = st.columns([1,3,1])
col.title('**Image Classification Web App** Team-3')
st.divider()
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col2:
    st.title('Our team')
with col3:
    st.header("Andriy")
    st.image('pictures/boy.jpg', use_column_width=True)

with col4:
    st.header("Igor")
    st.image('pictures/boy in glasses.jpg', use_column_width=True)

with col5:
    st.header("Serhii")
    st.image('pictures/boy in glasses1.jpg', use_column_width=True)

with col6:
    st.header("Olga")
    st.image('pictures/girl.jpg', use_column_width=True)
st.divider()
st.write("""
### *App predicts the class of image, classification is based on the prediction of a trained convolutional neural network used pre-trained model "DenseNet121".*
""", unsafe_allow_html=True)
