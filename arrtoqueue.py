# Author:Jack

class Queue():
	def __init__(self, size):
		self.size = size
		self.cur_size = 0
		self.start = 0
		self.end = 0
		self.queue = [0] * self.size

	def push(self, x):
		if self.isFull():
			print("Queue is full, you can't do this")
		else:
			self.queue[self.start] = x
			self.start = 0 if self.start == self.size - 1 else self.start + 1
			self.cur_size += 1

	def out(self):
		if self.isEmpty():
			print("Queue is empty, you can't do this")
		else:
			print(self.queue[self.end])
			self.end = 0 if self.end == (self.size - 1) else self.end + 1
			self.cur_size -= 1

	def isFull(self):
		return self.cur_size == self.size

	def isEmpty(self):
		return self.cur_size == 0

	def show(self):
		out = []
		if self.end >= self.start:
			out.extend(self.queue[self.end:])
			out.extend(self.queue[:self.start])
		else:
			out.extend(self.queue[self.end:self.start])
		print(out)



if __name__ == '__main__':
	queue = Queue(5)
	for i in range(5):
		queue.push(i * 2)
	queue.show()
	for i in range(3):
		queue.out()
	queue.show()
