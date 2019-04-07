
class player():

	def __init__(self,x,y,matrix):
		self.x=x
		self.y=y
		self.matrix=matrix
		self.score=0
		self.die=0
		self.lives=3
		self.posx=0
		self.posy=0
		self.level=0

	def initial(self):
		self.die=0
		self.x=2
		self.y=4
		return self.matrix
		

	def clear(self):
		for i in range(self.x,self.x+2):
			for j in range(self.y,self.y+4):
				if self.matrix[i][j]=='B':
					self.matrix[i][j]=' '

	def new_place(self):
		for i in range(self.x,self.x+2):
			for j in range(self.y,self.y+4):
				self.matrix[i][j]='B'
		return self.matrix		
			
						
			
	def move_up(self):
		if self.x-2>=0 and self.matrix[self.x-2][self.y]==' ':
			self.clear()
			self.x=self.x-2
			self.new_place()
		elif self.x-2>=0 and self.matrix[self.x-2][self.y]=='E':
			self.die=3	
			self.lives-=1
			self.clear()
		return self.matrix
			

	def move_down(self):
		if self.x+2<=37 and self.matrix[self.x+2][self.y]==' ':
			self.clear()
			self.x=self.x+2
			self.new_place()
		if self.x+2<=37 and self.matrix[self.x+2][self.y]=='E':
			self.die=1
			self.lives-=1
			self.clear()
		return self.matrix	

	def move_left(self):
		if self.y-4>=0 and self.matrix[self.x][self.y-4]==' ':
			self.clear()
			self.y=self.y-4
			self.new_place()
		if self.y-4>=0 and self.matrix[self.x][self.y-4]=='E':
			self.die=3
			self.lives-=1
			self.clear()
			
		return self.matrix

		
	def move_right(self):
		if self.y+4<76 and self.matrix[self.x][self.y+4]==' ':
			self.clear()
			self.y=self.y+4
			self.new_place()
		elif self.y+4<76 and self.matrix[self.x][self.y+4]=='E':
			self.die=3
			self.lives-=1
			self.clear()

		return self.matrix
	
	def getkill(self):
		if self.x<=self.posx+3 and self.x>=self.posx-2 and self.y==self.posy :
			self.die=1
		else:
			self.die=0
		if self.y-4<=self.posy and self.y+7>=self.posy	and self.posx==self.x:
			self.die=1	
		return self.die	
		