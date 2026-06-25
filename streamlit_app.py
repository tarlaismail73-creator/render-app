import streamlit as st
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import time

st.title("AI Render Studio Pro")
uploaded_file = st.file_uploader("Mimari fotoğrafını yükle", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Yüklenen Taslak")
    
    if st.button("Profesyonel Render Al"):
        with st.spinner('AI mimari ışıklandırma ve doku optimize ediliyor...'):
            time.sleep(3)
            
            # Gelişmiş Render Filtreleri
            # 1. Kontrastı artır (daha keskin hatlar)
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(1.5)
            
            # 2. Renk doygunluğunu artır (daha canlı mimari)
            enhancer = ImageEnhance.Color(image)
            image = enhancer.enhance(1.2)
            
            # 3. Keskinleştir (detayları ortaya çıkar)
            image = image.filter(ImageFilter.SHARPEN)
            
            st.image(image, caption="AI Optimize Edilmiş Render Sonucu")
            st.success("Render tamamlandı: Işık ve doku analizi optimize edildi.")
            
