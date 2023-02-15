"""Basic Data Structures"""
"""Implementation of the stack data structure"""

"""A stack is an ordered collection of items where addition and removal of items
always happens from the same end.(top). The most recently added item us the one
that is removed first. This ordering principle also known as LIFO, last in first out
"""

"""The Stack ADT is defined by the following structure and operations.
Stack() -- Creates a new stack that is empty. it needs no parameters and returns a new stack.
push(item) -- Adds a new item to the top of the stack. It needs the item and returms nothing
pop() removes the top item from the stack. Needs no parameters and returns nothing
peek() -- returns the topmost item on the stack. Needs no parameters and the stack is not modified
is_empty -- tests whether to see if the stack is empty. Needs no parameters and returns a boolean value
size() -- returns an integer. Needs no parameters."""

#Complete implementation of a Stack.

class Stack():
	def __init__(self):
		self.items = []

	def is_empty(self):
		if self.items == []:
			return True
		else:
			return False


	def push(self, item):
		self.items.append(item)


	def pop(self):
		try:
			return self.items.pop()
		except Exception as e:
			raise ValueError(e)



	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)

	def __repr__(self):
		output = "T["
		for i in range(1, len(self.items)+1):
			output = output + str(f"{self.items[-i]},")
		output = output + "]B"
		return output


""" Implementation of Queue"""
"""A queue is an ordered collection of items where the addition of new items happens at one end
known as the rear. and the removal happens at the other end commonly known as the "front".

The ordering principle is known as the FIFO. (first in first out).

Operations
q.is_empty()
q.enqueue(4)
q.enqueue('dog')
q.enqueue -- Adds an element to the end of the stack
q.size() -- Returns size of the queue
q.dequeue() -- removes the element in front of the queue
"""


class Queue():
	"""Implementation of the Queue ADT"""
	def __init__(self):
		self.items = []


	def is_empty(self):
		return self.items == []


	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

