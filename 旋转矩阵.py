# Author:Jack

import numpy as np

class RotateMat():
	def __init__(self, mat):
		self.mat = mat

	def rotate(self):
		LX, LY, RX, RY = 0, 0, len(self.mat) - 1, len(self.mat[0]) - 1
		while LX < RX:
			self.rotate_edge(LX, LY, RX, RY)
			LX, LY, RX, RY = LX + 1, LY + 1, RX - 1, RY - 1

	def rotate_edge(self, LX, LY, RX, RY):
		times = RX - LX
		for i in range(times):
			tmp = self.mat[LX][LY + i]
			self.mat[LX][LY + i] = self.mat[RX - i][LY]
			self.mat[RX - i][LY] = self.mat[RX][RY - i]
			self.mat[RX][RY - i] = self.mat[LX + i][RY]
			self.mat[LX + i][RY] = tmp

	def show(self):
		print(self.mat)


if __name__ == '__main__':
	mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
	r = RotateMat(mat)
	r.show()
	r.rotate()
	r.show()