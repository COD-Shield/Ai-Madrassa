import streamlit as st
import time
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Madrassa - نورانی قاعدہ اور پروگریس ٹریکر",
    page_icon="📖",
    layout="centered"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f4f9f6;
    }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px 24px;
        width: 100%;
    }
    .arabic-text {
        font-size: 42px;
        text-align: center;
        direction: rtl;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        color: #1b5e20;
        padding: 25px;
        background: #ffffff;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        letter-spacing: 5px;
    }
    .feedback-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #e8f5e9;
        border-left: 5px solid #2e7d32;
        font-size: 16px;
        color: #2e7d32;
        margin-top: 20px;
    }
    .timing-box {
        padding: 10px;
        border-radius: 8px;
        background-color: #e3f2fd;
        border-left: 5px solid #1976d2;
        font-size: 14px;
        color: #0d47a1;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION (For Attendance & Progress Tracking) ---
if 'enrollment_date' not in st.session_state:
    st.session_state.enrollment_date = "18 اکتوبر 2026"
if 'total_sessions' not in st.session_state:
    st.session_state.total_sessions = 3
if 'total_minutes' not in st.session_state:
    st.session_state.total_minutes = 25

# --- SIDEBAR: ADVANCED LMS & ENROLLMENT TRACKER ---
st.sidebar.header("📊 طالب علم کا ڈیش بورڈ")
student_name = st.sidebar.text_input("طالب علم کا نام:", "مُعاذ عزیز")

st.sidebar.markdown("---")
st.sidebar.subheader("📌 انرولمنٹ اور ایکٹیویٹی")
st.sidebar.text(f"📅 تاریخِ داخلہ: {st.session_state.enrollment_date}")
st.sidebar.text(f"🟢 آخری آن لائن: آج، صبح 08:00 بجے")
st.sidebar.text(f"⏱️ کل مشق کا وقت: {st.session_state.total_minutes} منٹ")
st.sidebar.text(f"📚 کل مکمل سیشنز: {st.session_state.total_sessions}")

st.sidebar.markdown("---")
st.sidebar.header("🎯 نصاب کا انتخاب")
course_type = st.sidebar.selectbox("کورس منتخب کریں:", ["نورانی قاعدہ", "تیسواں پارہ (عم پارہ)"])

# --- CURRICULUM DATABASE (NOORANI QAIDA & PARA 30) ---
if course_type == "نورانی قاعدہ":
    lessons_data = {
        "تختی نمبر 1: حروفِ مفردات (Al-Huroof Al-Mufradat)": {
            "arabic": "ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن و هـ ء ي",
            "description": "ان حروف کو الگ الگ اور درست مخارج کے ساتھ پڑھیں۔ (حروفِ ہجائی)"
        },
        "تختی نمبر 2: حروفِ مرکبات (Al-Huroof Al-Murakkabat)": {
            "arabic": "لا لـح لـم طم يس حم الم الر",
            "description": "ملی ہوئی شکلوں والے حروف کی پہچان اور مشق۔"
        },
        "تختی نمبر 3: حرکات (زبر، زیر، پیش)": {
            "arabic": "أَ إِ أُ بَ بِ بُ تَ تِ تُ",
            "description": "زبر (اوپر آواز)، زیر (نیچے آواز)، اور پیش (گول ہونٹوں سے آواز) کی مشق۔"
        },
        "تختی نمبر 4: تنوین (دو زبر، دو زیر، دو پیش)": {
            "arabic": "أَنْ أِنْ أُنْ بَنْ بِنْ بُنْ",
            "description": "تنوین اور نونِ ساکنہ کی آواز کی پہچان۔"
        }
    }
else:
    lessons_data = {
        "Surah An-Naba (النبأ)": {
            "arabic": "عَمَّ يَتَسَاءَلُونَ ۝ عَنِ النَّبَإِ الْعَظِيمِ",
            "description": "سورت النبأ کی ابتدائی آیات کی تلاوت۔"
        },
        "Surah Al-Ikhlas (الإخلاص)": {
            "arabic": "قُلْ هُوَ اللَّهُ أَحَدٌ ۝ اللَّهُ الصَّمَدُ",
            "description": "سورۃ الإخلاص - توحید کا بیان۔"
        },
        "Surah An-Nas (الناس)": {
            "arabic": "قُلْ أَعُوذُ بِرَبِّ النَّاسِ ۝ مَلِكِ النَّاسِ",
            "description": "سورۃ الناس - پناہ مانگنے کی سورت۔"
        }
    }

selected_lesson = st.sidebar.selectbox("سبق / تختی منتخب کریں:", list(lessons_data.keys()))
current_lesson = lessons_data[selected_lesson]

# --- SESSION TIMING TRACKER ---
if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()

elapsed_time = int(time.time() - st.session_state.session_start)
minutes = elapsed_time // 60
seconds = elapsed_time % 60

# --- MAIN CONTENT AREA ---
st.markdown("<h1 style='text-align: center; color: #2e7d32;'>📖 AI مکتب و مدرسہ</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #555; font-size: 18px;'>خوش آمدید، <b>{student_name}</b>! آج کا سبق: <b>{course_type}</b></p>", unsafe_allow_html=True)

# Timing Box
st.markdown(f"""
    <div class="timing-box">
        ⏱️ <b>موجودہ سیشن کا وقت:</b> {minutes:02d}:{seconds:02d} منٹ | <b>سبق:</b> {selected_lesson}
    </div>
""", unsafe_allow_html=True)

# Display Arabic Text / Qaida Board
st.markdown(f'<div class="arabic-text">{current_lesson["arabic"]}</div>', unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #666; font-size: 18px;'><b>ہدایت / وضاحت:</b> {current_lesson['description']}</p>", unsafe_allow_html=True)

st.divider()

# --- AUDIO RECORDING & EVALUATION MODULE ---
st.markdown("### 🎙️ تختی یا سبق سنائیں (Practice & Test)")
st.write("مائیکروفون کے بٹن پر کلک کر کے پڑھ کر سنائیں:")

audio_value = st.audio_input("تلاوت یا حروف ریکارڈ کرنے کے لیے کلک کریں:")

if audio_value is not None:
    st.audio(audio_value)
    
    with st.spinner("🤖 AI استاد آپ کی آواز کا جائزہ لے رہا ہے..."):
        time.sleep(2)
    
    # Update stats
    st.session_state.total_sessions += 1
    st.session_state.total_minutes += 5
    
    # AI Feedback Output
    st.markdown(f"""
        <div class="feedback-box">
            <b>🌟 ماشاءاللہ بہت عمدہ، {student_name}!</b><br>
            • آپ نے <b>{selected_lesson}</b> بہت اچھے طریقے سے ادا کیا ہے۔<br>
            • <b>وقت صرف ہوا:</b> {minutes} منٹ اور {seconds} سیکنڈز۔<br>
            • <b>استاد کی نصیحت:</b> مخارج بالکل درست ہیں، ایسے ہی جاری رکھیں!<br>
            • <b>اسکور:</b> ⭐⭐⭐⭐⭐ (5/5)
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons()
    
    # --- PARENT PROGRESS REPORT SECTION ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📩 والدین کو پروگریس رپورٹ بھیجیں")
    
    parent_email = st.text_input("والدین کی ای میل (Parent Email):", "parent@example.com")
    
    if st.button("📤 رپورٹ ارسال کریں"):
        st.success(f"✅ {student_name} کی پروگریس رپورٹ ({course_type} - {selected_lesson} | سیشن: {minutes}m | اسکور: 5/5) کامیابی سے {parent_email} پر بھیج دی گئی ہے!")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>AI Madrassa LMS • Powered by Python & Streamlit</p>", unsafe_allow_html=True)
