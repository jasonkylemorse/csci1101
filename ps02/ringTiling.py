# file: ringTiling.py
# author: Jason Morse
# date: February 1, 2013
#

from stddraw import *

import random


def ring(picture, x, y, radius, width, color):
        picture.filledCircle(x, y, radius, color)
        picture.filledCircle(x, y, radius - width, 'white')

def ringTiling(picture, N):
    radius = 1.0 / (2 * N)
    x = 0 - radius
    
    while x < 1.0:
        x = x + (2.0 * radius)
        y = 0 - radius
        
        while y < 1.0:
            width = random.uniform(0, radius)
            color = picture.randomColor()
            ring(picture, x, y, radius, width, color)
            y = y + (2.0 * radius)
        
def testRingTiling():
    def responder(event):
        color = picture.randomColor()
        ringTiling(picture, 5)

    picture = Picture()
    picture.bind('<Button-1>', responder)
    picture.start()

testRingTiling()

