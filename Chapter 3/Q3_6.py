class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return None if self.isEmpty() else self.stack.pop()

    def peek(self):
        return None if self.isEmpty() else self.stack[-1]


    def isEmpty(self):
        return len(self.stack) == 0


# Sort stack without using other data structure except Stack
def sortStack(s):
    sortedStack = Stack()
    while not s.isEmpty():
        data = s.pop()      
        while (not sortedStack.isEmpty()) and sortedStack.peek() < data:
            stack.push(sortedStack.pop())
        sortedStack.push(data)
    return sortedStack



#---------------test---------------
if __name__ == '__main__':
    from random import randrange
    stack = Stack()
    for i in range(10):
        stack.push(randrange(0,100))
    print "Before sorting",stack.stack
    print "After sorting ", sortStack(stack).stack


