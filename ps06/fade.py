# file: fade.py
# author: Jason Morse
# date: March 20, 2013
# 
from stdaudio import *

def makeSquareWaveNote(duration, halfSteps):

  sampleRate = 44100
  
  minSample = -1.0
  maxSample = 1.0

  frequencyOfA4 = 440 # Hz

  frequency = frequencyOfA4 * pow(2, halfSteps / 12.0)
  
  waveLength = int(sampleRate / frequency)

  halfWay = waveLength / 2
  
  oneSquareWave = [ minSample + 2.0 * (i / halfWay) for i in range(waveLength) ]

  allSquareWaves = [ oneSquareWave[i % waveLength] for i in range(int(duration * sampleRate))]

  return makeSound(allSquareWaves, allSquareWaves)


def fade(sound):
    left = getLeftChannel(sound)
    
    x = len(left)
    for i in range(x):
      left[i] = left[i] * (1.0 - i/float(len(left)))
    
    right = getRightChannel(sound)
    
    x = len(right)
    for i in range(x):
      right[i] = right[i] * (1.0 - i/float(len(right)))

    return makeSound(left, right)

def testFade():
  a = makeSquareWaveNote(3, 6)
  play(fade(a))

testFade()
