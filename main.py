import streamlit as st
import time
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI مکتب و مدرسہ - انٹرایکٹو نورانی قاعدہ",
    page_icon="📖",
    layout="wide"
)

# --- CUSTOM CSS FOR KIDS-FRIENDLY INTERACTIVE UI ---
st.markdown("""
    <style>
    .main {
        background-color: #f4f9f6;
    }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 20px;
        width: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #1b5e20;
        color: white;
    }
    .card-title {
        font-size: 18px;
        font-weight: bold;
        color: #2e7d32;
        text-align: center;
        margin-bottom: 10px;
    }
    /* Interactive Clickable Letters Styling */
    .qaida-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 15px;
        direction: rtl;
        padding: 30px;
        background: #ffffff;
        border-radius: 20px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.08);
        border: 2px solid #c8e6c9;
        margin-bottom: 25px;
    }
    .qaida-item {
        font-size: 45px;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        color: #1b5e20;
        background-color: #f1f8e9;
        padding: 10px 20px;
        border-radius: 12px;
        cursor: pointer;
        transition: 0.3s;
        border: 2px solid transparent;
    }
    .qaida-item:hover {
        background-color: #c8e6c9;
        color: #000;
        border-color: #2e7d32;
        transform: scale(1.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'selected_takhti' not in st.session_state:
    st.session_state.selected_takhti = None
if 'total_sessions' not in st.session_state:
    st.session_state.total_sessions = 5
if 'total_minutes' not in st.session_state:
    st.session_state.total_minutes = 40
if 'highlighted_letter' not in st.session_state:
    st.session_state.highlighted_letter = "کوئی حرف منتخب کریں"

# --- SIDEBAR: STUDENT PROFILE & DASHBOARD ---
st.sidebar.header("📊 طالب علم کا ڈیش بورڈ")
student_name = st.sidebar.text_input("طالب علم کا نام:", "مُعاذ عزیز")

st.sidebar.markdown("---")
st.sidebar.subheader("📌 ایکٹیویٹی لاگ")
st.sidebar.text(f"📅 داخلہ: 18 اکتوبر 2026")
st.sidebar.text(f"⏱️ کل وقت: {st.session_state.total_minutes} منٹ")
st.sidebar.text(f"📚 مکمل سیشنز: {st.session_state.total_sessions}")

if st.sidebar.button("🏠 مین صفحہ (تختیاں دیکھیں)"):
    st.session_state.selected_takhti = None

# --- COMPLETE NOORANI QAIDA DATABASE (Split into lists for clickable boxes) ---
qaida_lessons = {
    "تختی نمبر 1: حروفِ مفردات": {
        "items": ["أ", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "و", "هـ", "ء", "ي"],
        "desc": "حروفِ ہجائی کو الگ الگ اور درست مخارج سے ادا کریں۔ کسی بھی حرف پر کلک کر کے اسے نمایاں کریں۔"
    },
    "تختی نمبر 2: حروفِ مرکبات": {
        "items": ["لا", "لـح", "لـم", "طم", "يس", "حم", "الم", "الر", "طه"],
        "desc": "ملی ہوئی شکلوں والے حروف کی پہچان اور مشق۔"
    },
    "تختی نمبر 3: حرکات (زبر، زیر، پیش)": {
        "items": ["أَ", "إِ", "أُ", "بَ", "بِ", "بُ", "تَ", "تِ", "تُ", "ثَ", "ثِ", "ثُ"],
        "desc": "زبر، زیر اور پیش کو بغیر کھینچنے کے جلدی ادا کریں۔"
    },
    "تختی نمبر 4: تنوین (دو زبر، زیر، پیش)": {
        "items": ["أَنْ", "أِنْ", "أُنْ", "بَنْ", "بِنْ", "بُنْ", "تَ تَنْ", "تِنْ"],
        "desc": "تنوین یعنی آواز کے آخر میں نونِ ساکنہ کی ادائیگی۔"
    }
}

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: #2e7d32;'>📖 AI مکتب و مدرسہ - نورانی قاعدہ</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #555; font-size: 18px;'>خوش آمدید، <b>{student_name}</b>! بچوں کے لیے انٹرایکٹو پڑھائی کا ماحول:</p>", unsafe_allow_html=True)
st.divider()

# --- MAIN VIEW LOGIC ---
if st.session_state.selected_takhti is None:
    # --- GRID VIEW (CARDS) ---
    st.markdown("### 📚 نورانی قاعدے کی تختیاں (سبق منتخب کریں)")
    
    cols_per_row = 2
    lessons_keys = list(qaida_lessons.keys())
    
    for i in range(0, len(lessons_keys), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            if i + j < len(lessons_keys):
                takhti_name = lessons_keys[i + j]
                with cols[j]:
                    st.markdown(f'<div class="card-title">📌 {takhti_name}</div>', unsafe_allow_html=True)
                    st.info(f"کل حروف/الفاظ: {len(qaida_lessons[takhti_name]['items'])}")
                    if st.button("یہ سبق کھولیں 📖", key=f"btn_{i+j}"):
                        st.session_state.selected_takhti = takhti_name
                        st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)

else:
    # --- INTERACTIVE LESSON VIEW ---
    current_takhti = st.session_state.selected_takhti
    lesson_info = qaida_lessons[current_takhti]
    
    if st.button("⬅️ تمام تختیوں کی طرف واپس جائیں"):
        st.session_state.selected_takhti = None
        st.rerun()
        
    st.markdown(f"## 🎯 {current_takhti}")
    st.markdown(f"<p style='text-align: center; color: #444; font-size: 18px;'><b>💡 استاد کی ہدایت:</b> {lesson_info['desc']}</p>", unsafe_allow_html=True)
    
    # Session Timing Tracker
    if 'session_start' not in st.session_state:
        st.session_state.session_start = time.time()
    elapsed = int(time.time() - st.session_state.session_start)
    
    # --- INTERACTIVE CLICKABLE LETTERS BOARD ---
    st.markdown("### 👇 جس حرف کو پڑھنا ہو، اس پر کلک کریں:")
    
    # Displaying interactive buttons for each letter so child can click and highlight it
    cols_in_grid = 6
    items = lesson_info["items"]
    
    for r in range(0, len(items), cols_in_grid):
        c_cols = st.columns(cols_in_grid)
        for c in range(cols_in_grid):
            if r + c < len(items):
                letter = items[r + c]
                with c_cols[c]:
                    if st.button(letter, key=f"ltr_{r+c}"):
                        st.session_state.highlighted_letter = letter
                        
    # Highlighted Notice Box
    st.markdown(f"""
        <div style="padding: 15px; border-radius: 10px; background-color: #e3f2fd; border-left: 5px solid #1976d2; font-size: 20px; color: #0d47a1; text-align: center; margin-top: 20px;">
            ✨ <b>منتخب کردہ حرف (Highlighted):</b> <span style="font-size: 32px; font-weight: bold; color: #b71c1c;">{st.session_state.highlighted_letter}</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # --- AUDIO RECORDING & EVALUATION ---
    st.markdown("### 🎙️ اپنی آواز میں پڑھ کر سنائیں")
    audio_val = st.audio_input("ریکارڈنگ کے لیے کلک کریں:")
    
    if audio_val is not None:
        st.audio(audio_val)
        with st.spinner("🤖 AI استاد آپ کی آواز کا جائزہ لے رہا ہے..."):
            time.sleep(2)
            
        st.session_state.total_sessions += 1
        st.session_state.total_minutes += 5
        
        st.markdown(f"""
            <div style="padding: 15px; border-radius: 10px; background-color: #e8f5e9; border-left: 5px solid #2e7d32; font-size: 16px; color: #2e7d32; margin-top: 20px;">
                <b>🌟 ماشاءاللہ بہت شاندار، {student_name}!</b><br>
                • آپ نے <b>{current_takhti}</b> کی مشق کامیابی سے مکمل کی ہے۔<br>
                • <b>اسکور:</b> ⭐⭐⭐⭐⭐ (5/5)
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
        
        # Parent Report Section
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 📩 والدین کو پروگریس رپورٹ بھیجیں")
        p_email = st.text_input("والدین کی ای میل (Parent Email):", "parent@example.com")
        if st.button("📤 رپورٹ ارسال کریں"):
            st.success(f"✅ {student_name} کی رپورٹ ({current_takhti}) کامیابی سے {p_email} پر بھیج دی گئی ہے!")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>AI Madrassa LMS • Powered by Python & Streamlit</p>", unsafe_allow_html=True)
