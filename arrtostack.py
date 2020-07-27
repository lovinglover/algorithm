# Author:Jack

class Stack():
	def __init__(self, size):
		self.size = size
		self.top = 0
		self.stack = []

	def push(self, x):
		if self.isFull():
			print("Stack is full, you can't do this")
		else:
			self.stack.append(x)
			self.top += 1

	def pop(self):
		if self.isEmpty():
			print("Stack is empty, you can't do this")
		else:
			print(self.stack.pop())
			self.top -= 1

	def isFull(self):
		return self.top == self.size

	def isEmpty(self):
		return self.top == 0

	def show(self):
		print(self.stack)


if __name__ == '__main__':
	stack = Stack(10)
	for i in range(10):
		stack.push(i * 2)
	stack.show()
	for j in range(5):
		stack.pop()
	stack.show()
	stack.push(100)
	stack.show()