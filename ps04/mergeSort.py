# file: mergeSort.py
# author: Jason Morse
# date: February 19, 2013
#

def mergeSort(list):
    
  if list == []:
    return []

  else:
    pivot = list[0]
    left = [x for x in list if x < pivot]
    right = [x for x in list[1:] if x >= pivot]
    return mergeSort(left) + [pivot] + mergeSort(right)

def merge(list1, list2):

    a = list1 + list2
    
    return mergeSort(a)

