# Author:Jack

import numpy as np

class MatPrint():
	def __init__(self, mat):
		self.mat = mat
		

	def matPrint(self):
		LX = 0
		LY = 0
		RX = len(self.mat) - 1
		RY = len(self.mat[0]) - 1
		while LX <= RX and LY <= RY:
			self.PrintEdge(LX, LY, RX, RY)
			LX, LY, RX, RY = LX + 1, LY + 1, RX - 1, RY - 1
	
	
	def PrintEdge(self, LX, LY, RX, RY):
		if LX == RX:
			i = LY
			while i <= RY:
				print(self.mat[LX][i], end=" ")
				i += 1
		elif LY == RY:
			i = LX
			while i <= RX:
				print(self.mat[i][LY], end=" ")
				i += 1
		else:
			curx = LX
			cury = LY
			while curx != RX:
				print(self.mat[LX][curx], end=" ")
				curx += 1
			while cury != RY:
				print(self.mat[cury][RY], end=" ")
				cury += 1
			while curx != LX:
				print(self.mat[RX][curx], end=" ")
				curx -= 1
			while cury != LY:
				print(self.mat[cury][LX], end=" ")
				cury -= 1


if __name__ == '__main__':
	mat = np.array([[1, 2, 3 ,4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
	matprint = MatPrint(mat)
	matprint.matPrint()