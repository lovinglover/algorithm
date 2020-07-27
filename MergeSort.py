# Author:Jack

import numpy as np

def Merge_Sort(list, L, R):
	if L < R:
		mid = L + ((R - L) >> 1)
		Merge_Sort(list, L, mid)
		Merge_Sort(list, mid+1, R)
		return Merge(list, L, R, mid)

def Merge(list, L, R, M):
	merged = []
	l = []
	r = []
	l.extend(list[L:(M+1)])
	r.extend(list[(M+1):(R+1)])
	i,j = 0,0
	while i<len(l) and j<len(r):
		if l[i] <= r[j]:
			merged.append(l[i])
			i += 1
		else:
			merged.append(r[j])
			j += 1
	merged.extend(l[i:])
	merged.extend(r[j:])
	for k in range(len(merged)):
		list[L+k] = merged[k]

if __name__ == '__main__':
	list = np.random.randint(200, size=10)
	print('随机列表:', end='')
	print(list)
	Merge_Sort(list, 0, len(list)-1)
	print('归并排序:', end='')
	print(list)