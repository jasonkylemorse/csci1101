# file: rowOfRings.py
# author: Jason Morse
# date: February 1, 2013
#

from stddraw import *

import random

def ring(picture, x, y, radius, width, color):
        picture.filledCircle(x, y, radius, color)
        picture.filledCircle(x, y, radius - width, 'white')

def rowOfRings(picture, y, N):
    radius = 1.0 / (2 * N)
    def loop(N):
        if N > 0:
            x = 2 * N * radius - radius
            color = picture.randomColor()
            width = random.random() * radius
            loop(N-1)
            picture.filledCircle(x, y, radius, color)
            picture.filledCircle(x, y, radius - width, 'white')
    loop(N)

def testRowOfRings():
    def responder(event):
        rowOfRings(picture, 0.5, 5)

    picture = Picture()
    picture.bind('<Button-1>', responder)
    picture.start()

testRowOfRings()
    
