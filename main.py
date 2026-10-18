import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Madrasaa - Admin & Portal",
    page_icon="🕌",
    layout="wide",
)

# Custom CSS for Clean White Background & Professional UI
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');

        /* Clean White Background for High Readability */
        .stApp {
            background-color: #f8fafc;
            color: #1e293b;
            font-family: 'Noto Nastaliq Urdu', serif;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #0f172a;
            border-right: 2px solid #cbd5e1;
        }
        
        [data-testid="stSidebar"] * {
            color: #ffffff !important;
            font-size: 1.1rem;
        }

        /* Header Box */
        .header-box {
            text-align: center;
            background: #ffffff;
            border: 2px solid #e2e8f0;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }

        .taawwudh-bismillah {
            font-family: 'Amiri', serif;
            font-size: 2.2rem;
            color: #047857;
            line-height: 1.8;
        }

        /* Admin Dashboard Cards */
        .admin-card {
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            margin-bottom: 15px;
        }
        
        .admin-card h3 {
            color: #0f172a;
            margin-bottom: 5px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar Navigation for Admin & Student Portals
st.sidebar.markdown(
    "<h2 style='color: #38bdf8; font-family: Amiri; text-align: center;'>🕌 AI Madrasaa</h2>",
    unsafe_allow_html=True,
)
navigation = st.sidebar.radio(
    "مینو منتخب کریں",
    ["⚙️ ایڈمن پینل (Admin Panel)", "📖 طالبعلم پورٹل (Noorani Qaida)"],
)

if navigation == "⚙️ ایڈمن پینل (Admin Panel)":
    st.markdown(
        """
        <div class="header-box">
            <h1 style="color: #0f172a; font-family: Amiri;">مرحباً - ایڈمنسٹریشن ڈیش بورڈ</h1>
            <p style="color: #64748b;">یہاں سے آپ سسٹمز، کورس اسکرپٹس اور اے آئی ایجنٹس کو کنٹرول کر سکتے ہیں۔</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="admin-card">
                <h3>📁 Scenarios</h3>
                <p style="color: #64748b; font-size: 0.9rem;">بنیادی کورس ورک فلو</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Manage Scenarios", use_container_width=True):
            st.success("Scenarios پینل اوپن ہو گیا ہے۔")

    with col2:
        st.markdown(
            """
            <div class="admin-card">
                <h3>🤖 AI Agents</h3>
                <p style="color: #64748b; font-size: 0.9rem;">تلفظ چیکنگ ماڈیول</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Manage Agents", use_container_width=True):
            st.success("AI Agents پینل اوپن ہو گیا ہے۔")

    with col3:
        st.markdown(
            """
            <div class="admin-card">
                <h3>📊 Credentials</h3>
                <p style="color: #64748b; font-size: 0.9rem;">API اور سیکیورٹی کیز</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("View Credentials", use_container_width=True):
            st.success("Credentials پینل اوپن ہو گیا ہے۔")

    with col4:
        st.markdown(
            """
            <div class="admin-card">
                <h3>🌐 Webhooks</h3>
                <p style="color: #64748b; font-size: 0.9rem;">آٹومیشن اور لنکس</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        if st.button("Manage Webhooks", use_container_width=True):
            st.success("Webhooks پینل اوپن ہو گیا ہے۔")

elif navigation == "📖 طالبعلم پورٹل (Noorani Qaida)":
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

    st.markdown(
        """
        <div style="background: #ffffff; border-right: 6px solid #047857; padding: 15px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); direction: rtl;">
            <strong>ہدایات:</strong> دائیں طرف سے پڑھنا شروع کریں۔ کسی بھی حرف کے نیچے دیے گئے تلفظ بٹن پر کلک کریں تاکہ AI استاد آپ کو درست تلفظ بتائے۔
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Takhti Selection
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
            "<h3 style='color: #0f172a; direction: rtl;'>حروف مفردات کی مشق</h3>",
            unsafe_allow_html=True,
        )

        col1, col2, col3, col4, col5 = st.columns(5)

        with col5:
            st.markdown(
                '<div style="background:#ffffff; border:2px solid #cbd5e1; border-radius:12px; padding:20px; text-align:center;"><h1 style="color:#047857; font-family:Amiri; font-size:3rem; margin:0;">ا</h1><p style="color:#334155; font-weight:bold; margin-top:5px;">Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ا", key="b_alif", use_container_width=True)

        with col4:
            st.markdown(
                '<div style="background:#ffffff; border:2px solid #cbd5e1; border-radius:12px; padding:20px; text-align:center;"><h1 style="color:#047857; font-family:Amiri; font-size:3rem; margin:0;">ب</h1><p style="color:#334155; font-weight:bold; margin-top:5px;">Ba</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ب", key="b_ba", use_container_width=True)

        with col3:
            st.markdown(
                '<div style="background:#ffffff; border:2px solid #cbd5e1; border-radius:12px; padding:20px; text-align:center;"><h1 style="color:#047857; font-family:Amiri; font-size:3rem; margin:0;">ت</h1><p style="color:#334155; font-weight:bold; margin-top:5px;">Ta</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ت", key="b_ta", use_container_width=True)

        with col2:
            st.markdown(
                '<div style="background:#ffffff; border:2px solid #cbd5e1; border-radius:12px; padding:20px; text-align:center;"><h1 style="color:#047857; font-family:Amiri; font-size:3rem; margin:0;">ث</h1><p style="color:#334155; font-weight:bold; margin-top:5px;">Tha</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ث", key="b_tha", use_container_width=True)

        with col1:
            st.markdown(
                '<div style="background:#ffffff; border:2px solid #cbd5e1; border-radius:12px; padding:20px; text-align:center;"><h1 style="color:#047857; font-family:Amiri; font-size:3rem; margin:0;">ج</h1><p style="color:#334155; font-weight:bold; margin-top:5px;">Jeem</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ج", key="b_jeem", use_container_width=True)

    else:
        st.info("اس تختی کا مواد یہاں لوڈ ہو رہا ہے...")
