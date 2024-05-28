#!/usr/bin/python3


class Node():
	"""
	.. _Node:

	An element in the linked list.

	:ivar key: the value stored on the node
	:ivar prev_ptr: pointer to the node to the left
	:ivar next_ptr: pointer to the node to the right
	"""
	
	def __init__(self, key=None,prev_ptr=None, next_ptr=None):
		"""
		Create a new Node object.

		:param key: the value to be stored on the element.
		:type key: str
		:param prev_ptr: a pointer to the left node, or None.
		:type prev_ptr: Node
		:param next_ptr: a pointer to the right node, or None.
		:type next_ptr: Node
		"""
		self.key=key
		self.prev_ptr=prev_ptr
		self.next_ptr=next_ptr

	def __str__(self):
		return str(self.key)

class LinkedList():
	"""
	.. _LinkedList:

	A doubly-linked list implementation """

	def __init__(self):
		self.head = None 
		self.length = 0

	def is_empty(self):
		""" Check for empty list.

		:return: True if the list is empty, False otherwise.
		:rtype: bool
		"""
		return self.head is None

	def insert(self, node):
		""" Insert a new element in the list.
		
		:param node: a node element
		:type node: Node
		"""
		node.next_ptr = self.head
		if  self.head is not None:
			self.head.prev_ptr = node
		self.head = node	
		self.length += 1

	def search(self,k):
		""" Search the list for a key.

		:param k: a key value 
		:type k: str
		:return: the first node containing the key
		:rtype: Node
		"""
		node = self.head
		while node is not None and node.key != k:
			node = node.next_ptr
		return node

	def delete(self, node):
		""" Delete a node from the list.

		:param node: a node reference
		:type node: Node
		"""
		if node is None:
			return
		if node.prev_ptr is not None:
			node.prev_ptr.next_ptr = node.next_ptr
		else:
			self.head = node.next_ptr
		if node.next_ptr is not None:
			node.next_ptr.prev_ptr = node.prev_ptr
		self.length -= 1

	def __str__(self):
		""" Return a string representation of the list 
		:return: a string representation of the list, suitable for use in a `print` statement
		:rtype: str
		"""

		output = ' '+str(self.head)
		next_el = self.head.next_ptr
		while next_el is not None:
			output += ( ' -> {}'.format(next_el) )
			next_el = next_el.next_ptr
		return output


