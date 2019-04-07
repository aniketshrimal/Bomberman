from random import randrange, uniform

class bricks():

	def __init__(self,matrix):
		self.matrix=matrix

	def modify_wall(self):
		k=0
		while k<30:
			x=randrange(3,34)
			y=randrange(2,73)
			if x%2==0 and y%4==0 and self.matrix[x][y]==' ' and self.matrix[x][y+3]==' ' and self.matrix[x+1][y]==' ' and self.matrix[x+1][y+3]==' ' :
				k+=1
				for i in range(x,x+2):
					for j in range(y,y+4):
						self.matrix[i][j]='/'
		
		return self.matrix	

					
