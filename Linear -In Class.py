#Linear Data Structure

class LinearItem:

    def __init__(self, value):

        self.val = value
        self.next = None
        self.prev = None

    def setNext(self, item):
        self.Next = item

    def setPrev(self, item):
        self.Prev = item
        
        
    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getValue(self):
        return self.val
        
    
class Linear:

    def __init__(self):

        self.first = None
        self.last = None
        self.length = 0

    def add(self, item):

        if self.length == 0:
            self.first, self.last = LinearItem(item), LinearItem(item)
            self.length += 1

        else:
            self.Last.setNext(newItem)
            newItem.setPrev(self.last)
            self.last = newItem
            
