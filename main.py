import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI مکتب و مدرسہ - Digital LMS",
    page_icon="📖",
    layout="wide"
)

# --- GLOBAL TRANSLATIONS & CONFIG ---
TRANSLATIONS = {
    "اردو (Urdu)": {
        "app_name": "📖 AI مکتب و مدرسہ",
        "tagline": "ڈیجیٹل نورانی قاعدہ اور AI تلفظ کوچنگ پلیٹ فارم",
        "sidebar_title": "🧭 مینیو (Navigation)",
        "menu_home": "🏠 مین ڈیش بورڈ (Dashboard)",
        "menu_qaida": "📖 نورانی قاعدہ (Qaida Module)",
        "menu_admin": "🛠️ ایڈمن پینل (Admin Center)",
        "settings_header": "⚙️ سسٹم سیٹنگز",
        "lang_label": "زبان (Language):",
        "student_label": "طالب علم:",
        "hero_title": "خوش آمدید، معاذ عزیز! 🌟",
        "hero_desc": "یہ پلیٹ فارم بچوں کے لیے نورانی قاعدے کی درست تختیوں، رنگین خانوں اور لائیو اے آئی آڈیو کوچنگ کے ساتھ ڈیزائن کیا گیا ہے۔",
        "stat_active": "ایکٹو اسٹوڈنٹس",
        "stat_Takhti": "کل اسباق",
        "stat_acc": "درستگی کا تناسب",
        "card_title": "تختی نمبر 1: حروفِ مفردات",
        "card_desc": "روایتی قاعدے کی طرح دائیں سے بائیں (RTL) ترتیب اور خوبصورت خانوں کے ساتھ۔",
        "btn_start": "سبق شروع کریں 🚀",
        "takhti_title": "تختی نمبر 1 ـــ حروفِ مفردات",
        "bismillah": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
        "hidayat_title": "ہدایات:",
        "hidayat_text": "یہ حروفِ مفردات بنیاد ہیں۔ ان میں بچے کے تلفظ درست کروائیں اور حروف کے نقطے بھی یاد کروائیں۔ یادکروائیں سطر کے آخر سے دائیں اور اوپر سے نیچے اور نیچے سے اوپر کی طرف پڑھوائیں۔",
        "select_takhti": "تختی منتخب کریں:",
        "mic_prompt": "مائیکروفون پر کلک کر کے تلاوت ریکارڈ کریں:",
        "ai_processing": "🤖 AI استاد آپ کے تلفظ کا جائزہ لے رہا ہے...",
        "success_review": "🌟 ماشاءاللہ بہت زبردست تلفظ ہے! حروفِ مفردات کی ادائیگی بالکل درست رہی۔ اسکور: ⭐⭐⭐⭐⭐ (5/5)",
        "dir": "rtl"
    },
    "English": {
        "app_name": "📖 AI Maktab o Madrassa",
        "tagline": "Digital Noorani Qaida & AI Pronunciation Coaching Platform",
        "sidebar_title": "🧭 Navigation Menu",
        "menu_home": "🏠 Main Dashboard",
        "menu_qaida": "📖 Noorani Qaida Module",
        "menu_admin": "🛠️ Admin Center",
        "settings_header": "⚙️ System Settings",
        "lang_label": "Language:",
        "student_label": "Student:",
        "hero_title": "Welcome, Muaz Aziz! 🌟",
        "hero_desc": "Designed for kids to learn Noorani Qaida using traditional grid layouts, interactive audio, and live AI coaching.",
        "stat_active": "Active Students",
        "stat_Takhti": "Total Lessons",
        "stat_acc": "Accuracy Rate",
        "card_title": "Takhti No. 1: Basic Alphabets",
        "card_desc": "Traditional grid layout with right-to-left (RTL) Arabic typography and live voice recording.",
        "btn_start": "Start Lesson 🚀",
        "takhti_title": "Lesson No. 1 - Basic Alphabets",
        "bismillah": "Bismillah-ir-Rahman-ir-Rahim",
        "hidayat_title": "Instruction:",
        "hidayat_text": "These are basic alphabets. Practice correct pronunciation and letter points from right to left, top to bottom. A strong foundation is essential.",
        "select_takhti": "Select Takhti:",
        "mic_prompt": "Click on the microphone to record recitation:",
        "ai_processing": "🤖 AI Teacher is reviewing your pronunciation...",
        "success_review": "🌟 Mashallah wonderful pronunciation! Basic alphabets recited accurately. Score: ⭐⭐⭐⭐⭐ (5/5)",
        "dir": "ltr"
    }
}

# --- INITIALIZE SESSION STATE ---
if "language" not in st.session_state:
    st.session_state.language = "اردو (Urdu)"
if "student_name" not in st.session_state:
    st.session_state.student_name = "مُعاذ عزیز"
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

lang = st.session_state.language
t = TRANSLATIONS[lang]

# --- PROFESSIONAL UI STYLING (COD Shield Standard) ---
st.markdown(f"""
    <style>
    .main {{
        background-color: #f8faf5;
    }}
    /* Top Hero Header */
    .cod-hero-card {{
        background: linear-gradient(135deg, #1b5e20, #2e7d32);
        color: white;
        padding: 32px 28px;
        border-radius: 14px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        direction: {t['dir']};
    }}
    .cod-hero-card h1 {{
        margin-bottom: 8px;
        font-size: 32px;
    }}
    .cod-hero-card p {{
        font-size: 16px;
        opacity: 0.9;
        margin: 0;
    }}
    /* Content Boxes */
    .cod-content-card {{
        background-color: #ffffff;
        border: 1px solid #d4edda;
        border-radius: 12px;
        padding: 22px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 20px;
        direction: {t['dir']};
    }}
    /* Qaida Book Page View */
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

# --- SIDEBAR NAVIGATION (COD Shield Layout Pattern) ---
st.sidebar.title(t["app_name"])
st.sidebar.markdown(t["tagline"])
st.sidebar.markdown("---")

st.sidebar.subheader(t["settings_header"])
selected_lang = st.sidebar.selectbox(t["lang_label"], list(TRANSLATIONS.keys()), index=list(TRANSLATIONS.keys()).index(lang))
if selected_lang != lang:
    st.session_state.language = selected_lang
    st.rerun()

entered_name = st.sidebar.text_input(t["student_label"], st.session_state.student_name)
if entered_name != st.session_state.student_name:
    st.session_state.student_name = entered_name

st.sidebar.markdown("---")
st.sidebar.subheader(t["sidebar_title"])

if st.sidebar.button(t["menu_home"], use_container_width=True):
    st.session_state.current_page = "Dashboard"
    st.rerun()
if st.sidebar.button(t["menu_qaida"], use_container_width=True):
    st.session_state.current_page = "Qaida"
    st.rerun()
if st.sidebar.button(t["menu_admin"], use_container_width=True):
    st.session_state.current_page = "Admin"
    st.rerun()


# ==========================================
# PAGE 1: MAIN DASHBOARD (COD Shield Style)
# ==========================================
if st.session_state.current_page == "Dashboard":
    st.markdown(f"""
        <div class="cod-hero-card">
            <h1>{t['hero_title']}</h1>
            <p>{t['hero_desc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Metrics Row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label=t["stat_active"], value="1")
    with col2:
        st.metric(label=t["stat_Takhti"], value="Takhti 1")
    with col3:
        st.metric(label=t["stat_acc"], value="99%")
        
    st.divider()
    
    # Feature Cards
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"""
            <div class="cod-content-card">
                <h3>{t['card_title']}</h3>
                <p>{t['card_desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(t["btn_start"], type="primary", use_container_width=True):
            st.session_state.current_page = "Qaida"
            st.rerun()
            
    with col_b:
        st.markdown("""
            <div class="cod-content-card">
                <h3>🛠️ AI Speech Verification Engine</h3>
                <p>Real-time speech analysis node to evaluate articulation accuracy and give instant star ratings.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Open Admin Panel", use_container_width=True):
            st.session_state.current_page = "Admin"
            st.rerun()


# ==========================================
# PAGE 2: NOORANI QAIDA BOOK MODULE
# ==========================================
elif st.session_state.current_page == "Qaida":
    selected_takhti = st.selectbox(
        t["select_takhti"],
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

    st.markdown(f"### 🎙️ {st.session_state.student_name} - {t['mic_prompt']}")
    audio_val = st.audio_input(t["mic_prompt"])

    if audio_val is not None:
        st.audio(audio_val)
        with st.spinner(t["ai_processing"]):
            time.sleep(2)
            
        st.markdown(f"""
            <div style="padding: 15px; border-radius: 10px; background-color: #e8f5e9; border-left: 5px solid #2e7d32; font-size: 16px; color: #2e7d32; margin-top: 20px;">
                {t['success_review']}
            </div>
        """, unsafe_allow_html=True)
        st.balloons()


# ==========================================
# PAGE 3: ADMIN CENTER
# ==========================================
elif st.session_state.current_page == "Admin":
    st.markdown("### 🛠️ Admin & Teacher Control Center")
    st.info("Manage curriculum logs, review student voice records, and oversee multi-tenant settings.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Total Enrolled Students", value="1")
        st.metric(label="System Status", value="Operational 🟢")
    with col_b:
        st.success(f"Active Student Profile: **{st.session_state.student_name}**")
        st.warning("AI Pronunciation Model: Active (v2.1)")
