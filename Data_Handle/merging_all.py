import os
import shutil

def organize_files(src_folder, dest_folder):
    # Create destination folders if they do not exist
    os.makedirs(os.path.join(dest_folder, 'images'), exist_ok=True)
    os.makedirs(os.path.join(dest_folder, 'xml'), exist_ok=True)

    # Initialize a counter for naming files
    file_counter = 1

    # Walk through the source directory
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith('.jpg'):
                # Prepare the paths for the image and corresponding XML file
                img_path = os.path.join(root, file)
                xml_path = os.path.join(root, file.replace('.jpg', '.xml'))

                # Check if the XML file exists
                if os.path.exists(xml_path):
                    # Copy and rename the image file
                    shutil.copy(img_path, os.path.join(dest_folder, 'images', f'{file_counter}.jpg'))
                    # Copy and rename the XML file
                    shutil.copy(xml_path, os.path.join(dest_folder, 'xml', f'{file_counter}.xml'))

                    # Increment the file counter
                    file_counter += 1

# Directory paths
src_dir = r'C:\Users\MahdiKhalili\Desktop\Pit_13'
dest_dir = r'C:\Users\MahdiKhalili\Desktop\DTpit'

organize_files(src_dir, dest_dir)
