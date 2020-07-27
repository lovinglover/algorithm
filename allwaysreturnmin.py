# Author:Jack


class Stack():
	def __init__(self, size):
		self.size = size
		self.top = 0
		self.Data = []
		self.Min = []

	def push(self, x):
		if self.isFull():
			print("Stack is full, you can't do this")
		else:
			self.Data.append(x)
			if not self.Min or x < self.Min[-1]:
				self.Min.append(x)
			else:
				self.Min.append(self.Min[-1])
			self.top += 1

	def pop(self):
		if self.isEmpty():
			print("Stack is empty, you can't do this")
		else:
			print(self.Data.pop())
			self.Min.pop()
			self.top -= 1

	def getMin(self):
		print(self.Min[-1])

	def isFull(self):
		return self.top == self.size

	def isEmpty(self):
		return self.top == 0

	def show(self):
		print(self.Data)


if __name__ == '__main__':
	stack = Stack(4)
	stack.push(5)
	stack.push(4)
	stack.push(9)
	stack.push(3)
	stack.show()
	stack.getMin()
	stack.pop()
	stack.show()
	stack.getMin()