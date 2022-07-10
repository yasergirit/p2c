import face_alignment
import tensorflow
import torch
import dlib
import face_alignment
import streamlit as st


st.title("Photo to Cartoon Web App")
st.write("This App is to convert your photos to cartoon")

st.sidebar.file_uploader("Upload your photo", type=["jpeg","jpg","png"])

if img is None:
    st.write("You haven't write any image file")
else:
    st.write("**Input Photo**")
    st.image(img)
    st.write("**Output Cartoon")
    st.image(cartoon)