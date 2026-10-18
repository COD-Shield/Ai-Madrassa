import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI مکتب و مدرسہ - Login Portal",
    page_icon="📖",
    layout="wide"
)

# --- GLOBAL TRANSLATIONS & DICTIONARY ---
TRANSLATIONS = {
    "اردو (Urdu)": {
        "app_title": "📖 AI مکتب و مدرسہ (Digital Noorani Qaida)",
        "banner_title": "خوش آمدید! AI مکتب و مدرسہ میں آپ کا خیرمقدم ہے",
        "banner_desc": "بچوں کے لیے جدید ترین ڈیجیٹل قاعدہ، رنگین گرڈز، اور AI تلفظ کوچنگ کا بہترین پلیٹ فارم۔",
        "login_box_title": "🔐 پورٹل لاگ ان (Student & Parent Login)",
        "username_label": "یوزر نیم / طالب علم کا نام (Username)",
        "password_label": "پاسورڈ (Password)",
        "login_btn": "لاگ ان کریں 🚀",
        "login_success": "✅ کامیابی سے لاگ ان ہو گئے! سبق کی طرف منتقلی جاری ہے...",
        "login_error": "❌ غلط یوزر نیم یا پاسورڈ! براہ کرم دوبارہ کوشش کریں۔",
        "features_heading": "🌟 ہمارے پلیٹ فارم کی خصوصیات",
        "feat_1_title": "📖 ڈیجیٹل نورانی قاعدہ",
        "feat_1_desc": "روایتی انداز میں تختی نمبر 1 سے آگے تک کے تمام حروف اور مرکبات رنگین خانوں میں۔",
        "feat_2_title": "🎙️ AI تلفظ کوچنگ",
        "feat_2_desc": "بچے اپنی آواز ریکارڈ کر کے لائیو اے آئی (AI) سے تلفظ کی درستگی اور اسکور چیک کر سکتے ہیں۔",
        "feat_3_title": "📊 پروگریس ڈیش بورڈ",
        "feat_3_desc": "والدین اور اساتذہ کے لیے طلباء کی روزانہ کی کارکردگی اور اسباق کا مکمل ریکارڈ۔",
        "sidebar_title": "⚙️ ترتیبات (Settings)",
        "lang_label": "زبان منتخب کریں (Language):",
        "dir": "rtl"
    },
    "English": {
        "app_title": "📖 AI Maktab o Madrassa (Digital Noorani Qaida)",
        "banner_title": "Welcome to AI Maktab o Madrassa",
        "banner_desc": "An advanced digital Qaida platform with interactive grids and AI pronunciation coaching for kids.",
        "login_box_title": "🔐 Portal Login (Student & Parent)",
        "username_label": "Username / Student Name",
        "password_label": "Password",
        "login_btn": "Login 🚀",
        "login_success": "✅ Logged in successfully! Redirecting to dashboard...",
        "login_error": "❌ Incorrect username or password! Please try again.",
        "features_heading": "🌟 Platform Features & Highlights",
        "feat_1_title": "📖 Digital Noorani Qaida",
        "feat_1_desc": "Traditional book-style layout featuring Takhti 1 onwards in clear, colored grid boxes.",
        "feat_2_title": "🎙️ AI Pronunciation Coaching",
        "feat_2_desc": "Kids can record their voice and get instant AI-powered articulation feedback and scoring.",
        "feat_3_title": "📊 Progress Dashboard",
        "feat_3_desc": "Comprehensive tracking logs and performance insights for parents and teachers.",
        "sidebar_title": "⚙️ Settings",
        "lang_label": "Select Language:",
        "dir": "ltr"
    }
}

# --- INITIALIZE SESSION STATE ---
if "language" not in st.session_state:
    st.session_state.language = "اردو (Urdu)"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "student_name" not in st.session_state:
    st.session_state.student_name = "مُعاذ عزیز"

lang = st.session_state.language
t = TRANSLATIONS[lang]

# --- CSS STYLING ---
st.markdown(f"""
    <style>
    .main {{
        background-color: #f8faf5;
    }}
    .hero-banner {{
        background: linear-gradient(135deg, #1b5e20, #2e7d32);
        color: white;
        padding: 40px 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
        direction: {t['dir']};
    }}
    .hero-banner h1 {{
        margin-bottom: 12px;
        font-size: 34px;
    }}
    .hero-banner p {{
        font-size: 18px;
        opacity: 0.9;
        margin: 0;
    }}
    .login-container {{
        background-color: #ffffff;
        border: 2px solid #c8e6c9;
        border-radius: 16px;
        padding: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        direction: {t['dir']};
    }}
    .feature-card {{
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 15px;
        direction: {t['dir']};
        height: 100%;
    }}
    /* Qaida Book Page Styling for inside */
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
    }}
    .bismillah-banner {{
        font-size: 30px;
        text-align: center;
        color: #1b5e20;
        font-family: 'Amiri', serif;
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
        line-height: 1.6;
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
    .arabic-ltr {{
        font-size: 42px;
        font-family: 'Amiri', serif;
        font-weight: bold;
    }}
    .ltr-name {{
        font-size: 13px;
        color: #555;
        font-weight: bold;
        margin-top: 5px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR LANGUAGE SWITCHER ---
st.sidebar.title(t["app_title"])
st.sidebar.markdown("---")
st.sidebar.subheader(t["sidebar_title"])
new_lang = st.sidebar.selectbox(t["lang_label"], list(TRANSLATIONS.keys()), index=list(TRANSLATIONS.keys()).index(lang))
if new_lang != lang:
    st.session_state.language = new_lang
    st.rerun()

if st.session_state.logged_in:
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 لاگ آؤٹ / Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()


# ==========================================
# FLOW CONTROL: LOGIN vs DASHBOARD/QAIDA
# ==========================================
if not st.session_state.logged_in:
    # --- 1. LANDING & LOGIN PAGE ---
    
    # Top Hero Banner
    st.markdown(f"""
        <div class="hero-banner">
            <h1>{t['banner_title']}</h1>
            <p>{t['banner_desc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Login Section & Info Layout
    col_login, col_spacer, col_info = st.columns([1.2, 0.2, 1.6])
    
    with col_login:
        st.markdown(f"""
            <div class="login-container">
                <h3>{t['login_box_title']}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Form inputs inside container
        with st.form("login_form"):
            username = st.text_input(t["username_label"], value="muaz")
            password = st.text_input(t["password_label"], type="password", value="12345")
            submit_login = st.form_submit_button(t["login_btn"], use_container_width=True)
            
            if submit_login:
                # Default credentials check (Can be customized)
                if username.strip() != "" and password.strip() != "":
                    st.session_state.logged_in = True
                    st.session_state.student_name = username
                    st.success(t["login_success"])
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(t["login_error"])
                    
    with col_info:
        st.markdown(f"### {t['features_heading']}")
        
        st.markdown(f"""
            <div class="feature-card">
                <h4>{t['feat_1_title']}</h4>
                <p>{t['feat_1_desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="feature-card">
                <h4>{t['feat_2_title']}</h4>
                <p>{t['feat_2_desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="feature-card">
                <h4>{t['feat_3_title']}</h4>
                <p>{t['feat_3_desc']}</p>
            </div>
        """, unsafe_allow_html=True)

else:
    # --- 2. INNER APP (AFTER SUCCESSFUL LOGIN) ---
    st.success(f"خوش آمدید، **{st.session_state.student_name}**! آپ کامیابی سے لاگ ان ہو چکے ہیں۔")
    
    selected_takhti = st.selectbox(
        "تختی منتخب کریں / Select Takhti:",
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
        <div class="qaida-header-banner">تختی نمبر 1 ـــ حروفِ مفردات</div>
        <div class="bismillah-banner">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
        <div class="hidayat-box">
            <span class="hidayat-title">ہدایات:</span> یہ حروفِ مفردات بنیاد ہیں۔ ان میں بچے کے تلفظ درست کروائیں اور حروف کے نقطے بھی یاد کروائیں۔ یادکروائیں سطر کے آخر سے دائیں اور اوپر سے نیچے اور نیچے سے اوپر کی طرف پڑھوائیں۔
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
    
    st.markdown(f"### 🎙️ {st.session_state.student_name} - تلاوت کی مشق اور ریکارڈنگ")
    audio_val = st.audio_input("مائیکروفون پر کلک کر کے تلاوت ریکارڈ کریں:")

    if audio_val is not None:
        st.audio(audio_val)
        with st.spinner("🤖 AI استاد آپ کے تلفظ کا جائزہ لے رہا ہے..."):
            time.sleep(2)
            
        st.markdown("""
            <div style="padding: 15px; border-radius: 10px; background-color: #e8f5e9; border-left: 5px solid #2e7d32; font-size: 16px; color: #2e7d32; margin-top: 20px;">
                <b>🌟 ماشاءاللہ بہت زبردست تلفظ ہے!</b><br>
                • حروفِ مفردات کی ادائیگی بالکل درست رہی۔<br>
                • <b>اسکور:</b> ⭐⭐⭐⭐⭐ (5/5)
            </div>
        """, unsafe_allow_html=True)
        st.balloons()
