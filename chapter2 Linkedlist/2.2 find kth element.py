from linkedlist import *

ll = linked_list()

for x in xrange(0,11):
    ll.add_node(x)   




def main():
    k = 4


    fast_node = ll.head
    slow_node = ll.head
    for x in xrange(0,k):
        fast_node = fast_node.next

    if fast_node == None:
        print 'k is larger than the list length'
    else:
        while fast_node:
            slow_node = slow_node.next
            fast_node = fast_node.next
        
        print slow_node.data 


    

if __name__ == '__main__':
    main()