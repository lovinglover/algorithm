# Author:Jack
import numpy as np

def GetMaxDifference(list):
	#创建 N + 1 个桶，用3个list代替，分别存放最大值、最小值、是否为空的判断
	Max = [0] * (len(list) + 1)
	Min = [0] * (len(list) + 1)
	bucket = [False] * (len(list) + 1)
	Min_value = min(list)
	Max_value = max(list)
	diff = []
	for i in list:
		index = int((i - Min_value) * len(list) / (Max_value - Min_value))
		Max[index] = Max[index] if i < Max[index] else i
		if Min[index] == 0:
			Min[index] = i
		else:
			Min[index] = Min[index] if i > Min[index] else i
		bucket[index] = True

	for i in range(1, len(list) + 1):
		if bucket[i]:
			j = i - 1
			while not bucket[j]:
				j -= 1
			diff.append((Min[i] - Max[j]))
		else:
			continue
	return max(diff)


# for test
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
	list_sort = []
	print('随机数组:', end='')
	print(list)
	list_sort.extend(list)
	QuickSort(list_sort, 0, len(list_sort) - 1)
	print('排序后:', end='')
	print(list_sort)
	Max_Diff = GetMaxDifference(list)
	print('最大差值:', end='')
	print(Max_Diff)