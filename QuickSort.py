# Author:Jack

import numpy as np

def QuickSort(list, L, R):
	if L < R:
		H = Partition(list, L, R)
		QuickSort(list, L, H[0] - 1)
		QuickSort(list, H[1], R)

def Partition(list, L , R):
	less = L - 1
	more = R + 1
	num = list[np.random.randint(L, R)]
	#随机快排
	while L < more:
		if list[L] == num:
			L += 1
		elif list[L] < num:
			list[L], list[less + 1] = list[less + 1], list[L]
			less += 1
			L += 1
		else:
			list[L], list[more - 1] = list[more - 1], list[L]
			more -= 1
	return [less + 1, more]

if __name__ == '__main__':
	list = np.random.randint(200, size=10)
	print('随机列表:', end='')
	print(list)
	QuickSort(list, 0, len(list) - 1)
	print('快速排序:',end='')
	print(list)