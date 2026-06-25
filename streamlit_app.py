import streamlit as st

st.title("AI Render Studio")
uploaded_file = st.file_uploader("Fotoğraf yükle", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file)
    st.success("Görsel başarıyla yüklendi ve işleme alındı.")
  
