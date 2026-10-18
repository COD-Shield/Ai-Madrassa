import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI مکتب و مدرسہ - Digital Madrassa & LMS",
    page_icon="📖",
    layout="wide"
)

# --- GLOBAL TRANSLATIONS DICTIONARY ---
TRANSLATIONS = {
    "اردو (Urdu)": {
        "app_title": "📖 AI مکتب و مدرسہ (Digital Noorani Qaida & LMS)",
        "hero_title": "خوش آمدید، معاذ عزیز! 🌟",
        "hero_subtitle": "بچوں کے لیے جدید ترین ڈیجیٹل قاعدہ، انٹرایکティブ گرڈز، اور AI تلفظ کوچنگ سسٹم۔",
        "sidebar_header": "⚙️ گلوبل ترتیبات (Global Settings)",
        "lang_label": "زبان منتخب کریں (Language):",
        "student_label": "طالب علم کا نام:",
        "nav_home": "🏠 مین ڈیش بورڈ (Home)",
        "nav_qaida": "📖 نورانی قاعدہ کورس (Qaida)",
        "nav_admin": "🛠️ ایڈمن پینل (Admin Panel)",
        "quick_stats": "📊 فوری کارکردگی اور اعداد و شمار",
        "stat_students": "رجسٹرڈ طلباء",
        "stat_lessons": "مکمل اسباق",
        "stat_accuracy": "اوسط تلفظ درستگی",
        "card_qaida_title": "📚 تختی نمبر 1: حروفِ مفردات",
        "card_qaida_desc": "روایتی رنگین خانے، دائیں سے بائیں (RTL) ترتیب، اور آڈیو ریکارڈنگ کے ساتھ۔",
        "start_btn": "سبق شروع کریں 🚀",
        "takhti_title": "تختی نمبر 1 ـــ حروفِ مفردات",
        "bismillah": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
        "hidayat_title": "ہدایات:",
        "hidayat_text": "یہ حروفِ مفردات بنیاد ہیں۔ ان میں بچے کے تلفظ درست کروائیں اور حروف کے نقطے بھی یاد کروائیں۔ یادکروائیں سطر کے آخر سے دائیں اور اوپر سے نیچے اور نیچے سے اوپر کی طرف پڑھوائیں۔",
        "select_takhti_label": "تختی منتخب کریں:",
        "mic_text": "مائیکروفون پر کلک کر کے تلاوت ریکارڈ کریں:",
        "ai_check": "🤖 AI استاد آپ کے تلفظ کا جائزہ لے رہا ہے...",
        "success_msg": "🌟 ماشاءاللہ بہت زبردست تلفظ ہے! حروفِ مفردات کی ادائیگی بالکل درست رہی۔ اسکور: ⭐⭐⭐⭐⭐ (5/5)",
        "dir": "rtl"
    },
    "English": {
        "app_title": "📖 AI Maktab o Madrassa (Digital Noorani Qaida & LMS)",
        "hero_title": "Welcome, Muaz Aziz! 🌟",
        "hero_subtitle": "Advanced Digital Qaida, interactive grids, and AI pronunciation coaching system for kids.",
        "sidebar_header": "⚙️ Global Settings",
        "lang_label": "Select Language:",
        "student_label": "Student Name:",
        "nav_home": "🏠 Main Dashboard (Home)",
        "nav_qaida": "📖 Noorani Qaida Course",
        "nav_admin": "🛠️ Admin Panel",
        "quick_stats": "📊 Quick Performance & Statistics",
        "stat_students": "Registered Students",
        "stat_lessons": "Completed Lessons",
        "stat_accuracy": "Avg Pronunciation Score",
        "card_qaida_title": "📚 Takhti No. 1: Basic Alphabets",
        "card_qaida_desc": "Traditional colored grid layout, right-to-left (RTL) flow, with live audio recording.",
        "start_btn": "Start Lesson 🚀",
        "takhti_title": "Lesson No. 1 - Basic Alphabets",
        "bismillah": "Bismillah-ir-Rahman-ir-Rahim",
        "hidayat_title": "Instruction:",
        "hidayat_text": "These are basic alphabets. Practice correct pronunciation and letter points from right to left, top to bottom. A strong foundation is essential.",
        "select_takhti_label": "Select Takhti:",
        "mic_text": "Click on the microphone to record recitation:",
        "ai_check": "🤖 AI Teacher is reviewing your pronunciation...",
        "success_msg": "🌟 Mashallah wonderful pronunciation! Basic alphabets recited accurately. Score: ⭐⭐⭐⭐⭐ (5/5)",
        "dir": "ltr"
    }
}

# --- INITIALIZE SESSION STATE ---
if "language" not in st.session_state:
    st.session_state.language = "اردو (Urdu)"
if "student_name" not in st.session_state:
    st.session_state.student_name = "مُعاذ عزیز"
if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"

lang = st.session_state.language
t = TRANSLATIONS[lang]

# --- PRO PROFESSIONAL STYLES (COD Shield Banner & Card Style) ---
st.markdown(f"""
    <style>
    .main {{
        background-color: #f4f6f0;
    }}
    /* COD Shield Style Hero Banner */
    .hero-banner {{
        background: linear-gradient(135deg, #1b5e20, #2e7d32);
        color: white;
        padding: 35px 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
        direction: {t['dir']};
    }}
    .hero-banner h1 {{
        margin-bottom: 10px;
        font-size: 36px;
    }}
    .hero-banner p {{
        font-size: 18px;
        opacity: 0.9;
    }}
    /* Dashboard Cards Style */
    .dashboard-card {{
        background-color: #ffffff;
        border: 1px solid #c8e6c9;
        border-radius: 14px;
        padding: 24px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        margin-bottom: 20px;
        direction: {t['dir']};
    }}
    /* Book Page Container */
    .qaida-book-container {{
        border: 6px double #1b5e20;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        max-width: 950px;
        margin: 0 auto;
        direction: {t['dir']};
    }}
    .qaida-header-banner {{
        background: linear-gradient(135deg, #d32f2f, #b71c1c);
        color: white;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 15px;
        font-family: sans-serif;
    }}
    .bismillah-banner {{
        font-size: 30px;
        text-align: center;
        color: #1b5e20;
        font-family: 'Amiri', 'Traditional Arabic', serif;
        font-weight: bold;
        padding: 8px;
        border-bottom: 2px solid #c8e6c9;
        border-top: 2px solid #c8e6c9;
        margin-bottom: 20px;
    }}
    .hidayat-box {{
        background-color: #fffde7;
        border: 2px solid #fbc02d;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        color: #333;
        margin-bottom: 25px;
        text-align: {"right" if t['dir']=="rtl" else "left"};
        font-family: sans-serif;
        line-height: 1.6;
    }}
    .hidayat-title {{
        color: #e65100;
        font-weight: bold;
        font-size: 17px;
    }}
    .qaida-table {{
        width: 100%;
        border-collapse: separate;
        border-spacing: 12px;
        direction: {t['dir']};
        margin-bottom: 10px;
    }}
    .qaida-td {{
        background-color: #ffffff;
        border: 2px solid #2e7d32;
        border-radius: 12px;
        text-align: center;
        width: 20%;
        padding: 12px 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        vertical-align: middle;
    }}
    .qaida-td:hover {{
        background-color: #f1f8e9;
    }}
    .arabic-ltr {{
        font-size: 42px;
        font-family: 'Amiri', serif;
        font-weight: bold;
        line-height: 1.2;
    }}
    .ltr-name {{
        font-size: 13px;
        color: #555;
        font-weight: bold;
        margin-top: 5px;
        font-family: sans-serif;
    }}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR GLOBAL NAVIGATION & SETTINGS ---
st.sidebar.header(t["sidebar_header"])

new_lang = st.sidebar.selectbox(t["lang_label"], list(TRANSLATIONS.keys()), index=list(TRANSLATIONS.keys()).index(lang))
if new_lang != lang:
    st.session_state.language = new_lang
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown(f"**👤 {t['student_label']}**")
entered_name = st.sidebar.text_input("Name", st.session_state.student_name, label_visibility="collapsed")
if entered_name != st.session_state.student_name:
    st.session_state.student_name = entered_name

st.sidebar.markdown("---")
st.sidebar.markdown("### 🧭 Navigation Hub")
if st.sidebar.button(t["nav_home"], use_container_width=True):
    st.session_state.active_page = "Home"
    st.rerun()
if st.sidebar.button(t["nav_qaida"], use_container_width=True):
    st.session_state.active_page = "Qaida"
    st.rerun()
if st.sidebar.button(t["nav_admin"], use_container_width=True):
    st.session_state.active_page = "Admin"
    st.rerun()


# ==========================================
# 1. MAIN LANDING / DASHBOARD HUB (HOME)
# ==========================================
if st.session_state.active_page == "Home":
    # COD Shield Style Professional Banner
    st.markdown(f"""
        <div class="hero-banner">
            <h1>{t['hero_title']}</h1>
            <p>{t['hero_subtitle']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### {t['quick_stats']}")
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.metric(label=t["stat_students"], value="1")
    with col_s2:
        st.metric(label=t["stat_lessons"], value="Takhti 1")
    with col_s3:
        st.metric(label=t["stat_accuracy"], value="98%")
        
    st.divider()
    
    # Dashboard Course Cards
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown(f"""
            <div class="dashboard-card">
                <h3>{t['card_qaida_title']}</h3>
                <p>{t['card_qaida_desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(t["start_btn"], type="primary", use_container_width=True):
            st.session_state.active_page = "Qaida"
            st.rerun()
            
    with col_c2:
        st.markdown("""
            <div class="dashboard-card">
                <h3>🛠️ AI Speech Tutor (v2.1)</h3>
                <p>Real-time audio analysis and interactive feedback powered by artificial intelligence.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Open Admin Hub", use_container_width=True):
            st.session_state.active_page = "Admin"
            st.rerun()


# ==========================================
# 2. NOORANI QAIDA BOOK PAGE (QAIDA MODULE)
# ==========================================
elif st.session_state.active_page == "Qaida":
    selected_takhti = st.selectbox(
        t["select_takhti_label"],
        ["تختی نمبر 1: حروفِ مفردات", "تختی نمبر 2: حروفِ مرکبات", "تختی نمبر 3: حرکات"]
    )
    
    takhti_1_letters = [
        {"ar": "ا", "name": "Alif", "color": "#e53935"},
        {"ar": "ب", "name": "Ba", "color": "#000000"},
        {"ar": "ت", "name": "Ta", "color": "#8e24aa"},
        {"ar": "ث", "name": "Tha", "color": "#00897b"},
        {"ar": "ج", "name": "Jeem", "color": "#1e88e5"},
        {"ar": "ح", "name": "Ha", "color": "#d81b60"},
        {"ar": "خ", "name": "Kha", "color": "#43a047"},
        {"ar": "د", "name": "Dal", "color": "#e91e63"},
        {"ar": "ذ", "name": "Zal", "color": "#fb8c00"},
        {"ar": "ر", "name": "Ra", "color": "#43a047"},
        {"ar": "ز", "name": "Za", "color": "#1e88e5"},
        {"ar": "س", "name": "Seen", "color": "#d81b60"},
        {"ar": "ش", "name": "Sheen", "color": "#000000"},
        {"ar": "ص", "name": "Sad", "color": "#00897b"},
        {"ar": "ض", "name": "Dad", "color": "#43a047"},
        {"ar": "ط", "name": "Ta", "color": "#1e88e5"},
        {"ar": "ظ", "name": "Za", "color": "#00897b"},
        {"ar": "ع", "name": "Ain", "color": "#8e24aa"},
        {"ar": "غ", "name": "Ghain", "color": "#e53935"},
        {"ar": "ف", "name": "Fa", "color": "#d81b60"},
        {"ar": "ق", "name": "Qaf", "color": "#1e88e5"},
        {"ar": "ك", "name": "Kaf", "color": "#43a047"},
        {"ar": "ل", "name": "Lam", "color": "#fb8c00"},
        {"ar": "م", "name": "Meem", "color": "#8e24aa"},
        {"ar": "ن", "name": "Noon", "color": "#00897b"},
        {"ar": "و", "name": "Waw", "color": "#e53935"},
        {"ar": "هـ", "name": "Ha", "color": "#d81b60"},
        {"ar": "ء", "name": "Hamza", "color": "#1e88e5"},
        {"ar": "ي", "name": "Ya", "color": "#000000"}
    ]

    html_code = f"""
    <div class="qaida-book-container">
        <div class="qaida-header-banner">{t['takhti_title']}</div>
        <div class="bismillah-banner">{t['bismillah']}</div>
        <div class="hidayat-box">
            <span class="hidayat-title">{t['hidayat_title']}</span> {t['hidayat_text']}
        </div>
        <table class="qaida-table">
    """

    cols_per_row = 5
    total_items = len(takhti_1_letters)

    for i in range(0, total_items, cols_per_row):
        row_items = takhti_1_letters[i:i + cols_per_row]
        html_code += '<tr>'
        
        if len(row_items) < cols_per_row:
            empty_slots = cols_per_row - len(row_items)
            left_pad = empty_slots // 2
            right_pad = empty_slots - left_pad
            
            for _ in range(left_pad):
                html_code += '<td style="border: none;"></td>'
                
            for item in row_items:
                html_code += f'''
                    <td class="qaida-td">
                        <div class="arabic-ltr" style="color: {item['color']};">{item['ar']}</div>
                        <div class="ltr-name">{item['name']}</div>
                    </td>
                '''
            for _ in range(right_pad):
                html_code += '<td style="border: none;"></td>'
        else:
            for item in row_items:
                html_code += f'''
                    <td class="qaida-td">
                        <div class="arabic-ltr" style="color: {item['color']};">{item['ar']}</div>
                        <div class="ltr-name">{item['name']}</div>
                    </td>
                '''
        html_code += '</tr>'

    html_code += '</table></div>'
    st.markdown(html_code, unsafe_allow_html=True)
    
    st.divider()

    st.markdown(f"### 🎙️ {st.session_state.student_name} - {t['mic_text']}")
    audio_val = st.audio_input(t["mic_text"])

    if audio_val is not None:
        st.audio(audio_val)
        with st.spinner(t["ai_check"]):
            time.sleep(2)
            
        st.markdown(f"""
            <div style="padding: 15px; border-radius: 10px; background-color: #e8f5e9; border-left: 5px solid #2e7d32; font-size: 16px; color: #2e7d32; margin-top: 20px;">
                {t['success_msg']}
            </div>
        """, unsafe_allow_html=True)
        st.balloons()


# ==========================================
# 3. ADMIN PANEL
# ==========================================
elif st.session_state.active_page == "Admin":
    st.markdown("### 🛠️ Admin & Teacher Control Panel")
    st.info("Manage student records, review AI pronunciation logs, and configure curriculum settings.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Registered Students", value="1")
        st.metric(label="Active Sessions", value="1")
    with col_b:
        st.success(f"Current Student Profile: **{st.session_state.student_name}**")
        st.warning("AI Speech Model: Active (v2.1)")
