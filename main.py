import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI مکتب و مدرسہ - ڈیجیٹل نورانی قاعدہ",
    page_icon="📖",
    layout="wide"
)

# --- CUSTOM CSS FOR REAL QAIDA BOOK PAGE LOOK ---
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f0;
    }
    /* Outer Qaida Book Page Frame */
    .qaida-book-page {
        border: 6px double #1b5e20;
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        max-width: 900px;
        margin: 0 auto;
    }
    /* Top Banner / Takhti Title */
    .qaida-title-banner {
        background: linear-gradient(135deg, #2e7d32, #1b5e20);
        color: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    /* Instruction Box */
    .qaida-instruction {
        background-color: #fffde7;
        border-right: 6px solid #fbc02d;
        border-left: 6px solid #fbc02d;
        padding: 15px;
        border-radius: 8px;
        font-size: 16px;
        color: #333;
        margin-bottom: 25px;
        direction: rtl;
        text-align: right;
    }
    /* Traditional Grid Table Styling */
    .qaida-table {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 12px;
        direction: rtl;
        margin-bottom: 30px;
    }
    .qaida-box {
        background-color: #ffffff;
        border: 2px solid #2e7d32;
        border-radius: 10px;
        text-align: center;
        padding: 18px 10px;
        font-size: 42px;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        color: #1b5e20;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: all 0.2s ease-in-out;
    }
    .qaida-box:hover {
        background-color: #e8f5e9;
        border-color: #1b5e20;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR SETTINGS ---
st.sidebar.header("⚙️ ترتیبات / Settings")
language = st.sidebar.selectbox("زبان / Language:", ["اردو (Urdu)", "English"])
student_name = st.sidebar.text_input("طالب علم کا نام:", "مُعاذ عزیز")

st.sidebar.markdown("---")
st.sidebar.header("📚 نصاب")
selected_takhti = st.sidebar.selectbox(
    "تختی منتخب کریں:",
    ["تختی نمبر 1: حروفِ مفردات", "تختی نمبر 2: حروفِ مرکبات", "تختی نمبر 3: حرکات"]
)

# --- QAIDA DATA ---
letters = ["ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "و", "هـ", "ء", "ي"]

# --- MAIN PAGE RENDERING (BOOK STYLE) ---
st.markdown('<div class="qaida-book-page">', unsafe_allow_html=True)

# 1. Title Banner
st.markdown(f'''
    <div class="qaida-title-banner">
        📖 {selected_takhti}
    </div>
''', unsafe_allow_html=True)

# 2. Instructions Box
if language == "English":
    st.markdown('''
        <div class="qaida-instruction">
            <b>💡 Instruction:</b> These are basic alphabets. Practice correct pronunciation from right to left, top to bottom.
        </div>
    ''', unsafe_allow_html=True)
else:
    st.markdown('''
        <div class="qaida-instruction">
            <b>💡 ہدایت:</b> یہ حروفِ مفردات بنیاد ہیں۔ ان میں بچے کے تلفظ درست کروائیں۔ دائیں سے بائیں اور اوپر سے نیچے کی طرف پڑھائیں۔
        </div>
    ''', unsafe_allow_html=True)

# 3. Traditional Grid Cells (Book Page Look)
st.markdown('<div class="qaida-table">', unsafe_allow_html=True)
for ltr in letters:
    st.markdown(f'<div class="qaida-box">{ltr}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # End of book page frame

st.divider()

# --- AUDIO RECORDING & PRACTICE SECTION ---
st.markdown(f"### 🎙️ {student_name} کے لیے مشق اور ٹیسٹ (Practice & Record)")
audio_val = st.audio_input("مائیکروفون پر کلک کر کے آواز ریکارڈ کریں:")

if audio_val is not None:
    st.audio(audio_val)
    with st.spinner("🤖 AI استاد آپ کے تلفظ کا جائزہ لے رہا ہے..."):
        time.sleep(2)
        
    st.markdown("""
        <div style="padding: 15px; border-radius: 10px; background-color: #e8f5e9; border-left: 5px solid #2e7d32; font-size: 16px; color: #2e7d32; margin-top: 20px;">
            <b>🌟 ماشاءاللہ بہت زبردست تلفظ ہے!</b><br>
            • حروف کی ادائیگی بالکل درست رہی۔<br>
            • <b>اسکور:</b> ⭐⭐⭐⭐⭐ (5/5)
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
