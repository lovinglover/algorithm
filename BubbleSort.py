# Author:Jack

import numpy as np


# 冒泡排序
def Bubble_Sort(value):
	for i in range(len(value) - 1):
		for j in range(len(value) - 1):
			if value[j] > value[j + 1]:
				value[j], value[j + 1] = value[j + 1], value[j]
	print('冒泡排序:', end='')
	print(value)

# 主函数
if __name__ == '__main__':
	list = np.random.randint(200, size=10)
	print('随机列表:', end='')
	print(list)
	Bubble_Sort(list)
