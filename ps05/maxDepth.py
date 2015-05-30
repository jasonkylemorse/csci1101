# file: maxDepth.py
# author: Jason Morse
# date: March 1, 2013
#

# Binary Search Tree insert
#
def insert(key, value, bst):
    if bst == None:
        return (None, key, value, None)
    else:
        (left, key1, value1, right) = bst
        if key == key1:
            return (left, key, value, right)
        elif key < key1:
            return (insert(key, value, left), key1, value1, right)
        else:
            return (left, key1, value1, insert(key, value, right))

# Binary Search Tree find
#
def find(key, bst):
    if bst == None:
        return None
    else:
        (left, key1, value, right) = bst
        if key == key1:
            return value
        elif key < key1:
            return find(key, left)
        else:
            return find(key, right)


def maxDepth(bst):
    (left, key, value, right) = bst
    if left == None and right == None:
        return 0
    if left == None:
        return maxDepth(right) + 1
    if right == None:
        return maxDepth(left) + 1
    else:
        leftDepth = maxDepth(left)
        rightDepth = maxDepth(right)
        return max(leftDepth, rightDepth) + 1

