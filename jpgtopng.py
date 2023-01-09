import os
from PIL import Image # Importing Image from Pillow Module

# Set the directory where the JPG images are stored
input_dir = r'C:\Users\Mahraz\Desktop\garbage-ds\plates'

# Set the directory where the PNG images will be saved
output_dir = r'C:\Users\Mahraz\Desktop\garbage-ds\pngs\plates'

# Iterate over the JPG images in the input directory
for file in os.listdir(input_dir):
    # Check if the file is a JPG image
    if file.endswith(".jpg"):
        # Open the image
        with Image.open(os.path.join(input_dir, file)) as im:
            # Convert the image to PNG
            im.save(os.path.join(output_dir, file.replace(".jpg", ".png")), "PNG")
