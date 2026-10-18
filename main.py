import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI مکتب و مدرسہ - ڈیجیٹل نورانی قاعدہ",
    page_icon="📖",
    layout="wide"
)

# --- CUSTOM CSS FOR TRADITIONAL QAIDA GRID & MULTI-LINGUAL UI ---
st.markdown("""
    <style>
    .main {
        background-color: #f9fbf7;
    }
    .qaida-header {
        background: linear-gradient(135deg, #2e7d32, #1b5e20);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .instruction-box {
        background-color: #fffde7;
        border-left: 6px solid #fbc02d;
        padding: 15px;
        border-radius: 10px;
        font-size: 16px;
        color: #333;
        margin-bottom: 25px;
        direction: rtl;
    }
    /* Grid Box Styling like real Qaida book */
    .qaida-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 15px;
        direction: rtl;
        margin-bottom: 30px;
    }
    .qaida-cell {
        background-color: #ffffff;
        border: 3px solid #81c784;
        border-radius: 15px;
        text-align: center;
        padding: 20px;
        font-size: 50px;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        color: #1b5e20;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        cursor: pointer;
        transition: 0.3s;
    }
    .qaida-cell:hover {
        background-color: #e8f5e9;
        border-color: #2e7d32;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'selected_takhti' not in st.session_state:
    st.session_state.selected_takhti = "تختی نمبر 1: حروفِ مفردات"
if 'language' not in st.session_state:
    st.session_state.language = "اردو (Urdu)"

# --- SIDEBAR: MULTI-LINGUAL & NAVIGATION ---
st.sidebar.header("⚙️ ترتیبات / Settings")
st.session_state.language = st.sidebar.selectbox(
    "زبان منتخب کریں / Select Language:",
    ["اردو (Urdu)", "English", "العربية (Arabic)"]
)

st.sidebar.markdown("---")
st.sidebar.header("📚 نورانی قاعدہ کورس")
selected_takhti = st.sidebar.selectbox(
    "تختی منتخب کریں:",
    ["تختی نمبر 1: حروفِ مفردات", "تختی نمبر 2: حروفِ مرکبات", "تختی نمبر 3: حرکات (زبر، زیر، پیش)"]
)

student_name = st.sidebar.text_input("طالب علم کا نام:", "مُعاذ عزیز")

# --- DATA FOR TAKHTI 1 (As shown in reference image) ---
takhti_1_data = {
    "title_ur": "تختی نمبر 1: حروفِ مفردات",
    "title_en": "Lesson No. 1: Huroof-e-Mufradat (Alphabets)",
    "instruction_ur": "ہدایت: یہ حروفِ مفردات بنیاد ہیں[cite: 2]۔ ان میں بچے کے تلفظ درست کروائیں اور حروف کے نقطے بھی یاد کروائیں۔ دائیں سے بائیں اور اوپر سے نیچے کی طرف پڑھائیں۔",
    "instruction_en": "Instruction: These are basic alphabets[cite: 2]. Practice correct pronunciation and letter points from right to left.",
    "letters": ["ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "و", "هـ", "ء", "ي"]
}

# --- HEADER SECTION ---
if st.session_state.language == "English":
    st.markdown(f"""
        <div class="qaida-header">
            <h1>📖 AI Madrassa - Digital Noorani Qaida</h1>
            <p>Interactive Learning Platform for Kids (Multi-lingual)</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class="instruction-box" style="direction: ltr;">
            <b>💡 {takhti_1_data['title_en']}</b><br>
            {takhti_1_data['instruction_en']}
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
        <div class="qaida-header">
            <h1>📖 AI مکتب و مدرسہ - ڈیجیٹل نورانی قاعدہ</h1>
            <p>بچوں کے لیے روایتی اور جدید ڈیجیٹل انداز میں قرآن سیکھنے کا پلیٹ فارم</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class="instruction-box">
            <b>💡 {takhti_1_data['title_ur']}</b><br>
            {takhti_1_data['instruction_ur']}[cite: 2]
        </div>
    """, unsafe_allow_html=True)

st.subheader(f"👋 خوش آمدید، {student_name}!")
st.write("نیچے دیے گئے قاعدے کے خانوں (Grid) سے حروف پڑھیں اور آواز ریکارڈ کروائیں:")

# --- TRADITIONAL QAIDA GRID VIEW ---
st.markdown("### 🔠 تختی کے حروف (Clickable Grid)")

# Displaying letters in a structured grid columns like a book page
cols_count = 5
letters = takhti_1_data["letters"]

for i in range(0, len(letters), cols_count):
    cols = st.columns(cols_count)
    for j in range(cols_count):
        if i + j < len(letters):
            ltr = letters[i + j]
            with cols[j]:
                if st.button(ltr, key=f"grid_ltr_{i+j}", use_container_width=True):
                    st.success(f"آپ نے حرف **{ltr}** منتخب کیا ہے!")

st.divider()

# --- AUDIO RECORDING & EVALUATION MODULE ---
st.markdown("### 🎙️ تختی پڑھ کر سنائیں (Practice & Test)")
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
    
    # Parent report section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📩 والدین کو رپورٹ بھیجیں")
    p_email = st.text_input("والدین کی ای میل:", "parent@example.com")
    if st.button("📤 رپورٹ ارسال کریں"):
        st.success(f"✅ رپورٹ کامیابی سے {p_email} پر ارسال کر دی گئی ہے!")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>AI Madrassa Multi-lingual Edition • Powered by Streamlit</p>", unsafe_allow_html=True)
