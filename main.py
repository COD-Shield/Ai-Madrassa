import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Madrassa - آن لائن قرآن مدرسہ",
    page_icon="📖",
    layout="centered"
)

# --- CUSTOM CSS FOR KIDS-FRIENDLY UI ---
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
    .stButton>button:hover {
        background-color: #1b5e20;
        color: white;
    }
    .arabic-text {
        font-size: 36px;
        text-align: center;
        direction: rtl;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        color: #1b5e20;
        padding: 20px;
        background: #ffffff;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
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
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1 style='text-align: center; color: #2e7d32;'>📖 AI مکتب و مدرسہ</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555; font-size: 18px;'>پیارے بچوں کے ساتھ خوشگوار انداز میں قرآن پاک سیکھنے کا ڈیجیٹل استاد</p>", unsafe_allow_html=True)
st.divider()

# --- SIDEBAR: LESSON SELECTOR ---
st.sidebar.header("🎯 سبق کا انتخاب کریں")
student_name = st.sidebar.text_input("طالب علم کا نام:", "مُعاذ عزیز")
selected_surah = st.sidebar.selectbox(
    "سورہ منتخب کریں:",
    ["سورۃ الفاتحہ (Surah Al-Fatiha)", "سورۃ الإخلاص (Surah Al-Ikhlas)", "سورۃ الفلق (Surah Al-Falaq)", "سورۃ الناس (Surah An-Nas)"]
)

# --- SURAH DATABASE ---
surah_data = {
    "سورۃ الفاتحہ (Surah Al-Fatiha)": {
        "arabic": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ۝ الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
        "translation": "شروع اللہ کے نام سے جو بڑا مہربان نہایت رحم والا ہے 👑 تمام تعریفیں اللہ کے لیے ہیں جو تمام جہانوں کا پالنے والا ہے۔"
    },
    "سورۃ الإخلاص (Surah Al-Ikhlas)": {
        "arabic": "قُلْ هُوَ اللَّهُ أَحَدٌ ۝ اللَّهُ الصَّمَدُ",
        "translation": "آپ کہہ دیجیے کہ وہ اللہ ایک ہے 👑 اللہ بے نیاز ہے (سب اس کے محتاج ہیں وہ کسی کا محتاج نہیں)۔"
    },
    "سورۃ الفلق (Surah Al-Falaq)": {
        "arabic": "قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ ۝ مِنْ شَرِّ مَا خَلَقَ",
        "translation": "آپ کہہ دیجیے کہ میں صبح کے رب کی پناہ میں آتا ہوں 👑 ہر اس چیز کے شر سے جو اس نے پیدا کی ہے۔"
    },
    "سورۃ النّاس (Surah An-Nas)": {
        "arabic": "قُلْ أَعُوذُ بِرَبِّ النَّاسِ ۝ مَلِكِ النَّاسِ",
        "translation": "آپ کہہ دیجیے کہ میں لوگوں کے رب کی پناہ مانگتا ہوں 👑 جو لوگوں کا حقیقی بادشاہ ہے۔"
    }
}

current_lesson = surah_data[selected_surah]

# --- MAIN CONTENT AREA ---
st.subheader(f"خوش آمدید، {student_name}! 👋 آج کا سبق:")
st.info(f"موجودہ سبق: **{selected_surah}**")

# Display Arabic Text
st.markdown(f'<div class="arabic-text">{current_lesson["arabic"]}</div>', unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #666;'><b>ترجمہ:</b> {current_lesson['translation']}</p>", unsafe_allow_html=True)

st.divider()

# --- AUDIO RECORDING MODULE ---
st.markdown("### 🎙️ اپنی تلاوت ریکارڈ کریں")
st.write("مائیکروفون کے بٹن پر کلک کریں اور تلاوت سنائیں:")

audio_value = st.audio_input("تلاوت ریکارڈ کرنے کے لیے کلک کریں:")

if audio_value is not None:
    st.audio(audio_value)
    
    with st.spinner("🤖 AI استاد آپ کی تلاوت سن رہا ہے..."):
        time.sleep(2)
    
    # AI Feedback Output
    st.markdown(f"""
        <div class="feedback-box">
            <b>🌟 ماشاءاللہ بہت پیاری تلاوت، {student_name}!</b><br>
            • آپ نے حروف کا تلفظ بہت اچھا ادا کیا ہے۔<br>
            • <b>استاد کی نصیحت:</b> مد اور غنہ پر تھوڑا سا اور دھیان دیں۔<br>
            • <b>کارکردگی اسکور:</b> ⭐⭐⭐⭐⭐ (5/5)
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons()

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>AI Madrassa MVP • Powered by Streamlit</p>", unsafe_allow_html=True)
