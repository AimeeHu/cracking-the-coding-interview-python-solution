from classes.BinaryTreeNode import *


def findNextNode(node):
    if node is None:
        return None

    # Find the leftmost node of right subtree    
    if node.right is not None:
        return findLeftMost(node.right)

    # Go up until the node is on left substree of that parent
    else:
        return findParentToWhomeIsLeft(node)


def findLeftMost(node):
    current = node
    while current.left is not None:
        current = node.left
    return current

def findParentToWhomeIsLeft(node):
    current = node
    parent = current.parent
    while parent is not None and parent.left is not current:
        parent = parent.parent
        current = current.parent
    return parent



# ----------------test------------------
#           5
#          / \
#         3   7
#        / \   \
#       1   4   8
#      /
#     0
#
# In-order traversal: 0 1 3 4 5 7 8

def test():
    n5 = BinaryTreeNode(5)
    n5.setLeft(3)
    n3 = n5.left
    n5.setRight(7)
    n7 = n5.right
    n3.setLeft(1)
    n1 = n3.left
    n3.setRight(4)
    n4 = n3.right  
    n7.setRight(8)
    n8 = n7.right
    n1.setLeft(0)
    n0 = n1.left
        
    for node in [n5, n3, n7, n1, n4, n8, n0]:
        next = findNextNode(node)
        print node.value, "next:", next.value if next is not None else next


if __name__ == "__main__":
    test()