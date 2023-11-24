import xml.etree.ElementTree as ET
import glob
import os

def xml_to_yolo_bbox(bbox, w, h):
    x_center = ((bbox[2] + bbox[0]) / 2) / w
    y_center = ((bbox[3] + bbox[1]) / 2) / h
    width = (bbox[2] - bbox[0]) / w
    height = (bbox[3] - bbox[1]) / h
    return [x_center, y_center, width, height]

input_dir = r"C:\Users\MahdiKhalili\Desktop\DTpit\xml"
output_dir = r"C:\Users\MahdiKhalili\Desktop\DTpit\labels"
image_dir = r"C:\Users\MahdiKhalili\Desktop\DTpit\images"

os.makedirs(output_dir, exist_ok=True)

files = glob.glob(os.path.join(input_dir, '*.xml'))
for fil in files:
    basename = os.path.basename(fil)
    filename = os.path.splitext(basename)[0]

    if not os.path.exists(os.path.join(image_dir, f"{filename}.jpg")):
        print(f"{filename} image does not exist!")
        continue

    result = []
    bboxes = []

    tree = ET.parse(fil)
    root = tree.getroot()
    width = int(root.find("img_size_w").text)
    height = int(root.find("img_size_h").text)

    for obj in root.findall('object'):
        label = obj.get("name")

        pil_bbox = [int(float(x.text)) for x in obj.find("bndbox")]
        yolo_bbox = xml_to_yolo_bbox(pil_bbox, width, height)
        bbox_string = " ".join([str(x) for x in yolo_bbox])
        result.append(f"{0} {bbox_string}")
        bboxes.append(pil_bbox)

    if result:
        with open(os.path.join(output_dir, f"{filename}.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(result))
