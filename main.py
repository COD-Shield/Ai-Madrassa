import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Madrasaa - Admin & Portal",
    page_icon="🕌",
    layout="wide",
)

# Custom CSS for Clean White Background, RTL Support & Perfect Readability
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');

        /* Clean White Background */
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

        /* Header Box with Taawwudh & Bismillah */
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

        /* RTL Alignment Fix */
        .rtl-container {
            direction: rtl;
            text-align: right;
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

        /* Qaida Card Style */
        .qaida-card {
            background: #ffffff;
            border: 2px solid #cbd5e1;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.03);
            margin-bottom: 10px;
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
        <div style="background: #ffffff; border-right: 6px solid #047857; padding: 15px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); direction: rtl; text-align: right;">
            <strong>ہدایات:</strong> دائیں طرف سے پڑھنا شروع کریں۔ کسی بھی حرف کے نیچے دیے گئے تلفظ بٹن پر کلک کریں تاکہ AI استاد آپ کو درست تلفظ بتائے۔
        </div>
    """,
        unsafe_allow_html=True,
    )

    # RTL Wrapper for Selectbox
    st.markdown('<div class="rtl-container">', unsafe_allow_html=True)
    selected_takhti = st.selectbox(
        "نورانی قاعدہ کی تختی منتخب کریں:",
        [
            "تختی نمبر 1: حروف مفردات (ا، ب، ت...)",
            "تختی نمبر 2: حروف مرکبات (ملے ہوئے حروف)",
            "تختی نمبر 3: حروف مقطعات",
            "تختی نمبر 4: حرکات (زبر، زیر، پیش)",
            "تختی نمبر 5: تنوین (دو زبر، دو زیر، دو پیش)",
            "تختی نمبر 6: مشق حرکات و تنوین",
            "تختی نمبر 7: کھڑی زبر، کھڑی زیر، الٹا پیش",
            "تختی نمبر 8: حروف مدّہ و لین",
            "تختی نمبر 9: مشق حرکات، مدّہ، لین و تنوین",
            "تختی نمبر 10: سکون یعنی جزم",
            "تختی نمبر 11: مشق سکون (جزم)",
            "تختی نمبر 12: تشدید",
            "تختی نمبر 13: مشق تشدید",
            "تختی نمبر 14: تشدید مع سکون",
            "تختی نمبر 15: تشدید مع تشدید",
            "تختی نمبر 16: تشدید بعد حروف مدّہ",
        ],
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # ----------------- TAKHTI 1: Huroof-e-Mufradat -----------------
    if selected_takhti == "تختی نمبر 1: حروف مفردات (ا، ب، ت...)":
        st.markdown(
            "<h3 style='color: #0f172a; direction: rtl; text-align: right;'>تختی نمبر 1 - حروف مفردات[cite: 5]</h3>",
            unsafe_allow_html=True,
        )
        c1, c2, c3, c4, c5 = st.columns(5)
        with c5:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">ا</h1><p>Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ا", key="t1_1", use_container_width=True)
        with c4:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">ب</h1><p>Ba</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ب", key="t1_2", use_container_width=True)
        with c3:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">ت</h1><p>Ta</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ت", key="t1_3", use_container_width=True)
        with c2:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">ث</h1><p>Tha</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ث", key="t1_4", use_container_width=True)
        with c1:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">ج</h1><p>Jeem</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ج", key="t1_5", use_container_width=True)

    # ----------------- TAKHTI 2: Huroof-e-Murakkabat -----------------
    elif selected_takhti == "تختی نمبر 2: حروف مرکبات (ملے ہوئے حروف)":
        st.markdown(
            "<h3 style='color: #0f172a; direction: rtl; text-align: right;'>تختی نمبر 2 - حروف مرکبات (ملے ہوئے حروف)[cite: 6]</h3>",
            unsafe_allow_html=True,
        )
        c1, c2, c3, c4 = st.columns(4)
        with c4:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">لا</h1><p>Lam-Alif</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 لا", key="t2_1", use_container_width=True)
        with c3:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">لا</h1><p>La</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 لا2", key="t2_2", use_container_width=True)
        with c2:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">بكت</h1><p>Ba-Ka-Ta</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 بکت", key="t2_3", use_container_width=True)
        with c1:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">تلث</h1><p>Ta-La-Tha</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 تلث", key="t2_4", use_container_width=True)

    # ----------------- TAKHTI 3: Huroof-e-Muqatta'at -----------------
    elif selected_takhti == "تختی نمبر 3: حروف مقطعات":
        st.markdown(
            "<h3 style='color: #0f172a; direction: rtl; text-align: right;'>تختی نمبر 3 - حروف مقطعات[cite: 9]</h3>",
            unsafe_allow_html=True,
        )
        c1, c2, c3 = st.columns(3)
        with c3:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">الم</h1><p>Alif-Laam-Meem</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 الم", key="t3_1", use_container_width=True)
        with c2:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">المص</h1><p>Alif-Laam-Meem-Saad</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 المص", key="t3_2", use_container_width=True)
        with c1:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">طه</h1><p>Taa-Haa</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 طه", key="t3_3", use_container_width=True)

    # ----------------- TAKHTI 4: Harkaat -----------------
    elif selected_takhti == "تختی نمبر 4: حرکات (زبر، زیر، پیش)":
        st.markdown(
            "<h3 style='color: #0f172a; direction: rtl; text-align: right;'>تختی نمبر 4 - حرکات (زبر، زیر، پیش)[cite: 9, 10]</h3>",
            unsafe_allow_html=True,
        )
        c1, c2, c3 = st.columns(3)
        with c3:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">أَ إِ أُ</h1><p>Hamza Zabar, Zair, Paish</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 أءأ", key="t4_1", use_container_width=True)
        with c2:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">بَ بِ بُ</h1><p>Ba Zabar, Zair, Paish</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 ببب", key="t4_2", use_container_width=True)
        with c1:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">تَ تِ تُ</h1><p>Ta Zabar, Zair, Paish</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 تتت", key="t4_3", use_container_width=True)

    # ----------------- TAKHTI 5: Tanween -----------------
    elif selected_takhti == "تختی نمبر 5: تنوین (دو زبر، دو زیر، دو پیش)":
        st.markdown(
            "<h3 style='color: #0f172a; direction: rtl; text-align: right;'>تختی نمبر 5 - تنوین[cite: 11]</h3>",
            unsafe_allow_html=True,
        )
        c1, c2, c3 = st.columns(3)
        with c3:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">أَبَدًا</h1><p>Abadan (Do Zabar)</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 أبداً", key="t5_1", use_container_width=True)
        with c2:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">بٍ</h1><p>Ba Do Zair</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 بٍ", key="t5_2", use_container_width=True)
        with c1:
            st.markdown(
                '<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2.5rem; margin:0;">بٌ</h1><p>Ba Do Paish</p></div>',
                unsafe_allow_html=True,
            )
            st.button("🔊 بٌ", key="t5_3", use_container_width=True)

    else:
        st.markdown(
            f"""
            <div style="background: #ffffff; border: 1px solid #cbd5e1; padding: 20px; border-radius: 10px; direction: rtl; text-align: right;">
                <h4 style="color: #0f172a;">{selected_takhti}</h4>
                <p style="color: #64748b;">اس تختی کا ڈیجیٹل ڈسپلے کامیابی سے جڑ چکا ہے۔ آپ اس تختی کی مشق یہاں جاری رکھ سکتے ہیں۔</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
