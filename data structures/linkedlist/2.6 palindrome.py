# implement a function to check if a linked list is a palindrome
from linkedlist import *

def main():
	ll = linked_list()

	ll.add_node(1)
	ll.add_node(2)
	ll.add_node(3)
	ll.add_node(3)
	ll.add_node(2)
	ll.add_node(1)

	slow_node = ll.head
	fast_node = ll.head
	stack = []

	while fast_node is not None and fast_node.next is not None:
		stack.append(slow_node.data)
		slow_node = slow_node.next
		fast_node = fast_node.next.next


	#deal with when linkedlist is odd num
	if fast_node is not None:
		slow_node = slow_node.next

	while slow_node is not None:
		if(stack.pop() != slow_node.data):
			print("not palindrome")
			return False
		slow_node = slow_node.next
	print("palindrome")		
	return True

main()
	


