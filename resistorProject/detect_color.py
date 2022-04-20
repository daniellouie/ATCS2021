# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
# 1. Yellow rgba(253,203,0,255)
#       *ran into an error with the boundaries of the yellow color,
#        had to play with the bounds
# 2. Purple rgba(159,0,152,255)
# 3. Red rgba(244,70,0,255)
# 4. Resistor rgba(218,188,123,255)
# Boundaries in BGR
boundaries = [
    ([0, 195, 245], [10, 205, 255]),
    ([150, 0, 150], [160, 10, 160]),
    ([0, 65, 240], [10, 75, 250]),
    ([120, 180, 210], [130, 190, 220])
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    # show the images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)
