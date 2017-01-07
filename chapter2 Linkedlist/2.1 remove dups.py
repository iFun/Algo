# 1 remove duplicate from an unsorted linked list
# 2 return kth to last implement ana lgorithm to find the   last element
# 3 delete middle node delete a node with only access to that node
# 6 check if a linked list is a palindrome


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
        
        print 'successful added new node'

    def list_print(self):
        if self.head == None:
            print 'linked_list is empty'
        cur_node = self.head
        while cur_node:
            print (str(cur_node.data) + '->'),
            cur_node = cur_node.next
    def remove_node():
        pass

ll = linked_list()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

ll.list_print()
        
        