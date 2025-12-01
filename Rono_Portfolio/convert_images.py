import os
from PIL import Image

def convert_to_webp(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                file_name, file_ext = os.path.splitext(file_path)
                webp_path = f"{file_name}.webp"
                
                try:
                    with Image.open(file_path) as img:
                        img.save(webp_path, 'WEBP', quality=80)
                        print(f"Converted: {file_path} -> {webp_path}")
                except Exception as e:
                    print(f"Error converting {file_path}: {e}")

if __name__ == "__main__":
    assets_dir = os.path.join(os.getcwd(), "assets", "imgs")
    if os.path.exists(assets_dir):
        print(f"Starting conversion in {assets_dir}...")
        convert_to_webp(assets_dir)
        print("Conversion complete.")
    else:
        print(f"Directory not found: {assets_dir}")
