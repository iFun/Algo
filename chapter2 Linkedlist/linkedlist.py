class node:
 
    def __init__(self):
        self.next = None
        self.data = None

class linked_list:
 
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self,data):
        new_node = node()
        new_node.data = data

        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def list_print(self):
        if self.head == None:
            print 'linked_list is empty'
        cur_node = self.head
        while cur_node:
            print (str(cur_node.data) + '->'),
            cur_node = cur_node.next
        print ''




