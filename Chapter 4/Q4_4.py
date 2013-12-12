from classes.BinaryTreeNode import *

class LinkedListNode:
	
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def addNode(self, value):
		node = LinkedListNode(value)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node



# Using breadth first search
def createLevelLinkedlist1(root):
	result = []
	parents = LinkedList()
	if root is not None:
		parents.addNode(root)
	while parents.head is not None:
		result.append(parents)
		children = LinkedList()
		current = parents.head
		while current is not None:	
			if current.value.left is not None:
				children.addNode(current.value.left)
			if current.value.right is not None:
				children.addNode(current.value.right)
			current = current.next
		parents = children
	return result


	
# Using deep first search
def createLevelLinkedlist2(root, result = None, deep = 0):
	if result is None:
		result = []
	if root is None:
		return result
	if deep == len(result):
		L = LinkedList()
		result.append(L)
	result[deep].addNode(root)
	createLevelLinkedlist2(root.left, result, deep+1)
	createLevelLinkedlist2(root.right, result, deep+1)
	return result



# ------------------test---------------------------
# A binary search tree
#     5
#    / \
#   3   6
#  / \   \
# 1   4   8
#  \
#   2

def test():
	# create a tree
	bstree = BinaryTreeNode(5)
	bstree.setLeft(3)
	bstree.left.setLeft(1)
	bstree.left.left.setRight(2)
	bstree.left.setRight(4)
	bstree.setRight(6)
	bstree.right.setRight(8)
    
    # create a list of linkedlists containing tree nodes in each level
	result1 = createLevelLinkedlist1(bstree)
	result2 = createLevelLinkedlist2(bstree)
	
	print "Test for method 1:"
	printTnodeLinkedlistArray(result1)
	print "Test for method 2:"
	printTnodeLinkedlistArray(result2)


def printTnodeLinkedlistArray(resultlist):
	for i, llist in enumerate(resultlist):
		print i, "level:",
		p = llist.head
		while p is not None:
			print p.value.value,
			p = p.next
		print ""


if __name__ == "__main__":
	test()


	


		

		
		
		