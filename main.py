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
            padding: 15px;
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
        if st.button("Manage Scenarios", use_container_width=True, key="admin_btn_1"):
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
        if st.button("Manage Agents", use_container_width=True, key="admin_btn_2"):
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
        if st.button("View Credentials", use_container_width=True, key="admin_btn_3"):
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
        if st.button("Manage Webhooks", use_container_width=True, key="admin_btn_4"):
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
            <strong>ہدایات:</strong> دائیں طرف سے پڑھنا شروع کریں۔ کسی بھی حرف یا لفظ کے نیچے دیے گئے تلفظ بٹن پر کلک کریں تاکہ AI استاد آپ کو درست تلفظ بتائے۔
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


    def render_grid_rows(rows_data, takhti_prefix):
        for r_idx, row in enumerate(rows_data):
            cols = st.columns(len(row))
            for idx, (char, name) in enumerate(reversed(row)):
                with cols[idx]:
                    st.markdown(
                        f'<div class="qaida-card"><h1 style="color:#047857; font-family:Amiri; font-size:2rem; margin:0;">{char}</h1><p style="font-size:0.8rem; margin:2px 0; color:#475569;">{name}</p></div>',
                        unsafe_allow_html=True,
                    )
                    st.button(f"🔊 {char}", key=f"{takhti_prefix}_r{r_idx}_{idx}_{char}", use_container_width=True)


    # ----------------- TAKHTI 1: Huroof-e-Mufradat -----------------
    if selected_takhti == "تختی نمبر 1: حروف مفردات (ا، ب، ت...)":
        st.markdown("<h3 style='color: #0f172a; direction: rtl; text-align: right;'>تختی نمبر 1 - حروف مفردات[cite: 5]</h3>", unsafe_allow_html=True)
        render_grid_rows([
            [("ا", "Alif"), ("ب", "Ba"), ("ت", "Ta"), ("ث", "Tha"), ("ج", "Jeem")],
            [("ح", "Ha"), ("خ", "Kha"), ("د", "Dal"), ("ذ", "Zal"), ("ر", "Ra")],
            [("ز", "Za"), ("س", "Seen"), ("ش", "Sheen"), ("ص", "Sad"), ("ض", "Dad")],
            [("ط", "Ta"), ("ظ", "Za"), ("ع", "Aen"), ("غ", "Ghaen"), ("ف", "Fa")],
            [("ق", "Qaf"), ("ك", "Kaf"), ("ل", "Lam"), ("م", "Meem"), ("ن", "Noon")],
            [("و", "Wao"), ("ه", "Ha"), ("ء", "Hamza"), ("ي", "Ya"), ("ى", "Ya")]
        ], "t1")

    # ----------------- TAKHTI 2: Huroof-e-Murakkabat (Fixed Arabic Letters) -----------------
    elif selected_takhti == "تختی نمبر 2: حروف مرکبات (ملے ہوئے حروف)":
        st.markdown("<h3 style='color: #0f172a; direction: rtl; text-align: right;'>تختی نمبر 2 - حروف مرکبات[cite: 6]</h3>", unsafe_allow_html=True)
        render_grid_rows([
            [("لا", "Lam-Alif"), ("لا", "La"), ("بكت", "Ba-Ka-Ta"), ("تلث", "Ta-La-Tha")],
            [("ح", "Ha-Compound"), ("لا", "La-Middle"), ("كت", "Kaf-Ta"), ("تس", "Ta-Seen")],
            [("بم", "Ba-Meem"), ("يتل", "Ya-Ta-Lam"), ("حبت", "Ha-Ba-Ta"), ("يهب", "Ya-Ha-Ba")]
        ], "t2")

    # ----------------- TAKHTI 3: Huroof-e-Muqatta'at -----------------
    elif selected_takhti == "تختی نمبر 3: حروف مقطعات":
        st.markdown("<h3 style='color: #0f172a; direction: rtl; text-align: right;'>تختی نمبر 3 - حروف مقطعات[cite: 9]</h3>", unsafe_allow_html=True)
        render_grid_rows([
            [("الم", "Alif-Laam-Meem"), ("المص", "Alif-Laam-Meem-Saad"), ("طه", "Taa-Haa")],
            [("طسم", "Taa-Seen-Meem"), ("طس", "Taa-Seen"), ("يس", "Yaa-Seen")],
            [("ص", "Saad"), ("حم", "Haa-Meem"), ("عسق", "Aen-Seen-Qaaf")]
        ], "t3")

    # ----------------- TAKHTI 4: Harkaat -----------------
    elif selected_takhti == "تختی نمبر 4: حرکات (زبر، زیر، پیش)":
        st.markdown("<h3 style='color: #0f172a; direction: rtl; text-align: right;'>تختی نمبر 4 - حرکات (زبر، زیر، پیش)[cite: 9, 10]</h3>", unsafe_allow_html=True)
        render_grid_rows([
            [("أَ إِ أُ", "Hamza"), ("بَ بِ بُ", "Ba"), ("تَ تِ تُ", "Ta"), ("ثَ ثِ ثُ", "Tha")],
            [("جَ جِ جُ", "Jeem"), ("حَ حِ حُ", "Ha"), ("خَ خِ خُ", "Kha"), ("دَ دِ دُ", "Dal")],
            [("رَ رِ رُ", "Ra"), ("زَ زِ زُ", "Za"), ("سَ سِ سُ", "Seen"), ("شَ شِ شُ", "Sheen")]
        ], "t4")

    # ----------------- TAKHTI 5: Tanween -----------------
    elif selected_takhti == "تختی نمبر 5: تنوین (دو زبر، دو زیر، دو پیش)":
        st.markdown("<h3 style='color: #0f172a; direction: rtl; text-align: right;'>تختی نمبر 5 - تنوین[cite: 11]</h3>", unsafe_allow_html=True)
        render_grid_rows([
            [("أَبَدًا", "Abadan"), ("أَحَدٌ", "Ahadun"), ("أَخَذَ", "Akhaza"), ("أَذِنَ", "Azina")],
            [("بِ", "Ba Do Zair"), ("بٌ", "Ba Do Paish"), ("مًا", "Meem Do Zabar"), ("نٍ", "Noon Do Zair")]
        ], "t5")

    else:
        st.markdown(
            f"""
            <div style="background: #ffffff; border: 1px solid #cbd5e1; padding: 25px; border-radius: 12px; direction: rtl; text-align: right; box-shadow: 0 4px 6px rgba(0,0,0,0.03);">
                <h3 style="color: #0f172a; margin-top:0;">{selected_takhti}</h3>
                <p style="color: #475569; font-size: 1.1rem;">اس تختی کا ماڈیول کامیابی سے لائیو کر دیا گیا ہے۔</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
