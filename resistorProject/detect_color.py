"""
Identify Resistor values given still image
This program identifies the band colors and value of resistors.
It helps color deficient people, like myself, when the color
bands are difficult to differentiate or see. It currently
processes still images taken with specific framing.
@author: Daniel Louie
@version: 5/5/22
"""
# import the necessary packages
import numpy as np
import argparse
import sys
import cv2

# color palette: uses colors from ResistorColorTable.png (from: https://resistorcolorcodecalc.com/)
# each color interval was calibrated with a color identifier website and manually run through my
# program to set upper and lower values for R, G, and B.(+/-10 unless it hits 0 or 255 before then)
resistorColorPalette = {'resistorWire': [[99, 123, 135], [119, 143, 155]],
                        'resistorDarkTan': [[190, 160, 119], [210, 180, 139]],
                        'resistorLightTan': [[219, 186, 142], [239, 206, 162]],
                        'black': [[0, 0, 0], [10, 10, 10]],
                        'brown': [[107, 0, 0], [127, 10, 10]],
                        'red': [[245, 0, 0], [255, 10, 10]],
                        'orange': [[245, 143, 0], [255, 163, 10]],
                        'yellow': [[245, 245, 0], [255, 255, 10]],
                        'green': [[0, 157, 70], [10, 177, 90]],
                        'blue': [[0, 91, 174], [10, 111, 194]],
                        'violet': [[132, 0, 245], [152, 10, 255]],
                        'gray': [[146, 146, 146], [166, 166, 166]],
                        'white': [[245, 245, 245], [255, 255, 255]],
                        'gold': [[245, 200, 0], [255, 220, 10]],
                        'silver': [[206, 206, 206], [226, 226, 226]],
                        'pink': [[245, 206, 245], [255, 226, 255]],
                        }

# Dictionary that stores the color bands of resistors and their associated digit value
# Used for the first 2 bands
colorDigitDict = {'black': '0',
                  'brown': '1',
                  'red': '2',
                  'orange': '3',
                  'yellow': '4',
                  'green': '5',
                  'blue': '6',
                  'violet': '7',
                  'grey': '8',
                  'white': '9'}

# Dictionary that stores the color bands of resistors and their associated multiplier
# Used for the 3rd band
multiplierDict = {'pink': '.001',
                  'silver': '.01',
                  'gold': '.1',
                  'black': '1',
                  'brown': '10',
                  'red': '100',
                  'orange': '1k',
                  'yellow': '10k',
                  'green': '100k',
                  'blue': '1M',
                  'violet': '10M',
                  'grey': '100M',
                  'white': '1G'}

# Dictionary that stores the color bands of resistors and their associated (+/-) tolerance
# Used for the 4th band
toleranceDict = {'gray': '+/- 0.01 %',
                 'yellow': '+/- 0.02 %',
                 'orange': "+/- 0.05 %",
                 'violet': '+/- 0.1 %',
                 'blue': '+/- 0.25 %',
                 'green': '+/- 0.5 %',
                 'brown': '+/- 1 %',
                 'red': '+/- 2 %',
                 'gold': '+/- 5 %',
                 'silver': '+/- 10 %',
                 'none': '+/- 20 %'}

# bounding rectangle dimensions
rectStartX = 440
rectStartY = 170
rectEndX = 850
rectEndY = 190
rectMidPointY = int((rectEndY + rectStartY) / 2)


# function that scans a slice of pixels in the image and returns an array of resistor color bands
def scanImageColors():
    # array to be filled with the resistor band values, in order
    resistorColors = []
    # previous, current and next pixel values to be used in parsing pixels
    previousPixel = None
    currentPixel = None
    nextPixel = None
    print("Starting scan... (press 'q' to quit)")
    # loop through pixels and access RGB info
    # shrinking range by 2 on each side so it doesn't count the pixels of the bounding box
    for x in range(rectStartX + 2, rectEndX - 2):
        # # quits the loop and closes the window
        if cv2.waitKey(1) == ord('q'):
            # press q to terminate the loop
            cv2.destroyAllWindows()
            # quit program
            sys.exit()
            break
        y = rectMidPointY
        # get the values of the current pixel
        b, g, r = image[y][x]
        currentPixel = r, g, b
        # get the values of the next pixel
        bNext, gNext, rNext = image[y][x + 1]
        nextPixel = rNext, gNext, bNext
        # if the pixel color doesnt match the previous pixel but does match the next pixel
        # eliminates in-between color pixels and the colors picked up by the bounding box
        if currentPixel != previousPixel and currentPixel == nextPixel:
            # call function to get color name of pixel
            # (if it is not one of the pre-determined colors, returns None)
            currentPixelColor = determineColor(currentPixel)
            # add only the band colors
            if currentPixelColor is not None:
                resistorColors.append(currentPixelColor)
        previousPixel = currentPixel
        # progress bar that stays behind the current position to not interfere with the scanning
        progressLine = cv2.line(image, (rectStartX, rectMidPointY), (x - 2, rectMidPointY), (255, 0, 0),
                                thickness=3,
                                lineType=cv2.LINE_8)
        # repaint window to show animation
        cv2.imshow("image", progressLine)
    # if there are only 3 color bands, put None as the last band
    # (because this is still a valid '4 band' resistor code)
    if len(resistorColors) == 3:
        resistorColors.append('none')
    # return the array of band colors in order
    return resistorColors


# function that takes in an R, G, B array and determines if it is a band color in the dictionary
# and if so, returns the color, otherwise returns None
def determineColor(pixelColor):
    # loop through every color in the dictionary
    for colorName, color in resistorColorPalette.items():
        # check the pixel red falls in the red value interval
        if color[0][0] <= pixelColor[0] <= color[1][0]:
            # check the pixel green falls in the green value interval
            if color[0][1] <= pixelColor[1] <= color[1][1]:
                # check the pixel blue falls in the blue value interval
                if color[0][2] <= pixelColor[2] <= color[1][2]:
                    # do not count these as band colors
                    if colorName not in ['resistorWire', 'resistorDarkTan', 'resistorLightTan']:
                        return colorName
    return None


# function that takes in 4 color bands and uses the
# colorDigit, multiplier and tolerance dictionaries
# to determine the resistor value
def determineResistance(colorArray):
    band1, band2, band3, band4 = colorArray
    # if each of the values is a valid color in its array
    if band1 in colorDigitDict \
            and band2 in colorDigitDict \
            and band3 in multiplierDict \
            and band4 in toleranceDict:
        digit1 = colorDigitDict.get(band1)
        digit2 = colorDigitDict.get(band2)
        multiplier = multiplierDict.get(band3)
        tolerance = toleranceDict.get(band4)
        resistance = "Resistance = " + digit1 + digit2 + \
                     " x " + multiplier + " ohms " + tolerance
        return resistance
    else:
        return None


image = cv2.imread("resistorImages/" + input("Enter the resistor image you would like to scan:"))
height, width, depth = image.shape
# draw rectangle to visualize scanning area
startPoint = (rectStartX, rectStartY)
endPoint = (rectEndX, rectEndY)
# draw the rectangle on the main window
cv2.rectangle(image, startPoint, endPoint, (0, 0, 255), thickness=3, lineType=cv2.LINE_8)
# make a copy of the window to only show at the beginning
startImage = image.copy()
cv2.putText(startImage, "press any key to scan image", (10, 120), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1.5, color=(0, 0, 0), thickness=1, lineType=cv2.LINE_8)
cv2.imshow("startImage", startImage)
cv2.waitKey(0)
cv2.imshow("image", image)
# removes the "press any key to scan the image"
cv2.destroyWindow("startImage")
# quit message
cv2.putText(image, "press 'q' to quit", (10, 160), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1.5, color=(0, 0, 0), thickness=1, lineType=cv2.LINE_8)
# call function to determine band colors in order
resistorColorArray = scanImageColors()
cv2.putText(image, "scan complete", (600, 260), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1, color=(255, 0, 0), thickness=1, lineType=cv2.LINE_8)
print("Image scanning complete.")
bandColorString = "Band 1: " + resistorColorArray[0] \
                  + ", Band 2: " + resistorColorArray[1] \
                  + ", Band 3: " + resistorColorArray[2] \
                  + ", Band 4: " + resistorColorArray[3]
print("Resistor Colors:", bandColorString)
# display the band colors
cv2.putText(image, bandColorString, (10, 100), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1, color=(0, 0, 0), thickness=1,
            lineType=cv2.LINE_8)
# call function to determine resistance
resistanceValue = determineResistance(resistorColorArray)
resistanceOutputString = "Resistance value: " + resistanceValue
# display resistance
cv2.putText(image, resistanceOutputString, (10, 120), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1, color=(255, 0, 0), thickness=1, lineType=cv2.LINE_8)
print(resistanceOutputString)
cv2.imshow("image", image)
# wait until 'q' is pressed to quit program
while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 113:
        cv2.destroyAllWindows()
        break
