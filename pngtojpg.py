from PIL import Image
import os

# Set the path of the folder containing PNG images
png_folder = "path/to/png/folder"

# Set the path of the output folder for JPEG images
jpeg_folder = "path/to/jpeg/folder"

# Loop through all the PNG files in the folder
for filename in os.listdir(png_folder):
    if filename.endswith(".png"):
        # Open the PNG file and convert it to RGB format
        png_image = Image.open(os.path.join(png_folder, filename)).convert("RGB")
        
        # Set the output file path and save the JPEG image
        jpeg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpeg_image_path = os.path.join(jpeg_folder, jpeg_filename)
        png_image.save(jpeg_image_path, "JPEG")
