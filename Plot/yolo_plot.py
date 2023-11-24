import cv2
import matplotlib.pyplot as plt
import os

# Paths to the image and label files
image_path = r"C:\Users\MahdiKhalili\Desktop\DTpit\images\19338.jpg"
label_path = r"C:\Users\MahdiKhalili\Desktop\DTpit\labels\19338.txt"

# Check if files exist
if not (os.path.exists(image_path) and os.path.exists(label_path)):
    raise FileNotFoundError("Either the image or label file does not exist!")

# Load the image
image = cv2.imread(image_path)
h, w, _ = image.shape

# Read and plot the bounding boxes from the label file
with open(label_path, "r") as file:
    for line in file.readlines():
        # Parse the line into components: [class, x_center, y_center, width, height]
        _, x_center, y_center, width, height = [float(x) for x in line.split()]

        # Convert YOLO bounding box to OpenCV format
        x_min = int((x_center - width / 2) * w)
        y_min = int((y_center - height / 2) * h)
        x_max = int((x_center + width / 2) * w)
        y_max = int((y_center + height / 2) * h)

        # Draw the bounding box
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

# Display the image using matplotlib
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("1.jpg with Bounding Box")
plt.axis("off")
plt.show()
