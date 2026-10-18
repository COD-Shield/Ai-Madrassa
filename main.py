import streamlit as st

# 1. زبانوں کی ڈکشنری (Translations Dictionary)
translations = {
    "اردو (Urdu)": {
        "title": "تختی نمبر 1 ـــ حروفِ مفردات",
        "hidayat": "ہدایات: یہ حروفِ مفردات بنیاد ہیں۔ ان میں بچے کے تلفظ درست کروائیں اور حروف کے نقطے بھی یاد کروائیں۔",
        "settings": "ترتیبات / Settings",
        "name_label": "طالب علم کا نام:",
        "dir": "rtl"
    },
    "English": {
        "title": "Lesson No. 1 - Basic Alphabets",
        "hidayat": "Instruction: These are basic alphabets. Practice correct pronunciation and letter points.",
        "settings": "Settings",
        "name_label": "Student Name:",
        "dir": "ltr"
    },
    "العربية (Arabic)": {
        "title": "الدرس الأول - حروف الهجاء",
        "hidayat": "تعليمات: هذه الحروف المفردة هي الأساس. تدرب على النطق الصحيح.",
        "settings": "الإعدادات",
        "name_label": "اسم الطالب:",
        "dir": "rtl"
    }
}

# 2. سائیڈ بار میں زبان منتخب کرنے کا مینو
st.sidebar.header("⚙️ Language / زبان")
selected_lang = st.sidebar.selectbox("Select Language:", list(translations.keys()))

# 3. منتخب کردہ زبان کا ڈیٹا حاصل کرنا
t = translations[selected_lang]

# 4. ایپ میں استعمال کرنا (جہاں جو زبان سلیکٹ ہوگی، وہی متن آئے گا)
st.markdown(f"""
    <div style="direction: {t['dir']};">
        <h2>{t['title']}</h2>
        <p>{t['hidayat']}</p>
    </div>
""", unsafe_allow_html=True)
