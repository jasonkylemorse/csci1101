# file: diamonds.py
# author: Jason Morse
# date: February 1, 2013
#

from stddraw import *

def diamonds(picture, n):
    side = 1.0 / n
    def loop(column):
        if column < n:
            color = picture.randomColor()
            picture.filledSquare((side * column) + (side / 2), side * column + (side / 2), side / 2, color)
            loop(column + 1)
    loop(0)

def testDiamonds():
    def responder(event):
        diamonds(picture, 7)

    picture = Picture()
    picture.bind('<Button-1>', responder)
    picture.start()

testDiamonds()
