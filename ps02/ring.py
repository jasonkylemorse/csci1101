# file: ring.py
# author: Jason Morse
# date: February 1, 2013
#

from stddraw import *


def ring(picture, x, y, radius, width, color):
        picture.filledCircle(x, y, radius, color)
        picture.filledCircle(x, y, radius - width, 'white')

def testRing():
    def responder(event):
        color = picture.randomColor()
        ring(picture, .5, .5, .3, .2, color)

    picture = Picture()
    picture.bind('<Button-1>', responder)
    picture.start()

    

testRing()

