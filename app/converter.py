import os
from PIL import Image

def convert_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, 'webp')
            print(f"Converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def batch_convert(input_dir, output_dir):
    supported_formats = ('.png', '.jpg', '.jpeg')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_dir, output_filename)
            convert_image(input_path, output_path)
