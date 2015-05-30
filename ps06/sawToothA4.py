# file: sawToothA4.py
# author: Jason Morse
# date: March 20, 2013
# 

from stdaudio import *

def makeSawToothA4(duration, amplitude):
  
  sampleRate = 44100.0
  
  minSample = -1.0
  maxSample = 1.0

  frequencyOfA4 = 14700 # Hz

  frequency = frequencyOfA4
  
  waveLength = int((sampleRate / frequency))

  delta = (2.0 * amplitude) / waveLength
  
  oneSawTooth = [ (minSample + (i * delta)) for i in range(int(waveLength)) ]

  allSawToothWaves = [ oneSawTooth[i % int(waveLength)]  for i in range(int(duration * sampleRate))]

  return makeSound(allSawToothWaves, allSawToothWaves)

def testSawToothA4():
  a = makeSawToothA4(3, 1.0)
  play(a)

testSawToothA4()
