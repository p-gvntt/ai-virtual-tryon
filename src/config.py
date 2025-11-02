import os
from dotenv import load_dotenv

# Base directories
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_INPUT_DIR = os.path.join(DATA_DIR, "model_input")
OUTFIT_DIR = os.path.join(DATA_DIR, "outfit_tryon")
OUTPUT_DIR = os.path.join(DATA_DIR, "virtual_tryon_output")

# Output files
FINAL_OUTPUT = os.path.join(OUTPUT_DIR, "final_tryon.png")

# Environment
load_dotenv(os.path.join(BASE_DIR, ".env"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

if not OPENAI_API_KEY or not REPLICATE_API_TOKEN:
    raise ValueError("Please set OPENAI_API_KEY and REPLICATE_API_TOKEN in your .env file")

# Ensure directories exist
for path in [MODEL_INPUT_DIR, OUTFIT_DIR, OUTPUT_DIR]:
    os.makedirs(path, exist_ok=True)