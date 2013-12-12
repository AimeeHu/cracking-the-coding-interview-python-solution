from classes.BinaryTreeNode import *
from collections import deque

# Create an algorithm to decide if T2 is a subtree of T1

def containTree(T1, T2):
    if T2 is None:
        return True
    queue = deque()
    if T1 is not None:
        queue.append(T1)
    while len(queue) != 0:
        node = queue.popleft()
        if node.value == T2.value:
            if matchTree(node, T2):
                return True
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return False


def matchTree(n1, n2):
    if n1 == None and n2 == None:
        return True
    if n1 == None or n2 == None:
        return False
    if n1.value != n2.value:
        return False
    return matchTree(n1.left, n2.left) and matchTree(n1.right, n2.right)






# ----------------test-----------------
# T1          1            T2        2
#            / \                    / \
#           2   3                  4   2
#          / \   \                    / 
#         4   2   2                  8   
#            / 
#           8   
#               
              

def main():
    T1 = BinaryTreeNode(1)
    T1.setLeft(2)
    T1.setRight(3)
    T1.left.setLeft(4)
    T1.left.setRight(2)
    T1.right.setRight(2)
    T1.left.right.setLeft(8)
    T2 = BinaryTreeNode(2)
    T2.setLeft(4)
    T2.setRight(2)
    T2.right.setLeft(8)

    print containTree(T1, None)          # True
    print containTree(None, T2)          # False
    print containTree(T1, T2)            # True
    print containTree(T1, BinaryTreeNode(4))    # True


if __name__ == "__main__":
    main()
