from linkedlist import *

linkedlist_one = linked_list()
linkedlist_two = linked_list()


def main():
	linkedlist_one.generateList(4)
	linkedlist_one.list_print()
	linkedlist_two.generateList(4)
	linkedlist_two.list_print()
	result = linked_list()
	cur_node = linkedlist_one.head
	cur_node_two = linkedlist_two.head
	carry = 0
	while cur_node:
		tmp = cur_node.data + cur_node_two.data + carry
		carry = 0
		if tmp > 9:
			carry = 1 
			tmp = tmp - 10
		result.add_node(tmp)
		cur_node_two =cur_node_two.next
		cur_node = cur_node.next

	if carry == 1:
		result.add_node(1)

	result.list_print()



if __name__ == '__main__':
	main()