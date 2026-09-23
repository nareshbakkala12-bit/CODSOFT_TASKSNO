# CODSOFT AI Internship - Task 3
# Face Detection using OpenCV

import cv2
from google.colab.patches import cv2_imshow

# Load the pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Upload an image
from google.colab import files
uploaded = files.upload()

# Get uploaded image name
image_name = list(uploaded.keys())[0]

# Read the image
image = cv2.imread(image_name)

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# Display result
print("Number of faces detected:", len(faces))
cv2_imshow(image)
