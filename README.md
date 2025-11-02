# 👗 AI Virtual Try-On

A smart virtual try-on application that allows users to upload a personal photo and a clothing item image to see how the outfit would look on them. Powered by OpenAI GPT and Replicate's IDM-VTON model.

## ✨ Features

- **Single Outfit Swap**: Only one garment can be swapped at a time to maintain realism.  
- **Smart Outfit Analysis**: Uses GPT to analyze the uploaded clothing item and detect the main garment.  
- **Virtual Try-On**: Uses Replicate's IDM-VTON model to generate a realistic try-on image.  
- **Interactive Web App**: Upload model and outfit images via Streamlit, generate virtual try-ons repeatedly.  
- **Notebook Demo**: Run Jupyter notebooks to test the pipeline locally and explore outputs.  
- **Local Storage**: Saves uploaded images, model images, outfits, and final outputs in organized folders.  

## 🚀 Quick Start

### Prerequisites

- Python 3.8+  
- ~1-2GB free disk space for generated images  
- OpenAI API key (`OPENAI_API_KEY`)  
- Replicate API token (`REPLICATE_API_TOKEN`)  

> ⚠️ **Important:** The Replicate IDM-VTON model is **not for commercial use**. Follow the license terms at [Replicate](https://replicate.com/).

---

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-virtual-tryon.git
cd ai-virtual-tryon
```

2. **Create a virtual environment**
```bash
python3 -m venv .venv
```

3. **Activate the virtual environment**

macOS / Linux:
```bash
python3 -m venv .venv
```

Windows (CMD):
```bash
source .venv/bin/activate
```

4. **Upgrade pip (recommended)**
```bash
pip install --upgrade pip
```

5. **Install dependencies**
```bash
pip install -r requirements.txt
```

6. **Set up environment variables**

Create a `.env` file in the project root with:
```
OPENAI_API_KEY=your_openai_api_key
REPLICATE_API_TOKEN=your_replicate_token
```

7. **Prepare folder structure**
```
data/
├── model_input/             # Place one model image (user photo) here
├── outfit_tryon/            # Place the outfit image here (one at a time)
└── virtual_tryon_output/    # Generated outputs will be saved here
```

All folders contain a `.gitkeep` placeholder for Git tracking.

---

## Running the App

### Streamlit Web App:
```bash
streamlit run app/app.py
```

- Upload a model image and an outfit image.
- Click Generate Try-On to produce a virtual try-on image.
- Images are saved locally in `data/virtual_tryon_output/final_tryon.png`.

### Jupyter Notebook Demo:
```bash
jupyter notebook notebooks/demo_tryon.ipynb
```

- Select which model and outfit images to test.
- The notebook runs the same pipeline and displays the generated output.

---

## 📁 Project Structure
```
ai-virtual-try-on/
├── app/
│   └── app.py                   # Streamlit web app
├── data/
│   ├── model_input/             # User model images
│   ├── outfit_tryon/            # Outfit images for try-on
│   └── virtual_tryon_output/    # Generated try-on outputs
├── notebooks/
│   └── demo_tryon.ipynb         # Interactive demo notebook
├── src/
│   ├── __init__.py
│   ├── config.py                # Configuration and paths
│   ├── utils.py                 # Helper functions & category mapping
│   ├── services.py              # GPT & Replicate calls
│   └── main.py                  # Run virtual try-on pipeline
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (API keys)
├── .gitignore                   # Git ignore rules
└── README.md                    # Project documentation
```

---

## 🔧 How It Works

1. **Model & Outfit Upload**: Users upload their photo and a single clothing image.
2. **Outfit Analysis**: GPT extracts the main garment category and description.
3. **Background Processing**: Converts outfit to a consistent white background for better try-on results.
4. **Virtual Try-On**: Replicate IDM-VTON model generates the combined image.
5. **Output Storage**: Final image saved locally and displayed to the user.

---

## 💻 Usage Examples

### Streamlit App
```bash
# Launch Streamlit app
streamlit run app/app.py

# Then upload:
# - Model image: a photo of yourself
# - Outfit image: the clothing item you want to try on
```

### Notebook Demo
```bash
# Run the demo pipeline interactively
jupyter notebook notebooks/demo_tryon.ipynb
```

---

## 🎯 Key Components

### Smart Outfit Mapping

- Only the main garment is considered (skip accessories like shoes, bags, hats).
- Categories mapped internally via `CATEGORY_MAPPING` in `utils.py`.

### Virtual Try-On Pipeline

- `analyze_outfit()` → GPT classification of garment
- `add_white_background()` → ensures consistent input for VTON
- `run_replicate()` → calls IDM-VTON model for final output

---

## ⚠️ Disclaimer

- The IDM-VTON model from Replicate is **not for commercial use**.
- Always respect the model license: [Replicate License](https://replicate.com/).
- Generated outputs are for personal or educational use only.

---

## 🙏 Acknowledgments

- GPT and Replicate IDM-VTON for AI-powered try-on

---

**Ora divertiti a provare nuovi vestiti 😊**