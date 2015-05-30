# file: randomRings.py
# author: Jason Morse
# date: February 1, 2013
#

from stddraw import *

import random

def randomRings(picture, N):
    def loop(n):
        if n < N:
            x = random.random()
            y = random.random()
            radius = random.random()
            width = random.random() * radius
            color = picture.randomColor()
            picture.filledCircle(x, y, radius, color)
            picture.filledCircle(x, y, radius - width, 'white')
            loop(n+1)
    loop(0)
        
def testRing():
    def responder(event):
        N = 5
        randomRings(picture, N)

    picture = Picture()
    picture.bind('<Button-1>', responder)
    picture.start()

testRing()

