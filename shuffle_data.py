import os
import random
import shutil

# Define paths to input and output directories
input_image_dir = r"dir"
input_label_dir = r"dir"
input_xml_dir = r"dir"
output_dir = r"dir"

# Define train/test/validation split percentages
train_percent = 0.8
test_percent = 0.1
val_percent = 0.1

# Create output directories
for split in ['train', 'test', 'val']:
    os.makedirs(os.path.join(output_dir, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels', split), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'xml', split), exist_ok=True)

# Loop through images and labels
image_filenames = os.listdir(input_image_dir)
random.shuffle(image_filenames)

for filename in image_filenames:
    if not filename.endswith('.jpg'):
        continue

    basename = os.path.splitext(filename)[0]
    label_filename = f"{basename}.txt"
    xml_filename = f"{basename}.xml"

    # Determine which split to use
    r = random.uniform(0, 1)
    if r < train_percent:
        split = 'train'
    elif r < train_percent + test_percent:
        split = 'test'
    else:
        split = 'val'

    # Move files to appropriate split folders
    shutil.move(os.path.join(input_image_dir, filename), os.path.join(output_dir, 'images', split, filename))
    shutil.move(os.path.join(input_label_dir, label_filename), os.path.join(output_dir, 'labels', split, label_filename))
    shutil.move(os.path.join(input_xml_dir, xml_filename), os.path.join(output_dir, 'xml', split, xml_filename))
