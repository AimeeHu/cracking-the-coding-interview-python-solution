class BTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def setLeftChild(self, leftnode):
        self.left = leftnode
        if leftnode != None:
            leftnode.parent = self

    def setRightChild(self, rightnode):
        self.right = rightnode
        if rightnode != None:
            rightnode.parent = self



# O(n^2) Naive algorithms
def isBalanced(root):
    if root == None:
        return True
    heightDiff = getHeight(root.left) - getHeight(root.right)
    if abs(heightDiff) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)

def getHeight(root):
    if root == None:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1



# Another implementation with O(n) 
def isBalanced_2(root):
    return checkHeight(root)[0]

def checkHeight(root):
    if root == None:
        return True, 0
    isLeftBalanced, leftHeight = checkHeight(root.left)
    isRightBalanced, rightHeight = checkHeight(root.right)
    heightDiff = leftHeight - rightHeight
    treeHeight = max(leftHeight, rightHeight) + 1
    return abs(heightDiff) <= 1 and isLeftBalanced and isRightBalanced, treeHeight



#-------------------test-----------------
if __name__ == "__main__":
    btree = BTreeNode(1)
    btree.setLeftChild(BTreeNode(2))
    btree.setRightChild(BTreeNode(3))
    btree.right.setLeftChild(BTreeNode(4))
    btree.right.left.setLeftChild(BTreeNode(5))
    print isBalanced(btree)                     # False
    print isBalanced_2(btree)                   # False