# Author:Jack

import numpy as np

# def Insert_Sort(list):
# 	for i in range(1,len(list)):
# 		for j in range(i, 0, -1):
# 			if list[j] < list[j - 1]:
# 				list[j],list[j - 1] = list[j - 1],list[j]
# 	print('插入排序:', end='')
# 	print(list)

def Insert_Sort(list):
	for i in range(1,len(list)):
		cur = list[i]
		j = i - 1
		while j>=0 and list[j]>cur:
			list[j+1] = list[j]
			j -= 1
		list[j+1] = cur
	print('插入排序:', end='')
	print(list)


if __name__ == '__main__':
	list = np.random.randint(200, size=10)
	print('随机列表:', end='')
	print(list)
	Insert_Sort(list)
