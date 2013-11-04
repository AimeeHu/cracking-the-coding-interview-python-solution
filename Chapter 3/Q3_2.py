class StackWithMin:
    
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, value):
        self.stack.append(value)
        if len(self.min) == 0 or value <= self.min[-1]:
            self.min.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        data = self.stack.pop()
        if data == self.min[-1]:
            self.min.pop()
        return data

    def getMin(self):
        if len(self.min)==0:
            return None
        return self.min[-1]


#--------------test-----------------
from random import randrange
Stack = StackWithMin()
for i in range(15):
    data = randrange(1,100)
    Stack.push(data)
    print data,
print ""

for i in range(15):
    print "Poped", Stack.pop(), " New min", Stack.getMin()


