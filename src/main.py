import os
from pathlib import Path
from .config import MODEL_INPUT_DIR, OUTFIT_DIR, OUTPUT_DIR, FINAL_OUTPUT
from .utils import add_white_background, CATEGORY_MAPPING
from .services import analyze_outfit, run_replicate

def get_model_image():
    candidates = list(Path(MODEL_INPUT_DIR).glob("*.[pj][pn]g")) + list(Path(MODEL_INPUT_DIR).glob("*.webp"))
    if candidates:
        return candidates[0]
    raise FileNotFoundError("No model image found in model_input/")

def run_vton():
    outfit_files = list(Path(OUTFIT_DIR).glob("*.[pj][pn]g")) + list(Path(OUTFIT_DIR).glob("*.webp"))
    if not outfit_files:
        raise FileNotFoundError("No outfit images found in outfit_tryon/")

    model_img = get_model_image()
    final_data = None

    for outfit in outfit_files:
        print(f"Processing {outfit.name}...")
        info = analyze_outfit(outfit)
        if not info:
            continue

        raw_cat = info.get("category", "").strip()
        mapped_cat = CATEGORY_MAPPING.get(raw_cat)
        if not mapped_cat:
            print(f"Skipping {outfit.name}: category '{raw_cat}' not mapped")
            continue

        desc = info.get("description", f"A stylish {mapped_cat.replace('_',' ')} garment")
        outfit_buf = add_white_background(outfit)

        with open(model_img, "rb") as mfile:
            data = run_replicate(mfile, outfit_buf, mapped_cat, desc)
            if data:
                final_data = data

    if final_data:
        with open(FINAL_OUTPUT, "wb") as f:
            f.write(final_data)
        print(f"Saved final output into virtual_tryon_output/final_tryon.png")
    else:
        print("No valid output generated.")

# Run the function
if __name__ == "__main__":
    run_vton()
