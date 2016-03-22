import cv2
import cv2.cv as cv
from itertools import izip
import Image

# Input files
# Full path of file
videoFile = '/home/abhishek/projects/egnesse/Motivational short video - How to succeed - cartoon-hS5CfP8n_js.mp4'
imageFile = '/home/abhishek/projects/egnesse/pic/image153.jpg'

# Setting
checkMode = True    # Make it false, if you do not want to check type of image
checkSize = False    # Make it false, if you do not want to check Size of image

# Read Video file
videoFile = cv2.VideoCapture(videoFile)

# Get first frame
flag, frame = videoFile.read()

count = 0;

# Read input image
inputImage = Image.open(imageFile)

count = 0

while flag:
    # Convert frame array to image
    frameImage = Image.fromarray(frame)

    if checkMode == True:
        assert inputImage.mode == frameImage.mode, "Different kinds of images"
    if checkSize == True:
        assert inputImage.size == frameImage.size, "Different sizes"

    pairs = izip(inputImage.getdata(), frameImage.getdata())
    if len(inputImage.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

    ncomponents = inputImage.size[0] * inputImage.size[1] * 3
    print "Difference (percentage):", (dif / 255.0 * 100) / ncomponents
    count += 1

    # get the next frame
    flag, frame = videoFile.read()
