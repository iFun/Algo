from linkedlist import *

ll = linked_list()


def main():
	ll.generateList(15)
	ll.list_print()
	partition = 10

	left_head = None
	right_head = None
	tmp_right = None
	cur_node = ll.head

	while cur_node:
		if cur_node.data < partition:
			if left_head == None:
				left_head = cur_node
				ll.head = left_head #need to set linkedlist head
			else:
				left_head.next = cur_node
				left_head = left_head.next
		
		else:
			if right_head == None:
				right_head = cur_node
				tmp_right = right_head

			else:
				tmp_right.next = cur_node
				tmp_right = tmp_right.next
		
		cur_node = cur_node.next


	tmp_right.next = None #neet to set to None otherwise get loop linkedlist
	left_head.next = right_head

	ll.list_print()


if __name__ == '__main__':
    main()