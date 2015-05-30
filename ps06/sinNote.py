# file: sinNote.py
# author: Jason Morse
# date: March 20, 2013
#

from stdaudio import *
import math

def sinNote(halfSteps, duration, amplitude):
    
    sampleRate = 44100

    minSample = -1.0
    maxSample = 1.0

    frequencyOfA4 = 440

    frequency = frequencyOfA4 * pow(2, halfSteps / 12.0)

    waveLength = int(sampleRate / frequency)
    
    sinCurve = [float(amplitude) * math.sin(2.0 * math.pi * float(frequency) * (float(i % waveLength)/ float(sampleRate))) for i in range(waveLength)]

    allSinCurves = [sinCurve[i % waveLength] for i in range(int(duration * sampleRate))]

    return makeSound(allSinCurves, allSinCurves)

def testSinNote():
    a = sinNote(10, 4, 1.0)
    play(a)

testSinNote()
