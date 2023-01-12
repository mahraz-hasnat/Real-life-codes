import cv2
import os

# Set the image directory
image_dir = r'C:\Users\Mahraz\Desktop\test\resize3'

# Set the new image size
new_size = (1000, 700)

# Iterate through all images in the directory
for filename in os.listdir(image_dir):
    # Read the image
    image = cv2.imread(os.path.join(image_dir, filename))

    # Resize the image
    image = cv2.resize(image, new_size)

    # Save the image with the new size
    cv2.imwrite(os.path.join(image_dir, filename), image)
