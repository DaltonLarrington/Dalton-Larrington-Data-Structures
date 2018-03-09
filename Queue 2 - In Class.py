
class ListItem:

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

        li = ListItem(value, self.length)
        
        #note    
        
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
            output += ", " + str(ci.value)
        return output  


newList = MyList()
newList.add(5)
newList.add(7)
newList.add(True)
newList.add("Alpha")
newList.add(-1)
newList.add("hello")
print(newList)

