import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Konfigurasi halaman agar full-width dan rapi
st.set_page_config(
    page_title="Aqsa · Profile",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Gabungan CSS Hack untuk menghilangkan semua atribut Streamlit
st.markdown("""
    <style>
        /* Menghilangkan padding utama */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
        
        /* Menyembunyikan header, menu, dan tombol Deploy */
        header {visibility: hidden !important;}
        #MainMenu {visibility: hidden !important;}
        .stDeployButton {display: none !important;}
        
        /* Menyembunyikan footer 'Made with Streamlit' dan badge lainnya */
        footer {visibility: hidden !important;}
        .viewerBadge_container {display: none !important;}
        .viewerBadge_link {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# 3. Fungsi membaca HTML dengan path yang aman untuk Cloud
def load_html():
    # Mengambil path folder tempat file ini berada
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "index.html")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# 4. Eksekusi dan Tampilkan
try:
    html_content = load_html()
    # Height disesuaikan agar pas dengan kontenmu, scrolling diaktifkan
    components.html(html_content, height=1500, scrolling=True)
except Exception as e:
    st.error(f"Gagal memuat index.html: {e}")