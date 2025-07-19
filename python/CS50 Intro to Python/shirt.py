import sys
import os
from PIL import Image, ImageOps

# Allowed extensions
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Get file extensions (case-insensitive)
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    # Check extensions
    if input_ext not in ALLOWED_EXTENSIONS or output_ext not in ALLOWED_EXTENSIONS:
        sys.exit("Input and output must be .jpg, .jpeg, or .png")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # Try to open input image
    try:
        photo = Image.open(input_path)
    except FileNotFoundError:
        sys.exit(f"Input does not exist: {input_path}")
    except Exception as e:
        sys.exit(f"Could not open input: {e}")

    # Open shirt.png
    try:
        shirt = Image.open("shirt.png")
    except Exception as e:
        sys.exit(f"Could not open shirt.png: {e}")

    # Resize and crop input photo to shirt size
    size = shirt.size
    photo = ImageOps.fit(photo, size)

    # Overlay shirt on photo
    photo.paste(shirt, shirt)

    # Save result
    try:
        photo.save(output_path)
    except Exception as e:
        sys.exit(f"Could not save output: {e}")

if __name__ == "__main__":
    main() 