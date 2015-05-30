# file: sieve.py
# author: Jason Morse
# date: February 19, 2013
#

def sieve(list):
    if list == []:
        return []
    else:
        return [list[0]] + sieve([n for n in list if n % list[0] != 0])
