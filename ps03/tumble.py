# file: tumble.py
# author: Jason Morse
# date: February 10, 2013
#

from stddraw import *
import math

def tumble(picture, x, y, width, height, angle, delta, color):

        def loop(x, width, height):
            
            if x - width < 1.0:
                
                fall(picture, x, y, width, height, angle, delta, color)
                
                loop(x + height, height, width)

        loop(0, width, height)
                

def fall(picture, x, y, width, height, angle, delta, color):

    def loop(angle):
        
        inclinedRectangle(picture, x, y, width, height, angle, color)
    
        if angle > 0:
   
            picture.wait(50)
            picture.clear()
            picture.line(0.0, y, 1.0, y, penWidth=4.0, color='brown')
            loop(max(0.0, angle - delta))
            
    loop(angle)

def inclinedRectangle(picture, x, y, width, height, r, color):
    
    rightAngle = math.pi / 2.0

    x1 = x + math.cos(r) * height
    y1 = y + math.sin(r) * height
    
    x2 = x1 + math.cos(r + rightAngle) * width
    y2 = y1 + math.sin(r + rightAngle) * width
    
    x3 = x + math.cos(r + rightAngle) * width
    y3 = y + math.sin(r + rightAngle) * width

    filledPolygon(picture, [x, x1, x2, x3], [y, y1, y2, y3], color)

def filledPolygon(picture, xs, ys, color): 
    picture.filledPolygon(xs, ys, color)
    picture.polygon(xs, ys)

def start():
    def responder(event):
        width = .25
        height = .5
        angle = math.pi / 2.0
        delta = .1
        color = picture.randomColor()
        tumble(picture, .2, .2, width, height, angle, delta, color)

    picture = Picture()
    picture.setW(800)
    picture.setH(800)
    picture.bind('<Button-1>', responder)
    picture.start()
start()
