import os
import shutil

data_dir = 'data_dir'
output_dir = 'output_dir'
mapping_file = 'mapping.txt'

# Create output directories if they don't exist
os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'xml'), exist_ok=True)

# Loop over all the subfolders in the input directory
count = 1
mapping = {}

for root, dirs, files in os.walk(data_dir):
    jpg_files = [f for f in files if f.endswith('.jpg')]
    xml_files = [f for f in files if f.endswith('.xml')]

    for jpg_file in jpg_files:
        base_name = os.path.splitext(jpg_file)[0]
        corresponding_xml_file = base_name + '.xml'

        if corresponding_xml_file not in xml_files:
            raise FileNotFoundError(f"No XML file found for {jpg_file} in {root}")

        img_src_path = os.path.join(root, jpg_file)
        xml_src_path = os.path.join(root, corresponding_xml_file)

        img_dst_path = os.path.join(output_dir, 'images', f'{count}.jpg')
        xml_dst_path = os.path.join(output_dir, 'xml', f'{count}.xml')

        shutil.copy(img_src_path, img_dst_path)
        shutil.copy(xml_src_path, xml_dst_path)

        print(f"Copying image {img_src_path} to {img_dst_path}")
        print(f"Copying XML {xml_src_path} to {xml_dst_path}")

        mapping[count] = os.path.relpath(root, data_dir)

        count += 1

# Write the mapping to a text file
with open(os.path.join(output_dir, mapping_file), 'w') as f:
    for number, original_folder in mapping.items():
        f.write(f'{number} ==> {original_folder}\n')
