""" Implement a Queue class using two stacks."""

class MyQueue:

    def __init__(self):
        self.stackOldest = Stack()
        self.stackNewest = Stack()

    def push(self, value):
        self.stackNewest.push(value)

    def pop(self):
        if len(self.stackOldest.stack) == 0:
            self.moveToOldest()
        return self.stackOldest.pop()
    
    def peek(self):
        if len(self.stackOldest.stack) == 0:
            self.moveToOldest()
        return self.stackOldest.peek()

    def moveToOldest(self):
        while len(self.stackNewest.stack):
            self.stackOldest.push(self.stackNewest.pop())

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return None if len(self.stack) == 0 else self.stack.pop()

    def peek(self):
        return None if len(self.stack) == 0 else self.stack[-1]



#----------------test-------------------
if __name__ == "__main__":
    queue = MyQueue()
    for i in range(1,5):
        queue.push(i)
        print "Enqueued",i
        queue.push(i*2)
        print "Enqueued", i*2
        data = queue.pop()
        print "Dequeued", data

