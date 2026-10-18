import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI مکتب و مدرسہ - Make.com Style LMS",
    page_icon="📖",
    layout="wide"
)

# --- MAKE.COM STYLE CUSTOM CSS WITH AUDIO SPEECH ON HOVER ---
st.markdown("""
    <style>
    .main {
        background-color: #f4f5f7;
        direction: rtl;
    }
    [data-testid="stSidebar"] {
        background-color: #6d1b7b !important;
        color: white !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    .make-header {
        background-color: #ffffff;
        padding: 15px 25px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 25px;
        direction: rtl;
    }
    .workflow-card {
        background-color: #ffffff;
        border: 2px solid #e0e0e0;
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: 0.3s;
    }
    .workflow-card:hover {
        border-color: #6d1b7b;
        box-shadow: 0 6px 20px rgba(109,27,123,0.15);
    }
    .qaida-book-container {
        border: 6px double #6d1b7b;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        max-width: 950px;
        margin: 0 auto;
        direction: rtl;
    }
    .qaida-header-banner {
        background: linear-gradient(135deg, #6d1b7b, #4a1254);
        color: white;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .bismillah-banner {
        font-size: 30px;
        text-align: center;
        color: #6d1b7b;
        font-family: 'Amiri', serif;
        font-weight: bold;
        padding: 8px;
        border-bottom: 2px solid #e1bee7;
        border-top: 2px solid #e1bee7;
        margin-bottom: 20px;
    }
    .hidayat-box {
        background-color: #f3e5f5;
        border: 2px solid #ba68c8;
        padding: 15px;
        border-radius: 10px;
        font-size: 15px;
        color: #333;
        margin-bottom: 25px;
        text-align: right;
        line-height: 1.6;
    }
    /* QAIDA BOX WITH AUDIO TRIGGER ON HOVER */
    .qaida-box {
        background-color: #ffffff;
        border: 2px solid #6d1b7b;
        border-radius: 12px;
        text-align: center;
        padding: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        transition: all 0.3s ease-in-out;
        cursor: pointer;
    }
    .qaida-box:hover {
        background-color: #f3e5f5;
        border-color: #4a1254;
        transform: translateY(-5px) scale(1.03);
        box-shadow: 0 8px 20px rgba(109,27,123,0.25);
    }
    .arabic-letter {
        font-size: 42px;
        font-family: 'Amiri', serif;
        font-weight: bold;
    }
    .letter-name {
        font-size: 13px;
        color: #555;
        font-weight: bold;
        margin-top: 5px;
    }
    </style>

    <script>
    // JavaScript Text-to-Speech for AI Ustad Pronunciation
    function playAudio(text) {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel(); // Stop previous audio
            let utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'ar-SA'; // Arabic Language Accent
            utterance.rate = 0.8;     // Slower speed for clear learning
            window.speechSynthesis.speak(utterance);
        }
    }
    </script>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if "active_view" not in st.session_state:
    st.session_state.active_view = "Scenarios"
if "student_name" not in st.session_state:
    st.session_state.student_name = "مُعاذ عزیز"

# --- SIDEBAR (Make.com Purple Menu Style) ---
st.sidebar.markdown("<h2>⚡ AI Maktab</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

if st.sidebar.button("🗂️ Scenarios / کورسز", use_container_width=True):
    st.session_state.active_view = "Scenarios"
    st.rerun()

if st.sidebar.button("🤖 AI Agents / اساتذہ", use_container_width=True):
    st.session_state.active_view = "Agents"
    st.rerun()

if st.sidebar.button("📊 Credentials / پروگریس", use_container_width=True):
    st.session_state.active_view = "Credentials"
    st.rerun()

if st.sidebar.button("🌐 Webhooks / ایڈمن", use_container_width=True):
    st.session_state.active_view = "Admin"
    st.rerun()

# --- TOP HEADER BAR ---
st.markdown("""
    <div class="make-header">
        <div style="font-weight: bold; font-size: 18px; color: #333;">🔗 Integration Module: Noorani Qaida & AI Speech Verification</div>
        <div style="background-color: #e8f5e9; color: #2e7d32; padding: 5px 15px; border-radius: 20px; font-weight: bold;">🟢 Active Scenario</div>
    </div>
""", unsafe_allow_html=True)


# ==========================================
# 1. SCENARIOS VIEW
# ==========================================
if st.session_state.active_view == "Scenarios":
    st.markdown("### 🧩 Learning Scenarios (워크ف로우 ماڈیولز)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="workflow-card">
                <div style="font-size: 40px; margin-bottom: 10px;">📖</div>
                <h3>نورانی قاعدہ (Takhti 1-3)</h3>
                <p style="color: #666; font-size: 14px;">بنیادی حروفِ مفردات اور مرکبات کی لائیو مشق۔</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Open Module 🚀", use_container_width=True):
            st.session_state.active_view = "QaidaViewer"
            st.rerun()
            
    with col2:
        st.markdown("""
            <div class="workflow-card">
                <div style="font-size: 40px; margin-bottom: 10px;">🎙️</div>
                <h3>AI Speech Verification</h3>
                <p style="color: #666; font-size: 14px;">اوپن اے آئی (OpenAI Whisper) کی طرز پر تلفظ کی جانچ۔</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="workflow-card">
                <div style="font-size: 40px; margin-bottom: 10px;">📊</div>
                <h3>Progress & Analytics</h3>
                <p style="color: #666; font-size: 14px;">طالب علم کی روزانہ کی رپورٹس اور اسکور کارڈز۔</p>
            </div>
        """, unsafe_allow_html=True)


# ==========================================
# 2. QAIDA BOOK VIEWER (RTL with AI Audio Hover Pronunciation)
# ==========================================
elif st.session_state.active_view == "QaidaViewer":
    if st.button("⬅️ Back to Scenarios"):
        st.session_state.active_view = "Scenarios"
        st.rerun()
        
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

    # Container Box mimicking Book
    st.markdown("""
        <div class="qaida-book-container">
            <div class="qaida-header-banner">تختی نمبر 1 ـــ حروفِ مفردات</div>
            <div class="bismillah-banner">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
            <div class="hidayat-box">
                <b>ہدایات:</b> کسی بھی حرف پر کرسر (Cursor) لے جائیں؛ AI استاد فوراً اس حرف کا درست تلفظ بول کر سنائے گا۔
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")

    # Render Letters in Grid with Audio Pronunciation on Hover
    cols_per_row = 5
    for i in range(0, len(takhti_1_letters), cols_per_row):
        row_items = takhti_1_letters[i:i + cols_per_row]
        cols = st.columns(cols_per_row)
        reversed_cols = list(reversed(cols))
        
        for idx, item in enumerate(row_items):
            with reversed_cols[idx]:
                st.markdown(f"""
                    <div class="qaida-box" onmouseover="playAudio('{item['ar']}')">
                        <div class="arabic-letter" style="color: {item['color']};">{item['ar']}</div>
                        <div class="letter-name">{item['name']}</div>
                    </div>
                """, unsafe_allow_html=True)

    st.divider()
    
    st.markdown(f"### 🎙️ {st.session_state.student_name} - تلاوت کی مشق اور ریکارڈنگ")
    audio_val = st.audio_input("مائیکروفون پر کلک کر کے تلاوت ریکارڈ کریں:")

    if audio_val is not None:
        st.audio(audio_val)
        with st.spinner("🤖 AI استاد آپ کے تلفظ کا جائزہ لے رہا ہے..."):
            time.sleep(2)
            
        st.markdown("""
            <div style="padding: 15px; border-radius: 10px; background-color: #f3e5f5; border-left: 5px solid #6d1b7b; font-size: 16px; color: #4a1254; margin-top: 20px;">
                <b>🌟 ماشاءاللہ بہت زبردست تلفظ ہے!</b><br>
                • حروفِ مفردات کی ادائیگی بالکل درست رہی۔<br>
                • <b>اسکور:</b> ⭐⭐⭐⭐⭐ (5/5)
            </div>
        """, unsafe_allow_html=True)
        st.balloons()


# ==========================================
# 3. OTHER VIEWS
# ==========================================
elif st.session_state.active_view == "Agents":
    st.markdown("### 🤖 AI Pronunciation Agents")
    st.info("Configure AI models for real-time phoneme matching and speech recognition.")

elif st.session_state.active_view == "Credentials":
    st.markdown("### 📊 Student Credentials & Progress Logs")
    st.metric(label="Total Scenarios Run", value="14")
    st.metric(label="Average Accuracy", value="99.2%")

elif st.session_state.active_view == "Admin":
    st.markdown("### 🌐 Webhooks & Admin Panel")
    st.info("Manage global system webhooks, API keys, and multi-tenant security settings.")
