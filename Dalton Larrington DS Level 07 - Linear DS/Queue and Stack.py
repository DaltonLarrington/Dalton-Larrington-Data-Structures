#Queues and Stacks
#Programmer: Dalton Larrington
#Date: 4-5-2018

class Queue:

    def __init__(self, value, index):

        self.value = value
        self.index = index
        self.next = None
        self.prev = None

class MyList:

    def __init__(self):

        self.head = None
        self.tail = None
        self.length = 0

    def add(self, value):

         li = Queue(value, self.length)

         if self.length == 0:
            self.head = li

         else:
            li.prev = self.tail
            self.tail.next = li

         self.tail = li
         self.length += 1

    def __str__(self):

        output = str(self.head.value)

        ci = self.head

        for i in range(self.length - 1):
            ci = ci.next
            output += "," + str(ci.value)
        return output

newList = MyList()
newList.add(7)
newList.add(3)
newList.add(14)
newList.add(1)
newList.add(21)
newList.add(0)
newList.add(0)
newList.add(56)
print("Queue: ", newList)

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

        
s = Stack()
s.push(7)
s.push(3)
s.push(14)
s.push(1)
s.push(21)
s.push(0)
s.push(0)
s.push(56)
print("Stack: ", s.pop())

    
