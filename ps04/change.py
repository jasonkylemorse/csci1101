# file: change.py
# author: Jason Morse
# date: February 19, 2013
#

 def removeLargest(list):
    largest = max(list)
    return (largest, [ n for n in list if n != largest ])

def nCopies(n, item):
  if n == 0:
    return []
  else:
    return [item] + nCopies(n - 1, item)

def change(amount, coins):
    if amount == 0:
        return []
    else:
        (largest, rest) = removeLargest(coins)
        n = amount / largest
        if amount % largest == 0:
            return nCopies(n, largest)
        else:
            return nCopies(n, largest) + change(amount % largest, rest)
