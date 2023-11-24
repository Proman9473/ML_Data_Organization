import os
import shutil

# Define paths to the input directories and output directory
input_dir = r"C:\Users\MahdiKhalili\Desktop\datapitsfinal11"
output_dir = r"C:\Users\MahdiKhalili\Desktop\DTpit"

# Create the output directory
os.makedirs(output_dir, exist_ok=True)

# Define the subdirectories for each split
splits = ['train', 'test', 'val']

# Loop through each split
for split in splits:
    # Define paths to the current split's directories
    images_dir = os.path.join(input_dir, 'images', split)
    xml_dir = os.path.join(input_dir, 'xml', split)

    # Loop through the images in the current split's directory
    for filename in os.listdir(images_dir):
        if filename.endswith('.jpg'):
            # Move the image file to the output directory
            shutil.move(os.path.join(images_dir, filename), os.path.join(output_dir, filename))

            # Define the corresponding XML filename
            basename = os.path.splitext(filename)[0]
            xml_filename = f"{basename}.xml"

            # Move the XML file to the output directory
            shutil.move(os.path.join(xml_dir, xml_filename), os.path.join(output_dir, xml_filename))
