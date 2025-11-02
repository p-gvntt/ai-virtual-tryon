import io
from pathlib import Path
from PIL import Image

CATEGORY_MAPPING = {
    "Dresses": "dresses", "Gowns": "dresses", "Dress": "dresses",
    "Tops": "upper_body", "Top": "upper_body", "Blouses": "upper_body", "Blouse": "upper_body", "Shirts": "upper_body", "Shirt": "upper_body",
    "Jumpers": "upper_body", "Jumper": "upper_body", "Jackets": "upper_body", "Jacket": "upper_body", "Coats": "upper_body", "Coat": "upper_body",
    "Sweaters": "upper_body", "Sweater": "upper_body", "Outerwear": "upper_body", "Hoodies": "upper_body", "Hoodie": "upper_body",
    "Cardigans": "upper_body", "Cardigan": "upper_body",
    "Jeans": "lower_body", "Jean": "lower_body", "Skirts": "lower_body", "Skirt": "lower_body", "Pants": "lower_body", "Pant": "lower_body",
    "Trousers": "lower_body", "Trouser": "lower_body", "Shorts": "lower_body", "Short": "lower_body", "Bottoms": "lower_body",
    "T-Shirts": "upper_body", "T-Shirt": "upper_body", "Polos": "upper_body", "Polo": "upper_body", "Sweatshirts": "upper_body", "Sweatshirt": "upper_body",
    "Shirts (Men)": "upper_body", "Blazers": "upper_body", "Blazer": "upper_body", "Coats (Men)": "upper_body",
    "Jackets (Men)": "upper_body", "Hoodies (Men)": "upper_body", "Sweaters (Men)": "upper_body",
    "Jeans (Men)": "lower_body", "Chinos": "lower_body", "Chino": "lower_body", "Shorts (Men)": "lower_body",
    "Trousers (Men)": "lower_body", "Cargo Pants": "lower_body",
    "Bags": None, "Shoes": None, "Sandals": None, "Boots": None,
    "Hats": None, "Caps": None, "Socks": None,
    "Bracelets": None, "Earrings": None, "Necklaces": None, "Rings": None,
    "Scarves": None, "Belts": None, "Gloves": None,
}

def add_white_background(image_path: Path) -> io.BytesIO:
    try:
        with Image.open(image_path) as img:
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                bg = Image.new('RGB', img.size, (255, 255, 255))
                mask = img.split()[-1] if 'A' in img.getbands() else None
                bg.paste(img, mask=mask)
                buffer = io.BytesIO()
                bg.save(buffer, format='PNG')
            else:
                buffer = io.BytesIO()
                img.save(buffer, format='PNG')
        buffer.seek(0)
        return buffer
    except Exception as e:
        print(f"Failed to process image background: {e}")
        with open(image_path, "rb") as f:
            return io.BytesIO(f.read())