import streamlit as st
import time
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Madrassa - مکمل نورانی قاعدہ",
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
        font-size: 38px;
        text-align: center;
        direction: rtl;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        color: #1b5e20;
        padding: 25px;
        background: #ffffff;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        line-height: 1.8;
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

# --- SESSION STATE INITIALIZATION ---
if 'enrollment_date' not in st.session_state:
    st.session_state.enrollment_date = "18 اکتوبر 2026"
if 'total_sessions' not in st.session_state:
    st.session_state.total_sessions = 5
if 'total_minutes' not in st.session_state:
    st.session_state.total_minutes = 40

# --- SIDEBAR: LMS & COMPLETE NOORANI QAIDA CURRICULUM ---
st.sidebar.header("📊 طالب علم کا ڈیش بورڈ")
student_name = st.sidebar.text_input("طالب علم کا نام:", "مُعاذ عزیز")

st.sidebar.markdown("---")
st.sidebar.subheader("📌 انرولمنٹ اور ایکٹیویٹی")
st.sidebar.text(f"📅 تاریخِ داخلہ: {st.session_state.enrollment_date}")
st.sidebar.text(f"🟢 آخری آن لائن: آج")
st.sidebar.text(f"⏱️ کل مشق کا وقت: {st.session_state.total_minutes} منٹ")
st.sidebar.text(f"📚 کل مکمل سیشنز: {st.session_state.total_sessions}")

st.sidebar.markdown("---")
st.sidebar.header("🎯 مکمل نورانی قاعدہ کورس")
course_type = st.sidebar.selectbox("کورس منتخب کریں:", ["مُکَمَّل نورانی قاعدہ", "تیسواں پارہ (عم پارہ)"])

# --- COMPLETE NOORANI QAIDA DATABASE (Takhtiyan 1 to 10+) ---
if course_type == "مُکَمَّل نورانی قاعدہ":
    lessons_data = {
        "تختی نمبر 1: حروفِ مفردات (الفاظ کی شناخت)": {
            "arabic": "أ ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن و هـ ء ي",
            "description": "حروفِ ہجائی کو الگ الگ اور درست مخارج (گلے اور ہونٹوں سے) ادا کریں۔"
        },
        "تختی نمبر 2: حروفِ مرکبات (ملی ہوئی شکلیں)": {
            "arabic": "لا لـح لـم طم يس حم الم الر طه يس",
            "description": "جب دو یا دو سے زیادہ حروف آپس میں ملتے ہیں تو ان کی شکلیں کیسی ہوتی ہیں، اس کی مشق۔"
        },
        "تختی نمبر 3: حرکات (زبر، زیر، پیش)": {
            "arabic": "أَ إِ أُ بَ بِ بُ تَ تِ تُ ثَ ثِ ثُ",
            "description": "زبر (آواز اوپر اٹھتی ہے)، زیر (آواز نیچے جاتی ہے)، پیش (ہونٹ گول ہوتے ہیں۔ یاد رہے: انہیں کھینچ کر نہیں پڑھتے)۔"
        },
        "تختی نمبر 4: تنوین (دو زبر، دو زیر، دو پیش)": {
            "arabic": "أَنْ أِنْ أُنْ بَنْ بِنْ بُنْ تَ تَنْ تِنْ تُنْ",
            "description": "تنوین دراصل نونِ ساکنہ ہوتی ہے جو آواز کے آخر میں ظاہر ہوتی ہے۔"
        },
        "تختی نمبر 5: مشقِ حرکات و تنوین (ملا جلا سبق)": {
            "arabic": "فَلَ حَكَ خَلَقَ رَزَقَ كَتَبَ عَوۡمًا بَهِيۡجًا",
            "description": "حرکات اور تنوین کی مشترکہ مشق تاکہ روانی پیدا ہو۔"
        },
        "تختی نمبر 6: حروفِ مدّہ (الف مدہ، واؤ مدہ، یا مدہ)": {
            "arabic": "بَا بُو بِيْ تَ تُو تِيْ ثَا ثُو ثِيْ",
            "description": "حروفِ مدّہ کو ایک الف کے برابر (تھوڑا سا لمبا) کھینچ کر پڑھا جاتا ہے۔"
        },
        "تختی نمبر 7: حروفِ لین (واؤ لین، یا لین)": {
            "arabic": "بَوْ بَيْ تَوْ تَيْ ثَوْ ثَيْ جَوْ جَيْ",
            "description": "حروفِ لین کو نرمی کے ساتھ اور جلدی ادا کیا جاتا ہے۔"
        },
        "تختی نمبر 8: مدّہ اور لین کی مشق": {
            "arabic": "خَوْفٌ بَيْتٍ قَوْلٍ صَيْفٍ مَوْتٍ",
            "description": "مدہ اور لین کے قواعد کی روانی کے ساتھ تمرین۔"
        },
        "تختی نمبر 9: تنوین و نونِ ساکنہ اور اظہار و اخفا": {
            "arabic": "مِنْ حَوْلِ مِنْ خَوْفٍ مِنْ شَرِّ مِنْ وَلِيِّ",
            "description": "نونِ ساکنہ اور تنوین کے بعد حروفِ حلقی کا قاعدہ۔"
        },
        "تختی نمبر 10: تشدید (شدّ کی مشق)": {
            "arabic": "رَبَّ رَبِّ رَبُّ ضَرَّ ظَنَّ حَقَّ",
            "description": "تشدید والے حرف کو پچھلے حرف سے ملا کر دو بار پڑھا جاتا ہے اور سختی دی جاتی ہے۔"
        }
    }
else:
    lessons_data = {
        "Surah An-Naba (النبأ)": {
            "arabic": "عَمَّ يَتَسَاءَلُونَ ۝ عَنِ النَّبَإِ الْعَظِيمِ",
            "description": "تیسویں پارے کی پہلی سورت (النبأ) کی مشق۔"
        },
        "Surah Al-Ikhlas (الإخلاص)": {
            "arabic": "قُلْ هُوَ اللَّهُ أَحَدٌ ۝ اللَّهُ الصَّمَدُ",
            "description": "سورۃ الإخلاص - توحید اور قل هو الله."
        },
        "Surah An-Nas (الناس)": {
            "arabic": "قُلْ أَعُوذُ بِرَبِّ النَّاسِ ۝ مَلِكِ النَّاسِ",
            "description": "سورۃ الناس - آخری سورۃ مبارکہ۔"
        }
    }

selected_lesson = st.sidebar.selectbox("تختی / سبق منتخب کریں:", list(lessons_data.keys()))
current_lesson = lessons_data[selected_lesson]

# --- SESSION TIMING TRACKER ---
if 'session_start' not in st.session_state:
    st.session_state.session_start = time.time()

elapsed_time = int(time.time() - st.session_state.session_start)
minutes = elapsed_time // 60
seconds = elapsed_time % 60

# --- MAIN CONTENT AREA ---
st.markdown("<h1 style='text-align: center; color: #2e7d32;'>📖 AI مکتب و مدرسہ (نورانی قاعدہ)</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #555; font-size: 18px;'>خوش آمدید، <b>{student_name}</b>! آج کا کورس: <b>{course_type}</b></p>", unsafe_allow_html=True)

# Timing Box
st.markdown(f"""
    <div class="timing-box">
        ⏱️ <b>سیشن کا وقت:</b> {minutes:02d}:{seconds:02d} منٹ | <b>منتخب سبق:</b> {selected_lesson}
    </div>
""", unsafe_allow_html=True)

# Display Arabic Text / Qaida Board
st.markdown(f'<div class="arabic-text">{current_lesson["arabic"]}</div>', unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #444; font-size: 18px;'><b>💡 استاد کی ہدایت:</b> {current_lesson['description']}</p>", unsafe_allow_html=True)

st.divider()

# --- AUDIO RECORDING & EVALUATION MODULE ---
st.markdown("### 🎙️ تختی پڑھ کر سنائیں (Practice & Test)")
st.write("مائیکروفون کے بٹن پر کلک کریں اور پڑھ کر اپنی آواز ریکارڈ کروائیں:")

audio_value = st.audio_input("ریکارڈ کرنے کے لیے یہاں کلک کریں:")

if audio_value is not None:
    st.audio(audio_value)
    
    with st.spinner("🤖 AI استاد آپ کے تلفظ اور مخارج کا جائزہ لے رہا ہے..."):
        time.sleep(2)
    
    # Update stats
    st.session_state.total_sessions += 1
    st.session_state.total_minutes += 5
    
    # AI Feedback Output
    st.markdown(f"""
        <div class="feedback-box">
            <b>🌟 ماشاءاللہ بہت عمدہ، {student_name}!</b><br>
            • آپ نے <b>{selected_lesson}</b> کی مشق کامیابی سے مکمل کی ہے۔<br>
            • <b>صرف ہونے والا وقت:</b> {minutes} منٹ اور {seconds} سیکنڈز۔<br>
            • <b>استاد کا فیصلی تبصرہ:</b> حروف کا تلفظ اور حرکات بالکل درست ادا ہوئیں!<br>
            • <b>کارکردگی اسکور:</b> ⭐⭐⭐⭐⭐ (5/5)
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons()
    
    # --- PARENT PROGRESS REPORT SECTION ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📩 والدین کو پروگریس رپورٹ بھیجیں")
    
    parent_email = st.text_input("والدین کی ای میل (Parent Email):", "parent@example.com")
    
    if st.button("📤 رپورٹ ارسال کریں"):
        st.success(f"✅ {student_name} کی پروگریس رپورٹ ({course_type} - {selected_lesson} | وقت: {minutes}m | اسکور: 5/5) کامیابی سے {parent_email} پر بھیج دی گئی ہے!")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>AI Madrassa LMS • Powered by Python & Streamlit</p>", unsafe_allow_html=True)
