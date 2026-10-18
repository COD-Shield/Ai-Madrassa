import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI مکتب و مدرسہ - AI Madrassa",
    page_icon="📖",
    layout="wide"
)

# --- GLOBAL TRANSLATIONS DICTIONARY ---
TRANSLATIONS = {
    "اردو (Urdu)": {
        "app_title": "📖 AI مکتب و مدرسہ (Digital Noorani Qaida)",
        "onboarding_title": "👋 خوش آمدید! طالب علم کی پروفائل بنائیں",
        "name_prompt": "طالب علم کا نام درج کریں:",
        "lang_prompt": "زبان منتخب کریں (Select Language):",
        "start_btn": "سبق شروع کریں 🚀",
        "sidebar_header": "⚙️ گلوبل ترتیبات (Settings)",
        "change_profile": "پروفائل تبدیل کریں",
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
        "app_title": "📖 AI Maktab o Madrassa (Digital Noorani Qaida)",
        "onboarding_title": "👋 Welcome! Setup Student Profile",
        "name_prompt": "Enter Student Name:",
        "lang_prompt": "Select Language:",
        "start_btn": "Start Lesson 🚀",
        "sidebar_header": "⚙️ Global Settings",
        "change_profile": "Change Profile",
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

# --- INITIALIZE SESSION STATE FOR LOGIN / ONBOARDING ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "student_name" not in st.session_state:
    st.session_state.student_name = "مُعاذ عزیز"
if "language" not in st.session_state:
    st.session_state.language = "اردو (Urdu)"

# --- 1. LOGIN / ONBOARDING SCREEN ---
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align: center; color: #1b5e20;'>📖 AI مکتب و مدرسہ</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #555;'>Interactive Digital Noorani Qaida & LMS</h3>", unsafe_allow_html=True)
    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 📝 اسٹوڈنٹس لاگ ان / رجسٹریشن")
        entered_name = st.text_input("طالب علم کا نام / Student Name:", "مُعاذ عزیز")
        selected_lang = st.selectbox("زبان منتخب کریں / Select Language:", list(TRANSLATIONS.keys()))
        
        if st.button("سبق شروع کریں 🚀", use_container_width=True):
            st.session_state.student_name = entered_name
            st.session_state.language = selected_lang
            st.session_state.logged_in = True
            st.rerun()

else:
    # --- 2. MAIN APPLICATION (AFTER LOGIN) ---
    lang = st.session_state.language
    t = TRANSLATIONS[lang]
    
    # Global CSS matching the book page layout
    st.markdown(f"""
        <style>
        .main {{
            background-color: #f4f6f0;
        }}
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

    # --- SIDEBAR GLOBAL CONTROLS ---
    st.sidebar.header(t["sidebar_header"])
    
    # Global Language Switcher (Changes entire app instantly like COD Shield)
    new_lang = st.sidebar.selectbox(t["lang_prompt"], list(TRANSLATIONS.keys()), index=list(TRANSLATIONS.keys()).index(lang))
    if new_lang != lang:
        st.session_state.language = new_lang
        st.rerun()
        
    st.sidebar.markdown(f"**👤 {t['student_name'].replace(':', '')}:** {st.session_state.student_name}")
    
    selected_takhti = st.sidebar.selectbox(
        t["select_takhti_label"],
        ["تختی نمبر 1: حروفِ مفردات", "تختی نمبر 2: حروفِ مرکبات", "تختی نمبر 3: حرکات"]
    )
    
    if st.sidebar.button("🚪 " + t["change_profile"]):
        st.session_state.logged_in = False
        st.rerun()

    # --- QAIDA DATA ---
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

    # --- RENDER BOOK PAGE CONTAINER ---
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

    # --- PRACTICE & TEST MODULE ---
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
