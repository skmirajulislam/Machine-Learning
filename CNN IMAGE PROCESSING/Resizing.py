from PIL import Image
import os

path = '/Users/skmirajulislam/Documents/MyPython/ML/Topstack/data/flickr1k/grayscale' # source path
dstpath = '/Users/skmirajulislam/Documents/MyPython/ML/Topstack/data/flickr1k/Resize128' # destination path
directory = os.listdir(path)
count = 1000

for item in directory:
    img = Image.open(os.path.join(path, item))
    imgResize = img.resize((128, 128), Image.ANTIALIAS)
    imgResize.save(os.path.join(dstpath, f'{count}.jpg'))
    count += 1
