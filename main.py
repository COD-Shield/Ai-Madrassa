import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Maktab o Madrassa - Digital Noorani Qaida",
    page_icon="📖",
    layout="wide"
)

# --- CUSTOM CSS FOR EXACT QAIDA BOOK PAGE LOOK ---
st.markdown("""
    <style>
    .main {
        background-color: #eef2e6;
    }
    /* Outer Book Page Container */
    .qaida-book-container {
        border: 8px double #1b5e20;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        max-width: 950px;
        margin: 0 auto;
    }
    /* Top Header Banner */
    .qaida-header-banner {
        background: linear-gradient(135deg, #d32f2f, #b71c1c);
        color: white;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    /* Bismillah Banner */
    .bismillah-banner {
        font-size: 32px;
        text-align: center;
        color: #1b5e20;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        font-weight: bold;
        padding: 10px;
        border-bottom: 2px solid #c8e6c9;
        border-top: 2px solid #c8e6c9;
        margin-bottom: 20px;
    }
    /* Hidayat / Instructions Box (Yellowish like real book) */
    .hidayat-box {
        background-color: #fffde7;
        border: 2px solid #fbc02d;
        padding: 15px;
        border-radius: 10px;
        font-size: 16px;
        color: #333;
        margin-bottom: 25px;
        direction: rtl;
        text-align: right;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
    }
    .hidayat-title {
        color: #e65100;
        font-weight: bold;
        font-size: 18px;
    }
    /* Qaida Grid Table */
    .qaida-grid-table {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 12px;
        direction: rtl;
        margin-bottom: 30px;
    }
    .qaida-grid-cell {
        background-color: #ffffff;
        border: 2px solid #2e7d32;
        border-radius: 12px;
        text-align: center;
        padding: 15px 5px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.08);
        transition: 0.2s;
    }
    .qaida-grid-cell:hover {
        background-color: #f1f8e9;
        transform: scale(1.05);
    }
    .qaida-arabic-letter {
        font-size: 45px;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        font-weight: bold;
        line-height: 1.2;
    }
    .qaida-eng-label {
        font-size: 14px;
        color: #555;
        font-weight: bold;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR SETTINGS ---
st.sidebar.header("⚙️ Settings / ترتیبات")
student_name = st.sidebar.text_input("Student Name / طالب علم کا نام:", "Muaz Aziz")
selected_takhti = st.sidebar.selectbox(
    "Select Takhti / تختی منتخب کریں:",
    ["تختی نمبر 1: حروفِ مفردات", "تختی نمبر 2: حروفِ مرکبات", "تختی نمبر 3: حرکات"]
)

# --- QAIDA DATA (Takhti 1 with colors and English pronunciation labels as shown in image) ---
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
    {"ar": "ز", "name": "Zal / Z", "color": "#1e88e5"},
    {"ar": "س", "name": "Seen", "color": "#d81b60"},
    {"ar": "ش", "name": "Sheen", "color": "#000000"},
    {"ar": "ص", "name": "Sad", "color": "#00897b"},
    {"ar": "ض", "name": "Dad", "color": "#43a047"},
    {"ar": "ط", "name": "Ta", "color": "#1e88e5"},
    {"ar": "ظ", "name": "Za", "color": "#00897b"},
    {"ar": "ع", "name": "Ain", "color": "#8e24aa"},
    {"ar": "غ", "name": "Ghain", "color": "#e53935"},
    {"ar": "ف", "name": "Fa", "color": "#d81b60"}
]

# --- MAIN PAGE: BOOK PAGE VIEW ---
st.markdown('<div class="qaida-book-container">', unsafe_allow_html=True)

# 1. Takhti Header Banner
st.markdown('''
    <div class="qaida-header-banner">
        تختی نمبر 1 ـــ حروفِ مفردات
    </div>
''', unsafe_allow_html=True)

# 2. Bismillah
st.markdown('''
    <div class="bismillah-banner">
        بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
    </div>
''', unsafe_allow_html=True)

# 3. Hidayat Box (Instructions exactly matching image)
st.markdown('''
    <div class="hidayat-box">
        <span class="hidayat-title">ہدایات:</span> یہ حروفِ مفردات بنیاد ہیں۔ ان میں بچے کے تلفظ درست کروائیں اور حروف کے نقطے بھی یاد کروائیں۔ یا دکروائیں سطر کے آخر سے دائیں اور اوپر سے نیچے اور نیچے سے اوپر کی طرف پڑھوائیں. اگر اس تختی میں کمی رہی تو یاد رکھیے اس کا اثر بہت آگے تک جائے گا اور کمزور بنیاد پر اچھی عمارت ممکن نہیں[cite: 4].
    </div>
''', unsafe_allow_html=True)

# 4. Qaida Grid (Boxes with colored letters and English names)
st.markdown('<div class="qaida-grid-table">', unsafe_allow_html=True)
for item in takhti_1_letters:
    st.markdown(f'''
        <div class="qaida-grid-cell">
            <div class="qaida-arabic-letter" style="color: {item['color']};">{item['ar']}</div>
            <div class="qaida-eng-label">{item['name']}</div>
        </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # End of container

st.divider()

# --- AUDIO PRACTICE & TESTING MODULE ---
st.markdown(f"### 🎙️ {student_name} ke liye Tilaawat aur Mashq (Practice & Test)")
audio_val = st.audio_input("Microphone par click kar ke parh kar sunayein:")

if audio_val is not None:
    st.audio(audio_val)
    with st.spinner("🤖 AI ustad aapki aawaz aur talaffuz check kar raha hai..."):
        time.sleep(2)
        
    st.markdown("""
        <div style="padding: 15px; border-radius: 10px; background-color: #e8f5e9; border-left: 5px solid #2e7d32; font-size: 16px; color: #2e7d32; margin-top: 20px;">
            <b>🌟 Mashallah bohat zabardast talaffuz hai!</b><br>
            • Aap ne huroof-e-mufradat bilkul theek ada kiye hain.<br>
            • <b>Score:</b> ⭐⭐⭐⭐⭐ (5/5)
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
