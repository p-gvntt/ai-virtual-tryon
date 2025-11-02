# Streamlit app for virtual try-on
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import streamlit as st
from src.main import run_vton
from src.config import MODEL_INPUT_DIR, OUTFIT_DIR, OUTPUT_DIR, FINAL_OUTPUT

# Page config
st.set_page_config(
    page_title="AI Virtual Try-On Studio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS styling
st.markdown("""
<style>
/* Main container background */
.css-18e3th9 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
}

/* Title */
.title-container {
    text-align: center;
    margin-bottom: 2rem;
}
.main-title {
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(120deg, #ffffff 0%, #e0e7ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin-bottom: 0.5rem;
}
.subtitle {
    color: #e0e7ff;
    font-size: 1.2rem;
    font-weight: 300;
}

/* Upload card */
.upload-card {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 1rem 1rem 2rem 1rem;
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    margin-bottom: 2rem;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Section header */
.section-header {
    font-size: 1.5rem;
    font-weight: 700;
    color: #667eea;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.section-header::before {
    content: "✨";
    font-size: 1.8rem;
}

/* File uploader styling */
[data-testid="stFileUploader"] {
    border: 2px dashed #667eea;
    border-radius: 10px;
    padding: 1rem;
    background: rgba(102, 126, 234, 0.05);
}

[data-testid="stFileUploader"]:hover {
    background: rgba(102, 126, 234, 0.1);
    border-color: #764ba2;
}

/* Images in upload cards */
.upload-card img {
    width: 100% !important;
    height: auto !important;
    object-fit: contain;
    border-radius: 10px;
}

/* Result card */
.result-card {
    background: rgba(255, 255, 255, 0.98);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 20px 60px rgba(0,0,0,0.35);
    border: 2px solid rgba(255,255,255,0.3);
}

/* Buttons */
button.stButton>button {
    width: 100%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 1rem 2rem;
    font-size: 1.2rem;
    font-weight: 600;
    border-radius: 50px;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    transition: all 0.3s ease;
    margin-top: 1rem;
}
button.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
}

/* Info box */
.info-box {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    padding: 1.5rem;
    border-radius: 15px;
    margin: 1rem 0;
    box-shadow: 0 10px 30px rgba(240, 147, 251, 0.3);
}

/* Divider */
.divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #667eea, transparent);
    margin: 2rem 0;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="title-container">
    <h1 class="main-title">AI Virtual Try-On Studio</h1>
    <p class="subtitle">Transform your fashion experience with AI-powered virtual fitting</p>
</div>
""", unsafe_allow_html=True)

# Upload columns
col1, col2 = st.columns(2, gap="large")

# Model Upload
with col1:
    st.markdown('<div class="section-header">Model Image</div>', unsafe_allow_html=True)
    
    model_file = st.file_uploader(
        "Choose model image",
        type=["png", "jpg", "jpeg", "webp"],
        key="model",
        label_visibility="collapsed"
    )
    
    if model_file:
        model_path = Path(MODEL_INPUT_DIR) / model_file.name
        model_path.write_bytes(model_file.getbuffer())
        st.image(model_file, use_container_width=True)

# Outfit Upload
with col2:
    st.markdown('<div class="section-header">Outfit Image</div>', unsafe_allow_html=True)
    
    outfit_file = st.file_uploader(
        "Choose outfit image",
        type=["png", "jpg", "jpeg", "webp"],
        key="outfit",
        label_visibility="collapsed"
    )
    
    if outfit_file:
        outfit_path = Path(OUTFIT_DIR) / outfit_file.name
        outfit_path.write_bytes(outfit_file.getbuffer())
        st.image(outfit_file, use_container_width=True)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Generate button
col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])
with col_btn2:
    generate_btn = st.button("🎨 Generate Virtual Try-On", use_container_width=True)

# Processing
if generate_btn:
    if not model_file or not outfit_file:
        st.warning("⚠️ Please upload both a model image and an outfit image to continue.")
    else:
        with st.spinner("✨ AI is working its magic... This may take a moment."):
            try:
                run_vton()
                
                if Path(FINAL_OUTPUT).exists():
                    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
                    st.markdown('<div class="result-card">', unsafe_allow_html=True)
                    st.markdown('<div class="section-header">Your Virtual Try-On Result</div>', unsafe_allow_html=True)
                    
                    # Result columns
                    result_col1, result_col2, result_col3 = st.columns(3)
                    with result_col1:
                        st.markdown("**Original Model**")
                        st.image(model_file, use_container_width=True)
                    with result_col2:
                        st.markdown("**Outfit**")
                        st.image(outfit_file, use_container_width=True)
                    with result_col3:
                        st.markdown("**Final Result**")
                        st.image(FINAL_OUTPUT, use_container_width=True)
                    
                    st.success("🎉 Try-on generated successfully!")
                    st.info(f"💾 Output saved to /virtual_tryon_output/final_tryon.png")
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.error("❌ No output generated. Please check the logs for errors.")
            except Exception as e:
                st.error(f"❌ Error during processing: {e}")

# Footer info
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
    <strong>💡 Tips for best results:</strong><br>
    • Use clear, well-lit photos with the person facing forward<br>
    • Outfit images should be on a plain background<br>
    • Higher resolution images produce better results<br>
    • Processing typically takes 30-60 seconds
</div>
""", unsafe_allow_html=True)