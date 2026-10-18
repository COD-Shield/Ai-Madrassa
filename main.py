import time
import streamlit as st

# الصفحة الإعدادات (Page Configuration)
st.set_page_config(
    page_title="AI Maktab - اے آئی مکتب",
    page_icon="📖",
    layout="wide",
)

# Custom CSS for Islamic Theme, Background Pattern, and Word-by-Word Animation
st.markdown(
    """
    <style>
        /* Main Theme Colors & Islamic Geometric Background */
        .stApp {
            background-color: #051c13;
            background-image: radial-gradient(#d4af37 0.75px, transparent 0.75px), radial-gradient(#d4af37 0.75px, #051c13 0.75px);
            background-size: 30px 30px;
            background-position: 0 0, 15px 15px;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #4A154B;
            color: white;
        }

        /* Header Styling with Taawwudh and Bismillah */
        .header-box {
            text-align: center;
            background: rgba(11, 60, 41, 0.9);
            border: 2px solid #d4af37;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
        }

        .taawwudh-bismillah {
            font-family: 'Amiri', serif;
            font-size: 1.8rem;
            color: #d4af37;
            line-height: 1.8;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }

        /* Word-by-Word Animation for Teacher Message */
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
            background: rgba(5, 28, 19, 0.95);
            border: 1px solid #d4af37;
            border-radius: 10px;
            padding: 15px;
            font-size: 1.4rem;
            text-align: right;
            margin-bottom: 20px;
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
    # Adding a slight CSS animation delay for each word sequentially
    animated_html += f'<span class="animated-word" style="animation-delay: {i * 0.15}s;">{word}</span> '
animated_html += "</div>"

st.markdown(animated_html, unsafe_allow_html=True)

# Arabic Alphabet Cards Layout (Right to Left / RTL alignment representation)
st.write("### حروف تہجی کی مشق")
col1, col2, col3, col4, col5 = st.columns(5)

with col5:
    st.markdown(
        """
        <div style="border: 2px solid #d4af37; border-radius: 10px; padding: 20px; text-align: center; background: rgba(11,60,41,0.6);">
            <h1 style="color: #d4af37;">ا</h1>
            <p>Alif</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ا", key="btn_alif")

with col4:
    st.markdown(
        """
        <div style="border: 2px solid #d4af37; border-radius: 10px; padding: 20px; text-align: center; background: rgba(11,60,41,0.6);">
            <h1 style="color: #d4af37;">ب</h1>
            <p>Ba</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ب", key="btn_ba")

with col3:
    st.markdown(
        """
        <div style="border: 2px solid #d4af37; border-radius: 10px; padding: 20px; text-align: center; background: rgba(11,60,41,0.6);">
            <h1 style="color: #d4af37;">ت</h1>
            <p>Ta</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ت", key="btn_ta")

with col2:
    st.markdown(
        """
        <div style="border: 2px solid #d4af37; border-radius: 10px; padding: 20px; text-align: center; background: rgba(11,60,41,0.6);">
            <h1 style="color: #d4af37;">ث</h1>
            <p>Tha</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ث", key="btn_tha")

with col1:
    st.markdown(
        """
        <div style="border: 2px solid #d4af37; border-radius: 10px; padding: 20px; text-align: center; background: rgba(11,60,41,0.6);">
            <h1 style="color: #d4af37;">ج</h1>
            <p>Jeem</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.button("🔊 ج", key="btn_jeem")
