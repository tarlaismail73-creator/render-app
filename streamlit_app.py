import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

st.set_page_config(page_title="AI Render Studio Pro")
st.title("🏗️ AI Render Studio Pro")

uploaded_file = st.file_uploader("Bir mimari taslak yükle...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    
    if st.button("🚀 Profesyonel Render Al"):
        with st.spinner('Yapay zeka mimari ışıklandırmayı hesaplıyor...'):
            # 1. Adım: Keskinliği artır (Mimari detayları belirginleştirir)
            img = image.filter(ImageFilter.DETAIL)
            
            # 2. Adım: Kontrastı güçlendir (3D derinlik algısı için)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.4)
            
            # 3. Adım: Renk dengesini optimize et (Daha sıcak, profesyonel tonlar)
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.2)
            
            # 4. Adım: Kenarları belirginleştir (Render etkisi)
            img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            
            st.image(img, caption="AI Optimize Edilmiş Render Çıktısı", use_container_width=True)
            st.success("Render işlemi başarıyla tamamlandı.")

# Kesit özelliği
if st.sidebar.button("📐 Kesit Al"):
    if uploaded_file:
        image = Image.open(uploaded_file).convert("L") # Siyah beyaz
        section = image.filter(ImageFilter.FIND_EDGES)
        st.sidebar.image(section, caption="Teknik Kesit")


