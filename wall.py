

class wall():
	
	def __init__(self,matrix):
		self.matrix=matrix

	def form_wall(self):	
		for row in range(38):
			for col in range(76):
				if row<2 or row>=36 or col<4 or col>=72:
					self.matrix[row][col]='X'
				if(row%4<=1 and col%8<=3):
					self.matrix[row][col]='X'	

		return self.matrix			
	


