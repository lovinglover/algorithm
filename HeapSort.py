# Author:Jack
import numpy as np


def HeapSort(list):
	HeapInsert(list)
	heapsize = len(list) - 1
	head = 0
	while heapsize > 0:
		list[head], list[heapsize] = list[heapsize], list[head]
		i = head
		while (2 * i + 2) < heapsize:
			if list[2 * i + 1] > list[2 * i + 2] and list[2 * i + 1] > list[i]:
				list[i], list[2 * i + 1] = list[2 * i + 1], list[i]
				i = 2 * i + 1
			elif list[2 * i + 2] > list[2 * i + 1] and list[2 * i + 2] > list[i]:
				list[i], list[2 * i + 2] = list[2 * i + 2], list[i]
				i = 2 * i + 2
			else:
				break
		heapsize -= 1
		if heapsize == 1:
			if list[0] > list[1]:
				list[0], list[1] = list[1], list[0]
			heapsize -= 1
	print('堆排序:', end='')
	print(list)


def HeapInsert(list):
	for i in range(1, len(list)):
		while int((i - 1)/2) >= 0:
			if list[i] > list[int((i - 1)/2)]:
				list[i], list[int((i - 1)/2)] = list[int((i - 1)/2)], list[i]
				i = int((i - 1)/2)
			else:
				break


if __name__ == '__main__':
	list = np.random.randint(200, size=10)
	print('随机列表:', end='')
	print(list)
	HeapSort(list)

