# file: problemset1.py
# author: Jason Morse
# date: 1/17/13
#

import math
from stddraw import *

def helloWorld():
    return('Hello World!')

def goldenRatio():
    return((1 + math.sqrt(5)) / 2)

def hypotenuse(base,height):
    return(math.sqrt((base * base) + (height * height)))

def yellowCircle(radius):
    picture = Picture()

    red = 255         # All colors can be made with red, green and blue,
    green = 255     # with values ranging from 0 to 255.
    blue = 0        # What values of red, green, blue give yellow?

    color = picture.makeColor(red, green, blue)

    picture.filledCircle(.5, .5, radius, color)

    picture.start()
