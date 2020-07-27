# Author:Jack

import random

def Classify(list, num):
	'''
	Realize the following operation：
		area 0~less     < num
		area less~more  = num
		area more~(N-1) > num
	:param list:
	:param num:
	:return:
	'''
	less = -1
	more = len(list)
	i = 0
	while i < more:
		if list[i] == num:
			i += 1
		elif list[i] < num:
			list[i], list[less + 1] = list[less + 1], list[i]
			less += 1
			i += 1
		else:
			list[i], list[more - 1] = list[more - 1], list[i]
			more -= 1
	print('after: ',end='')
	print(list)

if __name__ == '__main__':
	list = [2, 4, 6, 8, 10, 11, 11, 11, 12, 14, 16, 18, 20]
	num = 11
	random.shuffle(list)
	print('before:',end='')
	print(list)
	Classify(list, num)