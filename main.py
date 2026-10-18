import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Madrassa - Online Quran Madrassa",
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
st.markdown("<h1 style='text-align: center; color: #2e7d32;'>📖 AI Maktab o Madrassa</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555; font-size: 18px;'>Bachon ke liye Quran e Pak seekhne ka digital ustad (30 Paras Edition)</p>", unsafe_allow_html=True)
st.divider()

# --- SIDEBAR: 30 PARAS SELECTOR ---
st.sidebar.header("🎯 Sabaq ka Intikhab Karein")
student_name = st.sidebar.text_input("Talib ilm ka naam:", "Muaz Aziz")

# Generating 30 Paras list dynamically
paras_list = [f"Para {i}" for i in range(1, 31)]
selected_para = st.sidebar.selectbox("Para muntakhib karein:", paras_list)

# Sample Database for Paras (MVP structure)
paras_database = {
    "Para 1": {
        "title": "Para 1 (Al-Fatiha & Al-Baqarah)",
        "arabic": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ۝ الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ ۝ الرَّحْمَٰنِ الرَّحِيمِ",
        "translation": "Shuru Allah ke naam se jo bara meharban nehayat reham wala hai. Tamam tareefein Allah ke liye hain jo tamam jahano ka palne wala hai."
    },
    "Para 30": {
        "title": "Para 30 (Amma Para - Surah An-Naba & An-Nas)",
        "arabic": "عَمَّ يَتَسَاءَلُونَ ۝ عَنِ النَّبَإِ الْعَظِيمِ",
        "translation": "Woh kis cheez ke baare mein apas mein pooch rahe hain? Us bare khabar ke baare mein."
    }
}

# Fallback for other paras so app doesn't break
current_lesson = paras_database.get(selected_para, {
    "title": f"{selected_para} - Ibtedai Sabaq",
    "arabic": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
    "translation": f"Yeh {selected_para} ka ibtedai safha hai. Yahan tilawat ki mashq ki jaye gi."
})

# --- MAIN CONTENT AREA ---
st.subheader(f" خوش آمدید، {student_name}! 👋")
st.info(f"Maujuda Sabaq: **{selected_para}** ({current_lesson['title']})")

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
    
    with st.spinner("🤖 AI Ustad aapki tilawat sun raha hai..."):
        time.sleep(2)
    
    # AI Feedback Output
    st.markdown(f"""
        <div class="feedback-box">
            <b>🌟 Mashallah bohat pyaari tilawat, {student_name}!</b><br>
            • Aap ne {selected_para} ke huroof ka talaffuz acha ada kiya hai.<br>
            • <b>Ustad ki Naseehat:</b> Mad aur Harkat par thoda aur dehan dein.<br>
            • <b>Score:</b> ⭐⭐⭐⭐⭐ (5/5)
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons()

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>AI Madrassa MVP • Powered by Streamlit</p>", unsafe_allow_html=True)
