import time


class bomb():

	def __init__(self,x,y,matrix):
		self.posx=x
		self.posy=y
		self.matrix=matrix
		self.val=0
		self.player=0
		self.enemy=0
		self.display=4
		self.brcount=0

	def bomb_plant(self):
		for i in range(self.posx,self.posx+2):
			for j in range(self.posy,self.posy+4):
					self.matrix[i][j]='O'
		self.val=1			
		return self.matrix			

	def bomb_display(self):
		for i in range(self.posx,self.posx+2):
			for j in range(self.posy,self.posy+4):
					self.matrix[i][j]=self.display
		self.display-=1			
		return self.matrix			
	
	def bomb_explode(self):
		for i in range(self.posx-2,self.posx+4):
			for j in range(self.posy,self.posy+4):
				if self.matrix[i][j]!='X':
					self.matrix[i][j]='e'
				
				
		for i in range(self.posx,self.posx+2):
			for j in range(self.posy-4,self.posy+8):
				if self.matrix[i][j]!='X':
					self.matrix[i][j]='e'
				
									
		return self.matrix			


	def clear(self):
		for i in range(self.posx-2,self.posx+4):
			for j in range(self.posy,self.posy+4):
				if self.matrix[i][j]=='e':
					self.matrix[i][j]=' '
		for i in range(self.posx,self.posx+2):
			for j in range(self.posy-4,self.posy+8):
				if self.matrix[i][j]=='e':
					self.matrix[i][j]=' '
		
		return self.matrix										

	def check_block(self):
		self.brcount=0
		
		if self.matrix[self.posx-2][self.posy]=='/':
				self.brcount+=1
		if self.matrix[self.posx+2][self.posy]=='/':
				self.brcount+=1
		if self.matrix[self.posx][self.posy-4]=='/':
				self.brcount+=1
		if self.matrix[self.posx][self.posy+4]=='/':
				self.brcount+=1
		
			