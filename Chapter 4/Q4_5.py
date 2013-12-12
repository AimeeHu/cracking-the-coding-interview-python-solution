from classes.BinaryTreeNode import *
import sys


# In-order traversal, and compare an element to the previous one
def isBST1(btree):
    return checkBST1(btree)[0]

def checkBST1(btree, previous = -sys.maxint-1):
    if btree is None or btree.value is None:
        return True, previous    
    
    [isleftbst, previous] = checkBST1(btree.left, previous)
    if not isleftbst:
        return False, previous
    
    if btree.value < previous:
        return False, previous
    previous = btree.value

    if not checkBST1(btree.right, previous)[0]:
        return False, previous

    return True, previous


# Passing down min and max values to check the node value is within the range
def isBST2(btree, minvalue = -sys.maxint-1, maxvalue = sys.maxint):
    if btree is None or btree.value is None:
        return True

    if btree.value < minvalue or btree.value > maxvalue:
        return False

    if (not isBST2(btree.left, minvalue, btree.value)) \
        or (not isBST2(btree.right, btree.value, maxvalue)):
        return False

    return True



# ----------------test------------------
#           5
#          / \
#         3   9
#        / \ / \
#       1  4 7 10

def test():
    btree = BinaryTreeNode(5)
    btree.setLeft(3)
    btree.setRight(9)
    btree.left.setLeft(1)
    btree.left.setRight(4)
    btree.right.setLeft(7)
    btree.right.setRight(10)

    print isBST1(btree)         # True
    print isBST2(btree)         # True



if __name__ == "__main__":
    test()
