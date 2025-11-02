import json, re, requests
from openai import OpenAI
import replicate
from .config import OPENAI_API_KEY, REPLICATE_API_TOKEN
from .utils import CATEGORY_MAPPING

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_outfit(image_path):
    try:
        with open(image_path, "rb") as f:
            img_base64 = f.read()

        valid_categories = [cat for cat in CATEGORY_MAPPING.keys() if CATEGORY_MAPPING[cat] is not None]
        categories_str = ", ".join(valid_categories)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are a fashion AI. Given an outfit image, return ONLY a single JSON object with keys: product_name, category, description. The category MUST be one of these exact values: {categories_str}. Skip accessories like hats, shoes, scarves, bags, jewelry. Return only ONE item."},
                {"role": "user", "content": [{"type": "text", "text": "Describe the main clothing item in this image."}, {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{__import__('base64').b64encode(img_base64).decode()}"}}]},
            ],
            temperature=0
        )

        raw_text = response.choices[0].message.content.strip()
        match = re.search(r"\{[^{}]*\}", raw_text)
        if not match:
            return None
        return json.loads(match.group(0))
    except Exception as e:
        print(f"Analyze failed: {e}")
        return None


def run_replicate(model_image, outfit_path, category, description):
    try:
        result = replicate.run(
            "cuuupid/idm-vton:0513734a452173b8173e907e3a59d19a36266e55b48528559432bd21c7d7e985",
            input={
                "crop": False,
                "seed": 42,
                "steps": 30,
                "category": category,
                "force_dc": False,
                "garm_img": outfit_path,
                "human_img": model_image,
                "mask_only": False,
                "garment_des": description,
            }
        )
        url = result[0] if isinstance(result, list) else result
        return requests.get(url).content
    except Exception as e:
        print(f"Replicate model failed: {e}")
        return None