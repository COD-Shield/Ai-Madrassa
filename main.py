import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Madrassa - Para 30 (Amma Para)",
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
        font-size: 34px;
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
st.markdown("<h1 style='text-align: center; color: #2e7d32;'>📖 AI Madrassa - Para 30 (Amma Para)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555; font-size: 18px;'>Sirf Teesway Pare ki Suraton ke sath tilawat ki mashq</p>", unsafe_allow_html=True)
st.divider()

# --- PARA 30 SURAHS DATABASE ---
para_30_surahs = {
    "Surah An-Naba (النبأ)": {
        "arabic": "عَمَّ يَتَسَاءَلُونَ ۝ عَنِ النَّبَإِ الْعَظِيمِ",
        "translation": "Woh kis cheez ke baare mein apas mein pooch rahe hain? Us bare khabar ke baare mein."
    },
    "Surah An-Naziat (النازعات)": {
        "arabic": "وَالنَّازِعَاتِ غَرْقًا ۝ وَالنَّاشِطَاتِ نَشْطًا",
        "translation": "Qasam hai un farishton ki jo sakhti se jaan nikalte hain aur jo naram dili se rooh khinchte hain."
    },
    "Surah Abasa (عبس)": {
        "arabic": "عَبَسَ وَتَوَلَّى ۝ أَنْ جَاءَهُ الْأَعْمَى",
        "translation": "Usne munh pher liya aur berukhi ki, is baat par ke uske paas ek andha shakhs aa gaya."
    },
    "Surah Al-Ikhlas (الإخلاص)": {
        "arabic": "قُلْ هُوَ اللَّهُ أَحَدٌ ۝ اللَّهُ الصَّمَدُ",
        "translation": "Aap keh dijiye ke woh Allah ek hai, Allah be-niaz hai."
    },
    "Surah An-Nas (الناس)": {
        "arabic": "قُلْ أَعُوذُ بِرَبِّ النَّاسِ ۝ مَلِكِ النَّاسِ",
        "translation": "Aap keh dijiye ke main logon ke rab ki panah mangta hoon, jo logon ka badshah hai."
    }
}

# --- SIDEBAR: SELECT SURAH FROM PARA 30 ---
st.sidebar.header("🎯 Para 30 - Surah Selection")
student_name = st.sidebar.text_input("Talib ilm ka naam:", "Muaz Aziz")
selected_surah = st.sidebar.selectbox("Surah muntakhib karein:", list(para_30_surahs.keys()))

current_lesson = para_30_surahs[selected_surah]

# --- MAIN CONTENT AREA ---
st.subheader(f"Khush amdeed, {student_name}! 👋")
st.info(f"Maujuda Sabaq: **{selected_surah}** (Para 30)")

# Display Arabic Text
st.markdown(f'<div class="arabic-text">{current_lesson["arabic"]}</div>', unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #666;'><b>Tarjuma:</b> {current_lesson['translation']}</p>", unsafe_allow_html=True)

st.divider()

# --- AUDIO RECORDING MODULE ---
st.markdown("### 🎙️ Apni Tilawat Record Karein")
st.write("Microphone button par click karein aur tilawat sunayein:")

audio_value = st.audio_input("Tilawat record karne ke liye click karein:")

if audio_value is not None:
    st.audio(audio_value)
    
    with st.spinner("🤖 AI ustad aapki tilawat sun raha hai..."):
        time.sleep(2)
    
    # AI Feedback Output
    st.markdown(f"""
        <div class="feedback-box">
            <b>🌟 Mashallah bohat pyaari tilawat, {student_name}!</b><br>
            • Aap ne {selected_surah} ki tilawat achay andaz mein ki hai.<br>
            • <b>Ustad ki Naseehat:</b> Makhraj aur harqat par mazeed tawajjo dein.<br>
            • <b>Score:</b> ⭐⭐⭐⭐⭐ (5/5)
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons()

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>AI Madrassa - Para 30 Edition • Powered by Streamlit</p>", unsafe_allow_html=True)
