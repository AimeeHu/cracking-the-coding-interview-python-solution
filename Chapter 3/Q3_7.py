from collections import deque

# Using a deque datatype as an implementation of queue

class Animal(object):

    def __init__(self, name):
        self.name = name
        self.order = -1

    def __str__(self):
        return "Animal: " + self.name


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def __str__(self):
        return "Cat: " + self.name

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def __str__(self):
        return "Dog: " + self.name



class AnimalQueue(object):
    
    def __init__(self):
        self.Dog = deque()
        self.Cat = deque()
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1 
        if isinstance(animal, Cat):
            self.Cat.append(animal)
        else:
            self.Dog.append(animal)

    def dequeueAny(self):
        if len(self.Dog) == 0:
            return self.dequeueCat()
        if len(self.Cat) == 0:
            return self.dequeueDog()
        if self.Dog[0].order < self.Cat[0].order:
            return self.Dog.popleft()
        else:
            return self.Cat.popleft()

    def dequeueDog(self):
        return self.Dog.popleft() if len(self.Dog) != 0 else None


    def dequeueCat(self):
        return self.Cat.popleft() if len(self.Cat) != 0 else None



#------------------test--------------------
if __name__ == "__main__":
    animals = AnimalQueue()
    animals.enqueue(Cat("cat_1"))
    animals.enqueue(Cat("cat_2"))
    animals.enqueue(Cat("cat_3"))
    animals.enqueue(Dog("dog_1"))
    animals.enqueue(Cat("cat_4"))
    animals.enqueue(Dog("dog_2"))
    print animals.dequeueAny()      # Cat: cat_1
    print animals.dequeueDog()      # Dog: dog_1
    print animals.dequeueCat()      # Cat: cat_2
    for i in range(3):
        print animals.dequeueAny()  # Cat: cat_3
                                    # Cat: cat_4
                                    # Dog: dog_2
    print animals.dequeueAny()      # None

