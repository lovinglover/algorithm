# Author:Jack
import numpy as np

def HeapInsert(list):
	#生成大根堆
	for i in range(1, len(list)):
		while int((i - 1)/2) >= 0:
			if list[i] > list[int((i - 1)/2)]:
				list[i], list[int((i - 1)/2)] = list[int((i - 1)/2)], list[i]
				i = int((i - 1)/2)
			else:
				break
	print(list)

if __name__ == '__main__':
	list = np.random.randint(200, size=10)
	print('随机列表：',end='')
	print(list)
	HeapInsert(list)
