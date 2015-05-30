# file: runFSM.py
# author: Jason Morse & Wantong Liu
# date: May 3, 2013
#
# This file contains Python representations of 2 finite state machines
# and an interpreter for finite state machines.

import string

# runFSM : finitestatemachine * state * string -> bool
#
# The call runFSM(M, state, input) returns true of input is in the
# language of the machine. Otherwise it returns False.
#
#def runFSM(M, state, input):
#
#    (A, Q, delta, _, F) = M
#
#    if (input == '') and (state in F):
#        return True
#    elif input == '':
#        return False
#
#    symbol = input[0]
#    key = (state, symbol)
#
#    if not(key in delta):
#        return False
#    else:
#        newState = delta[key]
#        return runFSM(M, newState, input[1:])

# PS10 - Problem 1 - Rewritten without recursion

def runFSM(M, state, input):

    (A, Q, delta, _, F) = M

    def loop(state, input):

        if (input == '') and (state in F):
            return True
        elif input == '':
            return False

        symbol = input[0]
        key = (state, symbol)
        if key in delta:
            newState = delta[key]
            return loop(newState, input[1:])
        else:
            return False

    return loop(state, input)
   
# Machine M4 accepts binary strings representing multiples of 4.
#
M4 = (['0', '1'], [0, 1, 2], { (0, '0'):1, (0, '1'): 0,
                               (1, '0'):2, (1, '1'): 0,
                               (2, '0'):2, (2, '1'): 0 }, 0, [2])

def fold(f, list, id):
    if list == []:
        return id
    else:
        return f(list[0], fold(f, list[1:], id))
    
def makeDelta():
    def insert((key, value), dictionary):
        dictionary[key] = value
        return dictionary
    
    allLetters = list(string.letters)
    letters = [ letter for letter in allLetters if not(string.upper(letter) in ['B', 'C', 'U'])]
    states = range(3)
    pairs = [ (state, letter) for letter in letters for state in states]
    zeroOne = [ ((state, letter), 0) for (state, letter) in pairs if state < 2 ]
    twos = [ ((state, letter), 2)  for (state, letter) in pairs if state == 2]
    others = [ ((0, 'U'), 0), ((0, 'C'), 0), ((0, 'B'), 1),
               ((1, 'B'), 1), ((1, 'U'), 2), ((1, 'U'), 2), ((1, 'C'), 2),
               ((2, 'U'), 2), ((2, 'U'), 2), ((2, 'B'), 2)]
    transitions = zeroOne + twos + others
    delta = fold(insert, transitions, {})
    return delta

# Machine MB accepts any string that contains either BC or BU.
#
MB = (list(string.letters), [0, 1, 2], makeDelta(), 0, [2])

    
