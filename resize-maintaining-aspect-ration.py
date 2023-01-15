import cv2
import os

# Set the image directory
image_dir = r'C:\Users\Mahraz\Desktop\497Project\resized\tissue'

# Set the new image width
new_width = 1600

# Iterate through all images in the directory
for filename in os.listdir(image_dir):
    # Read the image
    image = cv2.imread(os.path.join(image_dir, filename))

    # Calculate the new height based on the aspect ratio
    aspect_ratio = image.shape[0] / image.shape[1]
    new_height = int(new_width * aspect_ratio)

    # Resize the image
    image = cv2.resize(image, (new_width, new_height))

    # Save the image with the new size
    cv2.imwrite(os.path.join(image_dir, filename), image)
