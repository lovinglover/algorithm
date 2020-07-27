# Author:Jack

import numpy as np

class Median():
	def __init__(self):
		self.Max_arr = []
		self.Min_arr = []

	# def findMedianSortedArrays(self, nums1, nums2):
	# 	num = nums1 + nums2
	# 	self.Max_arr = []
	# 	self.Min_arr = []
	# 	for item in num:
	# 		self.push(item)
	# 	print(self.Get_Median())

	def push(self, x):
		if  not self.Min_arr or x < self.Min_arr[0]:
			self.Max_arr.append(x)
			self.Build_B_Heap()
		else:
			self.Min_arr.append(x)
			self.Build_S_Heap()

		if len(self.Max_arr) - len(self.Min_arr) > 1:
			self.Max_arr[0], self.Max_arr[-1] = self.Max_arr[-1], self.Max_arr[0]
			self.Min_arr.append(self.Max_arr.pop())
			self.Build_S_Heap()
			self.B_Heapify()
		if len(self.Min_arr) - len(self.Max_arr) > 1:
			self.Min_arr[0], self.Min_arr[-1] = self.Min_arr[-1], self.Min_arr[0]
			self.Max_arr.append(self.Min_arr.pop())
			self.Build_B_Heap()
			self.S_Heapify()

	def Build_B_Heap(self):
		#生成大根堆
		i = len(self.Max_arr) - 1
		while int((i - 1)/2) >= 0:
			if self.Max_arr[i] > self.Max_arr[int((i - 1)/2)]:
				self.Max_arr[i], self.Max_arr[int((i - 1)/2)] = self.Max_arr[int((i - 1)/2)], self.Max_arr[i]
				i = int((i - 1)/2)
			else:
				break

	def B_Heapify(self):
		i = 0
		while (2 * i + 2) < len(self.Max_arr):
			if self.Max_arr[2 * i + 1] >= self.Max_arr[2 * i + 2] and self.Max_arr[2 * i + 1] >= self.Max_arr[i]:
				self.Max_arr[i], self.Max_arr[2 * i + 1] = self.Max_arr[2 * i + 1], self.Max_arr[i]
				i = 2 * i + 1
			elif self.Max_arr[2 * i + 2] >= self.Max_arr[2 * i + 1] and self.Max_arr[2 * i + 2] >= self.Max_arr[i]:
				self.Max_arr[i], self.Max_arr[2 * i + 2] = self.Max_arr[2 * i + 2], self.Max_arr[i]
				i = 2 * i + 2
			else:
				break
		if len(self.Max_arr) == 2:
			(self.Max_arr[0], self.Max_arr[-1]) = (self.Max_arr[0], self.Max_arr[-1]) if self.Max_arr[0] > \
							  self.Max_arr[-1] else (self.Max_arr[-1], self.Max_arr[0])



	def Build_S_Heap(self):
		#生成小根堆
		i = len(self.Min_arr) - 1
		while int((i - 1)/2) >= 0:
			if self.Min_arr[i] < self.Min_arr[int((i - 1)/2)]:
				self.Min_arr[i], self.Min_arr[int((i - 1)/2)] = self.Min_arr[int((i - 1)/2)], self.Min_arr[i]
				i = int((i - 1)/2)
			else:
				break

	def S_Heapify(self):
		i = 0
		while (2 * i + 2) < len(self.Min_arr):
			if self.Min_arr[2 * i + 1] <= self.Min_arr[2 * i + 2] and self.Min_arr[2 * i + 1] <= self.Min_arr[i]:
				self.Min_arr[i], self.Min_arr[2 * i + 1] = self.Min_arr[2 * i + 1], self.Min_arr[i]
				i = 2 * i + 1
			elif self.Min_arr[2 * i + 2] <= self.Min_arr[2 * i + 1] and self.Min_arr[2 * i + 2] <= self.Min_arr[i]:
				self.Min_arr[i], self.Min_arr[2 * i + 2] = self.Min_arr[2 * i + 2], self.Min_arr[i]
				i = 2 * i + 2
			else:
				break
		if (2 * i + 1) < len(self.Min_arr):
			self.Min_arr[i], self.Min_arr[2 * i + 1] = (self.Min_arr[i], self.Min_arr[2 * i + 1]) if self.Min_arr[i] < \
							self.Min_arr[2 * i + 1] else (self.Min_arr[2 * i + 1], self.Min_arr[i])
		if len(self.Min_arr) == 2:
			(self.Min_arr[0], self.Min_arr[-1]) = (self.Min_arr[0], self.Min_arr[-1]) if self.Min_arr[0] < \
							  self.Min_arr[-1] else (self.Min_arr[-1], self.Min_arr[0])

	def Get_Median(self):
		if len(self.Min_arr) > len(self.Max_arr):
			return self.Min_arr[0]
		elif len(self.Min_arr) < len(self.Max_arr):
			return self.Max_arr[0]
		else:
			print ((self.Min_arr[0] + self.Max_arr[0]) /2)


if __name__ == '__main__':
	median = Median()
	# list = [1,2,3]
	# for i in list:
	# 	median.push(i)
	# median.Get_Median()
	nums1 = [7]
	nums2 = [1,2,3,4,5,6,8,9,10]
	median.findMedianSortedArrays(nums1, nums2)
