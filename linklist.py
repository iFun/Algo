class Node:

    def __init__(self, data):
        self.next = None
        self.data = data

    def getData(self):
        return self.data

    def setData(self,newdata):
        self.data = newdata

class Linklist:
  
    def __init__(self):
        self.head = None

    def setHead(self, newhead):
        self.head = newhead

    def addNode(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = temp
    def search(self, data):
        current = self.head
        if current is None:
            print 'empty link list'
        else:
            while current:
                if current.data == data:
                    return True
                current = current.next
        return False
            
                

    def printList(self):
        current = self.head
        while current:
            print (current.data + '->'),;
            current = current.next

linklist = Linklist()
linklist.addNode('a')
linklist.addNode('b')
linklist.addNode('c')
linklist.addNode('d')
if linklist.search('c'):
    print 'found it'
else:
    print 'does not exist'

linklist.printList()


        