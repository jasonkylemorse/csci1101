# file: ringInBounds.py
# author: Jason Morse
# date: February 1, 2013
#

from stddraw import *

def ringInBounds(picture, x, y, radius, width, color):
    
    if (x + radius) < 1.0 and (y + radius) < 1.0 and (x - radius) > 0 and (y - radius) > 0:        
            picture.filledCircle(x, y, radius, color)
            picture.filledCircle(x, y, radius - width, 'white')
            picture.start()
        
    else:
        
        print 'Ring centered at ' + str((x, y)) + ' with radius ' + str(radius) + ' is out of bounds.'

def testRingInBounds():
    def responder(event):
        color = picture.randomColor()
        ringInBounds(picture, .5, .5, .3, .1, 'green')

    picture = Picture()
    picture.bind('<Button-1>', responder)
    picture.start()

def testRingInBounds2():
    def responder(event):
        color = picture.randomColor()
        ringInBounds(picture, .9, .9, .3, .1, 'red')

    picture = Picture()
    picture.bind('<Button-1>', responder)
    picture.start()


testRingInBounds()
testRingInBounds2()

# testRingInBounds() will provide an example of a ring in bounds
# testRingInBounds2() will provide an example of a ring out of bounds
