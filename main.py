import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Maktab - اے آئی مکتب",
    page_icon="📖",
    layout="wide",
)

# Custom CSS for Clean Islamic Theme & Beautiful Background
st.markdown(
    """
    <style>
        /* Clean Solid Islamic Deep Green Background */
        .stApp {
            background-color: #0c2e21;
            color: #ffffff;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #4A154B;
            color: white;
        }

        /* Header Box with Gold Border */
        .header-box {
            text-align: center;
            background: #113f2d;
            border: 2px solid #d4af37;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        }

        .taawwudh-bismillah {
            font-family: 'Amiri', serif;
            font-size: 2rem;
            color: #d4af37;
            line-height: 1.8;
            text-shadow: 0 2px 4px rgba(0,0,0,0.6);
        }

        /* Word-by-Word Animation for Teacher Message */
        @keyframes fadeInWord {
            0% { opacity: 0; transform: translateY(8px); }
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
            background: #082218;
            border: 1px solid #d4af37;
            border-radius: 12px;
            padding: 18px;
            font-size: 1.4rem;
            text-align: right;
            margin-bottom: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        
        /* Alphabet Cards Styling */
        .alphabet-card {
            background: #113f2d;
            border: 2px solid #d4af37;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Menu
st.sidebar.markdown("<h2>⚡ AI Maktab</h2>", unsafe_allow_html=True)
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

# Instructions Banner
st.info(
    "ہدایات: دائیں طرف سے پڑھنا شروع کریں۔ کسی بھی حرف کے نیچے دیے گئے تلفظ سنیں بٹن پر کلک کریں تاکہ AI استاد آپ کو درست تلفظ بتائے۔"
)

# Dynamic Teacher Message with Word-by-Word Effect
teacher_text = (
    "مخرج بالکل درست ہے (Ba) استاد کا پیغام: حرف ب Al AI ادا کیا گیا ۔"
)
words = teacher_text.split()

# Generating HTML for Word-by-Word Animation
animated_html = '<div class="teacher-message-box">🎙️ استاد کا پیغام: '
for i, word in enumerate(words):
    animated_html += f'<span class="animated-word" style="animation-delay: {i * 0.15}s;">{word}</span> '
animated_html += "</div>"

st.markdown(animated_html, unsafe_allow_html=True)

# Arabic Alphabet Cards Layout (Right to Left / RTL alignment representation)
st.write("### حروف تہجی کی مشق")
col1, col2, col3, col4, col5 = st.columns(5)

with col5:
    st.markdown(
        """
        <div class="alphabet-card">
            <h1 style="color: #d4af37; margin:0;">ا</h1>
            <p style="margin:5px 0 0 0;">Alif</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ا", key="btn_alif", use_container_width=True)

with col4:
    st.markdown(
        """
        <div class="alphabet-card">
            <h1 style="color: #d4af37; margin:0;">ب</h1>
            <p style="margin:5px 0 0 0;">Ba</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ب", key="btn_ba", use_container_width=True)

with col3:
    st.markdown(
        """
        <div class="alphabet-card">
            <h1 style="color: #d4af37; margin:0;">ت</h1>
            <p style="margin:5px 0 0 0;">Ta</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ت", key="btn_ta", use_container_width=True)

with col2:
    st.markdown(
        """
        <div class="alphabet-card">
            <h1 style="color: #d4af37; margin:0;">ث</h1>
            <p style="margin:5px 0 0 0;">Tha</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ث", key="btn_tha", use_container_width=True)

with col1:
    st.markdown(
        """
        <div class="alphabet-card">
            <h1 style="color: #d4af37; margin:0;">ج</h1>
            <p style="margin:5px 0 0 0;">Jeem</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ج", key="btn_jeem", use_container_width=True)
