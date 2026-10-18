import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Madrasaa - نورانی قاعدہ",
    page_icon="📖",
    layout="wide",
)

# Custom CSS for Crystal Clear Readability, High Contrast, and Modern Theme
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');

        /* Clean Deep Islamic Green Background */
        .stApp {
            background: #061e14;
            color: #ffffff;
            font-family: 'Noto Nastaliq Urdu', serif;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #113f2d;
            border-right: 2px solid #d4af37;
        }
        
        [data-testid="stSidebar"] * {
            color: #ffffff !important;
            font-size: 1.1rem;
        }

        /* Header Box */
        .header-box {
            text-align: center;
            background: #0b3c29;
            border: 2px solid #d4af37;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
        }

        .taawwudh-bismillah {
            font-family: 'Amiri', serif;
            font-size: 2.3rem;
            color: #f3c653;
            line-height: 1.9;
            text-shadow: 0 2px 5px rgba(0,0,0,0.8);
        }

        /* Clear Readable Instructions Box */
        .custom-info {
            background: #0f3829;
            border-right: 6px solid #f3c653;
            border-top: 1px solid #1e5641;
            border-bottom: 1px solid #1e5641;
            border-left: 1px solid #1e5641;
            padding: 15px 20px;
            border-radius: 10px;
            font-size: 1.2rem;
            color: #ffffff;
            margin-bottom: 20px;
            direction: rtl;
            text-align: right;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }

        /* Teacher Message Box */
        .teacher-message-box {
            background: #092c1e;
            border: 1px solid #d4af37;
            border-radius: 12px;
            padding: 18px;
            font-size: 1.3rem;
            color: #ffffff;
            direction: rtl;
            text-align: right;
            margin-bottom: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        }

        /* Streamlit Selectbox & Inputs Fix for High Readability */
        .stSelectbox label {
            color: #f3c653 !important;
            font-size: 1.2rem !important;
            font-weight: bold;
        }
        
        div[data-baseweb="select"] > div {
            background-color: #0b3c29 !important;
            color: #ffffff !important;
            border: 2px solid #d4af37 !important;
            border-radius: 10px;
            font-size: 1.2rem;
        }

        /* Alphabet Cards */
        .alphabet-card {
            background: #0b3c29;
            border: 2px solid #d4af37;
            border-radius: 15px;
            padding: 20px 10px;
            text-align: center;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4);
            transition: all 0.3s ease;
        }

        .alphabet-card:hover {
            transform: translateY(-4px);
            border-color: #ffffff;
            box-shadow: 0 8px 20px rgba(212, 175, 55, 0.4);
        }

        /* Section Titles */
        .section-title {
            color: #f3c653;
            font-size: 1.6rem;
            margin-bottom: 20px;
            border-bottom: 2px dashed rgba(212, 175, 55, 0.4);
            padding-bottom: 8px;
            direction: rtl;
            text-align: right;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Navigation (Clean & Simple)
st.sidebar.markdown(
    "<h2 style='color: #f3c653; font-family: Amiri; text-align: center;'>⚡ AI Maktab</h2>",
    unsafe_allow_html=True,
)
main_menu = st.sidebar.radio("مینو منتخب کریں", ["📖 نورانی قاعدہ کورس"])

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

    # Takhti Selection Dropdown (Clear Text Color Fix)
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
                <strong>ہدایات:</strong> دائیں طرف سے پڑھنا شروع کریں۔ کسی بھی حرف کے نیچے دیے گئے تلفظ بٹن پر کلک کریں تاکہ AI استاد آپ کو درست تلفظ بتائے۔
            </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="teacher-message-box">🎙️ <span style="color: #f3c653;">استاد کا پیغام:</span> تختی نمبر 1 شروع ہو چکی ہے۔ حروفِ مفردات کو صاف اور درست تلفظ سے ادا کریں۔</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-title">حروف مفردات کی مشق</div>',
            unsafe_allow_html=True,
        )

        # Alphabet Cards Layout (Right to Left)
        col1, col2, col3, col4, col5 = st.columns(5)

        with col5:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; font-size: 3rem; margin:0;">ا</h1><p style="color:#ffffff; font-weight:bold; margin-top:5px;">Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ا", key="b_alif", use_container_width=True)

        with col4:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; font-size: 3rem; margin:0;">ب</h1><p style="color:#ffffff; font-weight:bold; margin-top:5px;">Ba</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ب", key="b_ba", use_container_width=True)

        with col3:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; font-size: 3rem; margin:0;">ت</h1><p style="color:#ffffff; font-weight:bold; margin-top:5px;">Ta</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ت", key="b_ta", use_container_width=True)

        with col2:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; font-size: 3rem; margin:0;">ث</h1><p style="color:#ffffff; font-weight:bold; margin-top:5px;">Tha</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ث", key="b_tha", use_container_width=True)

        with col1:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; font-size: 3rem; margin:0;">ج</h1><p style="color:#ffffff; font-weight:bold; margin-top:5px;">Jeem</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ج", key="b_jeem", use_container_width=True)

    elif selected_takhti == "تختی نمبر 2: حروف مرکبات (ملے ہوئے حروف)":
        st.markdown(
            """
            <div class="custom-info">
                <strong>ہدایات:</strong> مرکب حروف کو ایک ایک کر کے پہچانیں۔ ملی ہوئی حالت میں حروف کی شکل بدل جاتی ہے[cite: 6].
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="teacher-message-box">🎙️ <span style="color: #f3c653;">استاد کا پیغام:</span> مرکبات کی مشق شروع ہو چکی ہے۔ غور کریں کہ جڑنے کے بعد حروف کیسے لکھے جاتے ہیں۔</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-title">حروف مرکبات کی مشق</div>',
            unsafe_allow_html=True,
        )

        col1, col2, col3, col4 = st.columns(4)
        with col4:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; font-size: 2.5rem; margin:0;">لا</h1><p style="color:#ffffff; font-weight:bold; margin-top:5px;">Lam-Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 لا", key="m_la", use_container_width=True)
        with col3:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; font-size: 2.5rem; margin:0;">با</h1><p style="color:#ffffff; font-weight:bold; margin-top:5px;">Ba-Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 با", key="m_ba", use_container_width=True)
        with col2:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; font-size: 2.5rem; margin:0;">تا</h1><p style="color:#ffffff; font-weight:bold; margin-top:5px;">Ta-Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 تا", key="m_ta", use_container_width=True)
        with col1:
            st.markdown(
                '<div class="alphabet-card"><h1 style="color: #f3c653; font-family: Amiri; font-size: 2.5rem; margin:0;">ثا</h1><p style="color:#ffffff; font-weight:bold; margin-top:5px;">Tha-Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ثا", key="m_tha", use_container_width=True)

    else:
        st.markdown(
            '<div class="custom-info">اس تختی کا مواد تیزی سے تیار کیا جا رہا ہے، اگلی اپڈیٹ میں تمام الفاظ یہاں شو ہوں گے۔</div>',
            unsafe_allow_html=True,
        )
