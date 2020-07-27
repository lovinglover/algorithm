# Author:Jack

import numpy as np

class ZigZag():
	def __init__(self, mat):
		self.mat = mat

	def z_print(self):
		LX, LY, RX, RY = 0, 0, 0, 0
		endX = len(self.mat[0]) - 1
		endY = len(self.mat) - 1
		order = False
		while LY <= endX:
			self.print_each_line(LX, LY, RX, RY, order)
			LY = LY if LX != endX else LY + 1
			LX = LX + 1 if LX != endX else endX
			RX = RX if RY != endY else RX + 1
			RY = RY + 1 if RY != endY else endY
			order = not order

	def print_each_line(self, LX, LY, RX, RY, order):
		if order:
			while LX != RX - 1:
				print(self.mat[LY][LX])
				LX -= 1
				LY += 1
		else:
			while RX != LX + 1:
				print(self.mat[RY][RX])
				RX += 1
				RY -= 1


if __name__ == '__main__':
	mat = np.array([[1, 2, 3, 4],
					[5, 6, 7, 8],
					[9, 10, 11, 12]])
	z = ZigZag(mat)
	z.z_print()