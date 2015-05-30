# file: approxPi.py
# author: Jason Morse
# date: February 10, 2013
#

import random
import math

def approxPi(N):
    if N > 0:
        def loop(i, count):
            if i < N:
                x = random.random()
                y = random.random()
                if math.sqrt((x * x) + (y * y)) < 1.0:
                    count = count + 1
                return loop(i + 1, count)
        
            else:
                return ((4.0 * float(count)) / N)
        return loop(0, 0)
                


            
        

    
    
    
