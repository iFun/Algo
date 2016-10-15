class Node:

    def __init__(self, data):
        self.next = None
        self.data = data

    def __str__(self):
        return self.data

    def getData(self):
        return self.data

    def setData(self,newdata):
        self.data = newdata

class Linklist:
  
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

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
            self.size +=1
    def search(self, data):
        current = self.head
        if current is None:
            print 'empty link list'
        elif current.next is None:
            return current.data == data
        else:
            while current:
                if current.data == data:
                    return True
                current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        if current is None:
            return False
 
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
            

        self.head = prev
        return True

    def printList(self):
        current = self.head
        while current:
            print current 
            current = current.next

        print ''

linklist = Linklist()

linklist.addNode('a')
if linklist.search('a') is False:
    print 'asdasd'
else:
    print 'haha'
linklist.addNode('b')
linklist.addNode('c')
linklist.addNode('d')
linklist.addNode('e')
linklist.addNode('f')





linklist.reverse()


        