class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def setLeftChild(self, leftvalue):
        leftnode = TreeNode(leftvalue)
        self.left = leftnode
        if leftnode != None:
            leftnode.parent = self

    def setRightChild(self, rightvalue):
        rightnode = TreeNode(rightvalue)
        self.right = rightnode
        if rightnode != None:
            rightnode.parent = self

# print order: middle left right
def printTree(tree):
    if tree != None: 
        print tree.value
        print tree.value, "left:",
        printTree(tree.left)
        print ""
        print tree.value, "right:",
        printTree(tree.right)   



def arrayToBST(array, start, end):
    if start > end:
        return None
    middle = (start + end)/2 
    tree = TreeNode(array[middle])
    tree.left = arrayToBST(array, start, middle-1)
    tree.right = arrayToBST(array, middle+1, end)
    return tree


# --------------test--------------
if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6]
    tree = arrayToBST(array, 0, len(array)-1)
    printTree(tree)
