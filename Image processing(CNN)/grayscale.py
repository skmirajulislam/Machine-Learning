import os
import cv2

# Specify the path to your original color images
path = r'/Users/skmirajulislam/Documents/MyPython/ML/Topstack/data/flickr1k/images'

# Specify the path where you want to save the grayscale images
dstpath = r'/Users/skmirajulislam/Documents/MyPython/ML/Topstack/data/flickr1k/grayscale'

# List all files in the original_images folder
files = os.listdir(path)

# Iterate through each image and convert it to grayscale
for image in files:
    img = cv2.imread(os.path.join(path, image))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Save the grayscale image to the destination folder
    cv2.imwrite(os.path.join(dstpath, image), gray)
