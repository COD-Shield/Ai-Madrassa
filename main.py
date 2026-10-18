import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Maktab - اے آئی مکتب",
    page_icon="📖",
    layout="wide",
)

# Custom CSS for Premium & Attractive Islamic Theme
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');

        /* Main App Background - Rich Deep Emerald Gradient */
        .stApp {
            background: linear-gradient(135deg, #051c13 0%, #0c3826 100%);
            color: #ffffff;
            font-family: 'Noto Nastaliq Urdu', serif;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #2c0e35;
            color: white;
            border-right: 1px solid rgba(212, 175, 55, 0.2);
        }

        /* Header Box with Premium Gold Border & Glow */
        .header-box {
            text-align: center;
            background: rgba(11, 48, 33, 0.85);
            border: 2px solid #d4af37;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(212, 175, 55, 0.15);
            backdrop-filter: blur(10px);
        }

        .taawwudh-bismillah {
            font-family: 'Amiri', serif;
            font-size: 2.2rem;
            color: #f3c653;
            line-height: 1.9;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.7);
            letter-spacing: 1px;
        }

        /* Instructions Box */
        .custom-info {
            background: rgba(8, 34, 24, 0.9);
            border-right: 5px solid #d4af37;
            border-top: 1px solid rgba(212, 175, 55, 0.3);
            border-bottom: 1px solid rgba(212, 175, 55, 0.3);
            border-left: 1px solid rgba(212, 175, 55, 0.3);
            padding: 15px 20px;
            border-radius: 10px;
            font-size: 1.1rem;
            color: #e2e8f0;
            margin-bottom: 25px;
            direction: rtl;
            text-align: right;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }

        /* Word-by-Word Animation */
        @keyframes fadeInWord {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .animated-word {
            display: inline-block;
            animation: fadeInWord 0.4s ease forwards;
            margin: 0 4px;
            color: #ffffff;
            font-weight: bold;
        }

        .teacher-message-box {
            background: rgba(7, 30, 21, 0.95);
            border: 1px solid #d4af37;
            border-radius: 15px;
            padding: 20px;
            font-size: 1.3rem;
            direction: rtl;
            text-align: right;
            margin-bottom: 30px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        }
        
        /* Alphabet Cards Styling with Hover Effect */
        .alphabet-card {
            background: linear-gradient(145deg, #0e3b29, #09271c);
            border: 2px solid #d4af37;
            border-radius: 15px;
            padding: 25px 15px;
            text-align: center;
            box-shadow: 0 6px 18px rgba(0,0,0,0.4);
            transition: all 0.3s ease;
        }

        .alphabet-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(212, 175, 55, 0.3);
            border-color: #f3c653;
        }

        /* Section Title Styling */
        .section-title {
            color: #f3c653;
            font-size: 1.5rem;
            margin-bottom: 20px;
            border-bottom: 1px dashed rgba(212, 175, 55, 0.4);
            padding-bottom: 10px;
            direction: rtl;
            text-align: right;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Menu
st.sidebar.markdown(
    "<h2 style='color: #f3c653; font-family: Amiri;'>⚡ AI Maktab</h2>",
    unsafe_allow_html=True,
)
menu = st.sidebar.radio(
    "", ["📁 Scenarios", "🤖 AI Agents", "📊 Credentials", "🌐 Webhooks"]
)

# Header Section with Complete Taawwudh and Bismillah
st.markdown(
    """
    <div class="header-box">
        <div class="taawwudh-bismillah">
            أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ<br>
            بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# Instructions Banner (RTL Fixed)
st.markdown(
    """
    <div class="custom-info">
        <strong>ہدایات:</strong> دائیں طرف سے پڑھنا شروع کریں۔ کسی بھی حرف کے نیچے دیے گئے تلفظ سنیں بٹن پر کلک کریں تاکہ AI استاد آپ کو درست تلفظ بتائے۔
    </div>
""",
    unsafe_allow_html=True,
)

# Dynamic Teacher Message with Correct RTL Ordering & Word-by-Word Effect
teacher_text = "استاد کا پیغام: حرف (Ba) کا مخرج بالکل درست ادا کیا گیا۔ ماشاءاللہ!"
words = teacher_text.split()

animated_html = '<div class="teacher-message-box">🎙️ <span style="color: #f3c653;">استاد کا ماڈیول:</span> '
for i, word in enumerate(words):
    animated_html += f'<span class="animated-word" style="animation-delay: {i * 0.12}s;">{word}</span> '
animated_html += "</div>"

st.markdown(animated_html, unsafe_allow_html=True)

# Arabic Alphabet Cards Layout
st.markdown(
    '<div class="section-title">حروف تہجی کی مشق (Arabic Alphabets Practice)</div>',
    unsafe_allow_html=True,
)

col1, col2, col3, col4, col5 = st.columns(5)

with col5:
    st.markdown(
        """
        <div class="alphabet-card">
            <h1 style="color: #f3c653; font-family: Amiri; font-size: 3rem; margin:0;">ا</h1>
            <p style="color: #cbd5e1; margin:8px 0 0 0; font-family: sans-serif; font-weight: bold;">Alif</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ا", key="btn_alif", use_container_width=True)

with col4:
    st.markdown(
        """
        <div class="alphabet-card">
            <h1 style="color: #f3c653; font-family: Amiri; font-size: 3rem; margin:0;">ب</h1>
            <p style="color: #cbd5e1; margin:8px 0 0 0; font-family: sans-serif; font-weight: bold;">Ba</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ب", key="btn_ba", use_container_width=True)

with col3:
    st.markdown(
        """
        <div class="alphabet-card">
            <h1 style="color: #f3c653; font-family: Amiri; font-size: 3rem; margin:0;">ت</h1>
            <p style="color: #cbd5e1; margin:8px 0 0 0; font-family: sans-serif; font-weight: bold;">Ta</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ت", key="btn_ta", use_container_width=True)

with col2:
    st.markdown(
        """
        <div class="alphabet-card">
            <h1 style="color: #f3c653; font-family: Amiri; font-size: 3rem; margin:0;">ث</h1>
            <p style="color: #cbd5e1; margin:8px 0 0 0; font-family: sans-serif; font-weight: bold;">Tha</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ث", key="btn_tha", use_container_width=True)

with col1:
    st.markdown(
        """
        <div class="alphabet-card">
            <h1 style="color: #f3c653; font-family: Amiri; font-size: 3rem; margin:0;">ج</h1>
            <p style="color: #cbd5e1; margin:8px 0 0 0; font-family: sans-serif; font-weight: bold;">Jeem</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ج", key="btn_jeem", use_container_width=True)
