from linkedlist import *

ll = linked_list()

ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
ll.add_node(6)
ll.add_node(7)
ll.add_node(8)
ll.add_node(9)
ll.add_node(10)
ll.add_node(11)
ll.add_node(12)

def solution(node):
    if node is ll.head:
        ll.head = ll.head.next
    elif node is ll.tail:
        cur_node = ll.head
        while cur_node.next.next:
            cur_node = cur_node.next
        ll.tail = cur_node
        ll.tail.next = None
    else:
        node.data = node.next.data
        node.next = node.next.next

def main():

    solution(ll.head)
    solution(ll.tail)
    cur_node = ll.head
    cur_node = cur_node.next
    cur_node = cur_node.next
    data = cur_node.data
    solution(cur_node)


    assert (ll.head.data == 2),"wrong"
    assert (ll.tail.data == 11),"wrong"
    assert (ll.find_node(data) == False),"wrong"

    print 'all passed'

if __name__ == '__main__':
    main()