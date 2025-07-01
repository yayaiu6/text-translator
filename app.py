import streamlit as st
from googletrans import Translator, LANGUAGES
import time

# Page configuration
st.set_page_config(page_title="Text Translator", page_icon="🌐", layout="wide")

# Initialize translator and session state
if 'translator' not in st.session_state:
    st.session_state.translator = Translator()
if 'translated_text' not in st.session_state:
    st.session_state.translated_text = ""

translator = st.session_state.translator

# Main title
st.title("🌐 Text Translator")
st.markdown("---")

# Create columns for layout
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    st.subheader("Source Text")
    source_languages = {'auto': 'Auto Detect'}
    source_languages.update(LANGUAGES)
    source_lang = st.selectbox("Select Source Language:", options=list(source_languages.keys()),
                              format_func=lambda x: source_languages[x].title() if x != 'auto' else source_languages[x], index=0)
    source_text = st.text_area("Enter text to translate:", height=100, placeholder="Enter text here...")

with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    translate_button = st.button("Translate ➡️", type="primary", use_container_width=True)

with col3:
    st.subheader("Translated Text")
    target_languages = {k: v for k, v in LANGUAGES.items() if k != 'auto'}
    target_lang = st.selectbox("Select Target Language:", options=list(target_languages.keys()),
                              format_func=lambda x: target_languages[x].title(),
                              index=list(target_languages.keys()).index('en') if 'en' in target_languages else 0)
    # تحديث النص المترجم مباشرة من الحالة
    translated_text = st.session_state.translated_text
    translated_text_area = st.text_area("Translated Text:", value=translated_text, height=100, disabled=True)

# Handle translation
if translate_button and source_text.strip():
    try:
        with st.spinner('Translating...'):
            result = translator.translate(source_text, src=source_lang if source_lang != 'auto' else 'auto', dest=target_lang)
            st.session_state.translated_text = result.text
            st.experimental_rerun()  # إعادة تشغيل فوري لتحديث الواجهة
    except Exception as e:
        st.error(f"Translation error: {str(e)}. Check your internet connection and try again.")
elif translate_button and not source_text.strip():
    st.warning("Please enter text to translate")

# Text statistics
if source_text:
    col_stats1, col_stats2, col_stats3 = st.columns(3)
    with col_stats1:
        st.metric("Character Count", len(source_text))
    with col_stats2:
        st.metric("Word Count", len(source_text.split()))
    with col_stats3:
        if st.session_state.translated_text:
            st.metric("Translated Text Length", len(st.session_state.translated_text))



# Project credits
st.markdown("---")
st.markdown("""
### About the Project
This Text Translator application was developed as a research project to facilitate seamless multilingual communication. Built with Streamlit and powered by Google Translate, it offers an intuitive interface for translating text across numerous languages.

#### Developed By
<div style='display: flex; gap: 20px; flex-wrap: wrap; padding: 15px; background-color: #f8f9fa; border-radius: 10px;'>
    <div style='display: flex; align-items: center; gap: 10px;'>
        <span style='font-size: 1.2em;'>👤</span>
        <div>
            <strong style='color: #1a1a1a;'>Shahd Elmaghawry</strong><br>
            <a href='https://www.linkedin.com/in/shahd-elmaghawry-066923307/' target='_blank' style='color: #0a66c2; text-decoration: none;'>LinkedIn Profile</a>
        </div>
    </div>
    <div style='display: flex; align-items: center; gap: 10px;'>
        <span style='font-size: 1.2em;'>👤</span>
        <div>
            <strong style='color: #1a1a1a;'>Yahya Mahrouf</strong><br>
            <a href='https://www.linkedin.com/in/yahya-mahrouf/' target='_blank' style='color: #0a66c2; text-decoration: none;'>LinkedIn Profile</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
    .stButton > button { 
        width: 100%; 
        margin-top: 10px; 
    }
    .metric-container { 
        background-color: #f0f2f6; 
        padding: 10px; 
        border-radius: 10px; 
        text-align: center; 
    }
    .stTextArea > div > div > textarea { 
        font-family: 'Arial', sans-serif; 
        font-size: 14px; 
        resize: none; 
    }
    [data-theme='dark'] div[data-testid="stMarkdownContainer"] strong {
        color: #ffffff !important;
    }
    [data-theme='dark'] div[data-testid="stMarkdownContainer"] a {
        color: #66b3ff !important;
    }
    [data-theme='dark'] div[style*="background-color: #f8f9fa"] {
        background-color: #2c2f33 !important;
    }
    @media (max-width: 600px) {
        .stTextArea > div > div > textarea { 
            height: 80px !important; 
            font-size: 12px; 
        }
        .stColumn > div { 
            padding: 5px; 
        }
        div[data-testid="stMarkdownContainer"] > div[style*="flex-wrap"] { 
            flex-direction: column; 
            padding: 10px; 
        }
    }
</style>
""", unsafe_allow_html=True)
