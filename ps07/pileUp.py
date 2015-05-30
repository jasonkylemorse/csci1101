# file: pileUp.py
# author: Jason Morse
# date: April 5, 2013
#

from stddraw import *
import random

def pileUp(N):
    def responder(event):
        fallingBlockGo(picture, (1.0 / N), a)

    v = 0
    a = [[v]*(N) for i in range(N)]
    print a
    
    picture = Picture()
    picture.setH(800)
    picture.setW(800)
    picture.bind('<Button-1>', responder)
    picture.start()

def fallingBlockGo(picture, width, a):
    N = int(width ** -1)
    
    for i in range(N):
        if a[(N - 1)][i] == 1:
            print 'Pile Up Complete.'
            return None
    
    (red, green, blue) = (255, 255, 0)
    color = picture.makeColor(red, green, blue)

    halfWidth = (width / 2)
    halfHeight = halfWidth
    y = 1.0
    col = random.randint(0, N - 1)
    x = (halfWidth * 2 * col) + halfWidth
    color = 'blue'
    
    deltaY = -.01
    delay = 200
    
    row = array(a, col, width)
    if row < N:
        a[row][col] = 1
    print a
    
    if row == (N - 1):
        color = 'yellow'
        
    handleOfBlock = picture.filledRectangle(x, y, halfWidth, halfHeight, color)
    
    while y + (halfHeight) > ((halfWidth * 2 * row) + 2 * halfWidth):
        picture.move(handleOfBlock, 0, deltaY)
        picture.wait(handleOfBlock, delay)
        y = y + deltaY

def array(a, col, width):
    N = int(width ** -1)
    row = 0
    while row < N:
        if a[row][col] == 0:
            return row
        row = row + 1
