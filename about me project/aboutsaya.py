import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi halaman Streamlit agar full-width
st.set_page_config(
    page_title="Aqsa · Profile",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS Hack untuk menghilangkan padding dan menu bawaan Streamlit
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
        /* Menyembunyikan header dan footer Streamlit */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. Membaca file HTML buatanmu
def load_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

html_content = load_html()

# 4. Menampilkan HTML di dalam komponen iframe Streamlit
# Height diset cukup tinggi agar mencakup seluruh konten (kamu bisa menyesuaikan angkanya)
components.html(html_content, height=1200, scrolling=True)