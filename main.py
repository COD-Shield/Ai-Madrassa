import time
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Maktab - نورانی قاعدہ",
    page_icon="📖",
    layout="wide",
)

# Custom CSS for Premium Islamic Theme & RTL Support
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');

        .stApp {
            background: linear-gradient(135deg, #051c13 0%, #0c3826 100%);
            color: #ffffff;
            font-family: 'Noto Nastaliq Urdu', serif;
        }

        [data-testid="stSidebar"] {
            background-color: #2c0e35;
            color: white;
            border-right: 1px solid rgba(212, 175, 55, 0.2);
        }

        .header-box {
            text-align: center;
            background: rgba(11, 48, 33, 0.85);
            border: 2px solid #d4af37;
            border-radius: 20px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
        }

        .taawwudh-bismillah {
            font-family: 'Amiri', serif;
            font-size: 2rem;
            color: #f3c653;
            line-height: 1.8;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.7);
        }

        .custom-info {
            background: rgba(8, 34, 24, 0.9);
            border-right: 5px solid #d4af37;
            padding: 15px 20px;
            border-radius: 10px;
            font-size: 1.1rem;
            color: #e2e8f0;
            margin-bottom: 20px;
            direction: rtl;
            text-align: right;
        }

        .teacher-message-box {
            background: rgba(7, 30, 21, 0.95);
            border: 1px solid #d4af37;
            border-radius: 15px;
            padding: 15px;
            font-size: 1.2rem;
            direction: rtl;
            text-align: right;
            margin-bottom: 25px;
        }
        
        .alphabet-card {
            background: linear-gradient(145deg, #0e3b29, #09271c);
            border: 2px solid #d4af37;
            border-radius: 15px;
            padding: 20px 10px;
            text-align: center;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.4);
            transition: all 0.3s ease;
        }

        .alphabet-card:hover {
            transform: translateY(-5px);
            border-color: #f3c653;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.markdown(
    "<h2 style='color: #f3c653; font-family: Amiri;'>⚡ AI Maktab</h2>",
    unsafe_allow_html=True,
)
main_menu = st.sidebar.radio(
    "مینو", ["📖 نورانی قاعدہ کورس", "🤖 AI Agents", "📊 Credentials", "🌐 Webhooks"]
)

if main_menu == "📖 نورانی قاعدہ کورس":
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

    # Takhti Selection Dropdown (ساری تختیاں ایک ایک کر کے)
    selected_takhti = st.selectbox(
        "نورانی قاعدہ کی تختی منتخب کریں:",
        [
            "تختی نمبر 1: حروف مفردات (ا، ب، ت...)",
            "تختی نمبر 2: حروف مرکبات (ملے ہوئے حروف)",
            "تختی نمبر 3: حروف مقطعات",
            "تختی نمبر 4: حرکات (زبر، زیر، پیش)",
            "تختی نمبر 5: تنوین",
        ],
    )

    if selected_takhti == "تختی نمبر 1: حروف مفردات (ا، ب، ت...)":
        st.markdown(
            """
            <div class="custom-info">
                <strong>تختی نمبر 1 - ہدایات:</strong> حروف مفردات بنیاد ہیں۔ دائیں سے پڑھنا شروع کریں اور حروف کے مخارج اور نقطے اچھے سے یاد کروائیں۔
            </div>
        """,
            unsafe_allow_html=True,
        )

        # Teacher AI Message
        st.markdown(
            '<div class="teacher-message-box">🎙️ <span style="color: #f3c653;">استاد کا پیغام:</span> تختی نمبر 1 شروع ہو چکی ہے۔ حروفِ مفردات کو صاف تلفظ سے ادا کریں۔</div>',
            unsafe_allow_html=True,
        )

        # Row 1 of Alphabets
        col1, col2, col3, col4, col5 = st.columns(5)

        with col5:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; margin:0;">ا</h1><p>Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ا", key="b_alif", use_container_width=True)

        with col4:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; margin:0;">ب</h1><p>Ba</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ب", key="b_ba", use_container_width=True)

        with col3:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; margin:0;">ت</h1><p>Ta</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ت", key="b_ta", use_container_width=True)

        with col2:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; margin:0;">ث</h1><p>Tha</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ث", key="b_tha", use_container_width=True)

        with col1:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; margin:0;">ج</h1><p>Jeem</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ج", key="b_jeem", use_container_width=True)

    elif selected_takhti == "تختی نمبر 2: حروف مرکبات (ملے ہوئے حروف)":
        st.markdown(
            """
            <div class="custom-info">
                <strong>تختی نمبر 2 - ہدایات:</strong> مرکب حروف کو ایک ایک کر کے پہچانیں۔ ملی ہوئی حالت میں حروف کی شکل بدل جاتی ہے[cite: 6].
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="teacher-message-box">🎙️ <span style="color: #f3c653;">استاد کا پیغام:</span> مرکبات کی مشق شروع ہو چکی ہے۔ غور کریں کہ جڑنے کے بعد حروف کیسے لکھے جاتے ہیں۔</div>',
            unsafe_allow_html=True,
        )

        # Example Murakkabat display (e.g. لا , با , يا)
        col1, col2, col3, col4 = st.columns(4)
        with col4:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; margin:0;">لا</h1><p>Lam-Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 لا", key="m_la", use_container_width=True)
        with col3:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; margin:0;">با</h1><p>Ba-Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 با", key="m_ba", use_container_width=True)
        with col2:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; margin:0;">تا</h1><p>Ta-Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 تا", key="m_ta", use_container_width=True)
        with col1:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; margin:0;">ثا</h1><p>Tha-Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ثا", key="m_tha", use_container_width=True)

    else:
        st.info(
            "اس تختی کا ڈیٹا لوڈ ہو رہا ہے... اگلی تختی کے الفاظ یہاں جلد شامل کیے جائیں گے۔"
        )

else:
    st.write(f"آپ نے {main_menu} منتخب کیا ہے۔")
