"""
Detect colors in still image

@author: Daniel Louie
@version: 4/20/22
"""
# import the necessary packages
import numpy as np
import argparse
import cv2

""" REFORMATTED PROJECT: 
rebuilding previous code to work on new set of images
to loop through, identify order, then determine value
"""
# color boundaries dictionary (*in BGR) using color palette of: https://resistorcolorcodecalc.com/
colors = {'yellow': [[0, 195, 245], [10, 205, 255]],
          'purple': [[150, 0, 150], [160, 10, 160]],
          'red': [[0, 65, 240], [10, 75, 250]],
          'resistor': [[120, 180, 210], [130, 190, 220]]}
# rectangle dimensions
rect_start_x = 150
rect_start_y = 245
rect_end_x = 425
rect_end_y = 260
rect_midpoint_y = int((rect_end_y + rect_start_y)/2)
# construct argument parse and parse the argument through terminal
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image")
args = vars(ap.parse_args())
# load image and image shapes
image = cv2.imread(args["image"])
height, width, depth = image.shape
# draw rectangle to visualize scanning bar
start_point = (rect_start_x, rect_start_y)
end_point = (rect_end_x, rect_end_y)
cv2.rectangle(image, start_point, end_point, (0, 0, 255), thickness=3, lineType=cv2.LINE_8)
cv2.imshow("image", image)
# draw circle to visualize starting coordinate of scanner
#*ISSUE with repainting white circle
# circle_center = (rect_start_x, rect_midpoint_y)
# radius = 10
# circle = cv2.circle(image, circle_center, radius, (255, 255, 255), thickness=3, lineType=cv2.LINE_AA)
# cv2.imshow("images", image)
cv2.waitKey(0)

# loop through pixels and access RGB info
for x in range(rect_start_x, rect_end_x):
    y = rect_midpoint_y
    print("x:", x, "y:", y)
    print(image[y][x])
    #*ISSUE with repainting white circle
    # circle_center = (x, y)
    # circle = cv2.circle(image, circle_center, radius, (255, 255, 255), thickness=3, lineType=cv2.LINE_AA)
    # cv2.imshow("images", circle)
    if cv2.waitKey(1) == ord('q'):
        # press q to terminate the loop
        cv2.destroyAllWindows()
        break

"""Original project:
used for testing openCV, methods, ideas. 
Referenced for making reformatted version.
"""
#
# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", help="path to the image")
# args = vars(ap.parse_args())
# # load the image
# image = cv2.imread(args["image"])
# # convert image to hsv/hsb
# image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#
# # define the list of boundaries *(in rgba)
# # 1. Yellow rgba(253,203,0,255)
# #       *ran into an error with the boundaries of the yellow color,
# #        had to play with the bounds
# # 2. Purple rgba(159,0,152,255)
# # 3. Red rgba(244,70,0,255)
# # 4. Resistor rgba(218,188,123,255)
# # Boundaries *(in BGR)
# # arrays may need to be in Numpy Arrays for OpenCV**
# boundaries = [
#     ([0, 195, 245], [10, 205, 255]),
#     ([150, 0, 150], [160, 10, 160]),
#     ([0, 65, 240], [10, 75, 250]),
#     ([120, 180, 210], [130, 190, 220])
# ]
# # template for converting boundaries to a dictionary (BGR)
# colors = {'yellow': [[0, 195, 245], [10, 205, 255]],
#           'purple': [[150, 0, 150], [160, 10, 160]],
#           'red': [[0, 65, 240], [10, 75, 250]],
#           'resistor': [[120, 180, 210], [130, 190, 220]]}
#
#
# # # loop over the boundaries
# # for (lower, upper) in boundaries:
# #     # create NumPy arrays from the boundaries
# #     lower = np.array(lower, dtype="uint8")
# #     #test
# #     print(lower)
# #     upper = np.array(upper, dtype="uint8")
# #     #test
# #     print(upper)
# #     # find the colors within the specified boundaries and apply
# #     # the mask
# #     mask = cv2.inRange(image, lower, upper)
# #     output = cv2.bitwise_and(image, image, mask=mask)
# #     # show the images
# #     cv2.imshow("images", np.hstack([image, output]))
# #     cv2.waitKey(0)
#
# def make_mask(image, lower, upper):
#     # create NumPy arrays from the boundaries
#     lower = np.array(lower, dtype="uint8")
#     # test
#     print(lower)
#     upper = np.array(upper, dtype="uint8")
#     # test
#     print(upper)
#     # find the colors within the specified boundaries and apply
#     # the mask
#     mask = cv2.inRange(image, lower, upper)
#     return mask
#
#
# yellow_mask = make_mask(image, colors['yellow'][0], colors['yellow'][1])
# output = cv2.bitwise_and(image, image, mask=yellow_mask)
# # show the images
# cv2.imshow("images", np.hstack([image, output]))
# cv2.waitKey(0)
#
# purple_mask = make_mask(image, colors['purple'][0], colors['purple'][1])
# output = cv2.bitwise_and(image, image, mask=purple_mask+yellow_mask)
# # show the images
# cv2.imshow("images", np.hstack([image, output]))
# cv2.waitKey(0)
#
# red_mask = make_mask(image, colors['red'][0], colors['red'][1])
# output = cv2.bitwise_and(image, image, mask=purple_mask+yellow_mask+red_mask)
# # show the images
# cv2.imshow("images", np.hstack([image, output]))
# cv2.waitKey(0)
#
# resistor_mask = make_mask(image, colors['resistor'][0], colors['resistor'][1])
# output = cv2.bitwise_and(image, image, mask=purple_mask+yellow_mask+red_mask+resistor_mask)
# # show the images
# cv2.imshow("images", np.hstack([image, output]))
# cv2.waitKey(0)
#
#
# # define the starting and end points of the rectangle
# # start_point = (x, y))
# start_point = (150, 245)
# end_point = (425, 260)
# # draw the rectangle
# cv2.rectangle(image, start_point, end_point, (0, 0, 255), thickness=3, lineType=cv2.LINE_8)
# # display the output
# cv2.imshow("images", np.hstack([image, output]))
# cv2.waitKey(0)
#
# #draw a circle
# circle_center = (285, 252)
# radius = 10
# cv2.circle(image, circle_center, radius, (255, 255, 255), thickness=3, lineType=cv2.LINE_AA)
# cv2.imshow("images", np.hstack([image, output]))
# cv2.waitKey(0)
#
# # image[y, x]??
# b, g, r = (image[252, 285])
# print(r)
# print(g)
# print(b)
# cv2.waitKey(0)


