# Author:Jack

import random



def Classify(list,num):
	'''
	Realize the following operation：
		area 0~x     <= num
		area x~(N-1) > num
	:param list:
	:param num:
	:return:
	'''
	x = -1
	for i in range(len(list)):
		if list[i] <= num:
			list[i], list[x + 1] = list[x + 1], list[i]
			x += 1
	print('after: ',end='')
	print(list)

if __name__ == '__main__':
	list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
	num = 11
	random.shuffle(list)
	print('before:',end='')
	print(list)
	Classify(list,num)

