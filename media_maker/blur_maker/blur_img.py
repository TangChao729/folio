import sys
import os
from PIL import Image, ImageFilter

if len(sys.argv) != 2:
    print("Usage: python blur_img.py <image_path>")
    sys.exit(1)

input_path = sys.argv[1]
if not os.path.isfile(input_path):
    print(f"File not found: {input_path}")
    sys.exit(1)

# Open the image
img = Image.open(input_path)

# Resize to smaller size (e.g., 25% of original)
small_size = (max(1, img.width // 4), max(1, img.height // 4))
img_small = img.resize(small_size, Image.LANCZOS)

# Apply blur
img_blur = img_small.filter(ImageFilter.GaussianBlur(radius=6))

# Prepare output filename
base, ext = os.path.splitext(input_path)
output_path = f"{base}-blur{ext}"

# Save the blurred image
img_blur.save(output_path)
print(f"Blurred image saved to {output_path}") 