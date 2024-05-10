#--------------------Folder--------------------#

import os
from rembg import remove
from PIL import Image

from google.colab import drive

drive.mount('/content/drive')

# Change the working directory to the Food Project directory
os.chdir('/content/drive/My Drive/Food Project')

# Define input and output folders
input_folder = "./input_images"
output_folder = "./output_images"

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image file
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # Define input and output file paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.split('.')[0] + '.png')

        # Load the input image
        input_image = Image.open(input_path)

        # Remove the background using rembg
        output_image = remove(input_image)

        # Save the output image as a PNG file
        output_image.save(output_path)
