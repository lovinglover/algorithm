# Author:Jack

import numpy as np

def Select_Sort(list):
	for i in range(len(list) - 1):
		small = list[i]
		j = i
		index = i
		while j<len(list):
			if small > list[j]:
				small,index = list[j],j
			j += 1
		list[index] = list[i]
		list[i] = small
	print('选择排序:', end='')
	print(list)



if __name__ == '__main__':
	list = np.random.randint(200, size=10)
	print('随机列表:', end='')
	print(list)
	Select_Sort(list)