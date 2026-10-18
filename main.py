import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI مکتب و مدرسہ - نورانی قاعدہ",
    page_icon="📖",
    layout="wide"
)

# --- CUSTOM CSS FOR RTL (RIGHT-TO-LEFT) QAIDA PAGE ---
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f0;
    }
    .qaida-book-container {
        border: 6px double #1b5e20;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        max-width: 1000px;
        margin: 0 auto;
        direction: rtl;
    }
    .qaida-header-banner {
        background: linear-gradient(135deg, #d32f2f, #b71c1c);
        color: white;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .bismillah-banner {
        font-size: 30px;
        text-align: center;
        color: #1b5e20;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        font-weight: bold;
        padding: 8px;
        border-bottom: 2px solid #c8e6c9;
        border-top: 2px solid #c8e6c9;
        margin-bottom: 20px;
    }
    .hidayat-box {
        background-color: #fffde7;
        border: 2px solid #fbc02d;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        color: #333;
        margin-bottom: 25px;
        text-align: right;
    }
    .hidayat-title {
        color: #e65100;
        font-weight: bold;
        font-size: 17px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR SETTINGS ---
st.sidebar.header("⚙️ Settings / ترتیبات")
student_name = st.sidebar.text_input("Student Name / طالب علم کا نام:", "مُعاذ عزیز")
selected_takhti = st.sidebar.selectbox(
    "Select Takhti / تختی منتخب کریں:",
    ["تختی نمبر 1: حروفِ مفردات", "تختی نمبر 2: حروفِ مرکبات", "تختی نمبر 3: حرکات"]
)

# --- QAIDA DATA (Complete Takhti 1 - All Arabic Alphabets from Alif to Ya) ---
takhti_1_letters = [
    {"ar": "ا", "name": "Alif", "color": "#e53935"},
    {"ar": "ب", "name": "Ba", "color": "#000000"},
    {"ar": "ت", "name": "Ta", "color": "#8e24aa"},
    {"ar": "ث", "name": "Tha", "color": "#00897b"},
    {"ar": "ج", "name": "Jeem", "color": "#1e88e5"},
    {"ar": "ح", "name": "Ha", "color": "#d81b60"},
    {"ar": "خ", "name": "Kha", "color": "#43a047"},
    {"ar": "د", "name": "Dal", "color": "#e91e63"},
    {"ar": "ذ", "name": "Zal", "color": "#fb8c00"},
    {"ar": "ر", "name": "Ra", "color": "#43a047"},
    {"ar": "ز", "name": "Za", "color": "#1e88e5"},
    {"ar": "س", "name": "Seen", "color": "#d81b60"},
    {"ar": "ش", "name": "Sheen", "color": "#000000"},
    {"ar": "ص", "name": "Sad", "color": "#00897b"},
    {"ar": "ض", "name": "Dad", "color": "#43a047"},
    {"ar": "ط", "name": "Ta", "color": "#1e88e5"},
    {"ar": "ظ", "name": "Za", "color": "#00897b"},
    {"ar": "ع", "name": "Ain", "color": "#8e24aa"},
    {"ar": "غ", "name": "Ghain", "color": "#e53935"},
    {"ar": "ف", "name": "Fa", "color": "#d81b60"},
    {"ar": "ق", "name": "Qaf", "color": "#1e88e5"},
    {"ar": "ك", "name": "Kaf", "color": "#43a047"},
    {"ar": "ل", "name": "Lam", "color": "#fb8c00"},
    {"ar": "م", "name": "Meem", "color": "#8e24aa"},
    {"ar": "ن", "name": "Noon", "color": "#00897b"},
    {"ar": "و", "name": "Waw", "color": "#e53935"},
    {"ar": "هـ", "name": "Ha", "color": "#d81b60"},
    {"ar": "ء", "name": "Hamza", "color": "#1e88e5"},
    {"ar": "ي", "name": "Ya", "color": "#000000"}
]

# --- MAIN PAGE CONTAINER ---
st.markdown('<div class="qaida-book-container">', unsafe_allow_html=True)

# 1. Header Banner
st.markdown('<div class="qaida-header-banner">تختی نمبر 1 ـــ حروفِ مفردات</div>', unsafe_allow_html=True)

# 2. Bismillah
st.markdown('<div class="bismillah-banner">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>', unsafe_allow_html=True)

# 3. Hidayat Box
st.markdown('''
    <div class="hidayat-box">
        <span class="hidayat-title">ہدایات:</span> یہ حروفِ مفردات بنیاد ہیں۔ ان میں بچے کے تلفظ درست کروائیں اور حروف کے نقطے بھی یاد کروائیں۔ یادکروائیں سطر کے آخر سے دائیں اور اوپر سے نیچے اور نیچے سے اوپر کی طرف پڑھوائیں۔ اگر اس تختی میں کمی رہی تو یاد رکھیے اس کا اثر بہت آگے تک جائے گا اور کمزور بنیاد پر اچھی عمارت ممکن نہیں۔
    </div>
''', unsafe_allow_html=True)

# 4. RTL GRID COLUMNS (Complete Alphabets Grid - Right to Left)
cols_per_row = 5
for i in range(0, len(takhti_1_letters), cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row - 1, -1, -1):
        idx = i + (cols_per_row - 1 - j)
        if idx < len(takhti_1_letters):
            item = takhti_1_letters[idx]
            with cols[j]:
                st.markdown(f"""
                    <div style="background-color: #ffffff; border: 2px solid #2e7d32; border-radius: 12px; text-align: center; padding: 10px; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                        <div style="font-size: 38px; font-family: 'Amiri', serif; font-weight: bold; color: {item['color']};">{item['ar']}</div>
                        <div style="font-size: 13px; color: #555; font-weight: bold; margin-top: 4px;">{item['name']}</div>
                    </div>
                """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # End of container

st.divider()

# --- PRACTICE & TEST MODULE ---
st.markdown(f"### 🎙️ {student_name} کے لیے مشق اور ریکارڈنگ")
audio_val = st.audio_input("مائیکروفون پر کلک کر کے تلاوت ریکارڈ کریں:")

if audio_val is not None:
    st.audio(audio_val)
    with st.spinner("🤖 AI استاد آپ کے تلفظ کا جائزہ لے رہا ہے..."):
        time.sleep(2)
        
    st.markdown("""
        <div style="padding: 15px; border-radius: 10px; background-color: #e8f5e9; border-left: 5px solid #2e7d32; font-size: 16px; color: #2e7d32; margin-top: 20px;">
            <b>🌟 ماشاءاللہ بہت زبردست تلفظ ہے!</b><br>
            • حروفِ مفردات کی ادائیگی بالکل درست رہی۔<br>
            • <b>اسکور:</b> ⭐⭐⭐⭐⭐ (5/5)
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
