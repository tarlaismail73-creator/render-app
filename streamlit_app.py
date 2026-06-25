import streamlit as st
from PIL import Image, ImageOps
import time

st.title("AI Render Studio")
uploaded_file = st.file_uploader("Mimari fotoğrafını yükle", type=["jpg", "png"])

if uploaded_file:
    # 1. Fotoğrafı göster
    image = Image.open(uploaded_file)
    st.image(image, caption="Yüklenen Taslak")
    
    # 2. Render simülasyonu
    if st.button("Render Al"):
        with st.spinner('Yapay zeka modeli render alıyor...'):
            time.sleep(4) # İşlem süresi
            # Fotoğrafı render gibi göstermek için filtre
            render_image = ImageOps.posterize(image, 2) 
            
        # 3. Sonucu göster
        st.image(render_image, caption="AI Render Sonucu")
        st.success("İşlem başarılı! Mimari dokular optimize edildi.")
        
