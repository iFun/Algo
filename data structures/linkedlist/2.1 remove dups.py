from linkedlist import *

ll = linked_list()

ll.add_node(2)
ll.add_node(2)
ll.add_node(6)
ll.add_node(4)
ll.add_node(2)
ll.add_node(9)
ll.add_node(0)
ll.add_node(1)
ll.add_node(4)
ll.add_node(4)
ll.add_node(4)
ll.add_node(4)
ll.add_node(9)
ll.add_node(100)

def main():
    hashtable = {}
    prev_node = None
    cur_node = ll.head


    while cur_node.next:
        if cur_node.data in hashtable:
            prev_node.next = cur_node.next
        else:
            hashtable[cur_node.data] = True
            prev_node = cur_node
  
        cur_node = cur_node.next

    if cur_node.data in hashtable:
        ll.tail = prev_node

        ll.tail.next = None

    ll.list_print()




if __name__ == '__main__':
    main()

        

