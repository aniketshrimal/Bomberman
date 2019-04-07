from random import *

class enemy():

	def __init__(self,matrix):
		self.x=0
		self.y=0
		self.val=0
		self.matrix=matrix
		self.kill=0
		self.posx=-1
		self.posy=-1
		self.player=0	

	def initial(self):
		while 1:	
			self.x=randint(0,34)
			self.y=randint(4,72)
			self.val=1
			for row in range(self.x,self.x+2):
				for col in range(self.y,self.y+4):
					if self.matrix[row][col]!=' ':
						self.val=0
			if self.val==1 and self.x%2==0 and self.y%4==0:
				break
		for row in range(self.x,self.x+2):
				for col in range(self.y,self.y+4):
					self.matrix[row][col]='E'												
		return self.matrix
		

	def clear(self):
		for i in range(self.x,self.x+2):
			for j in range(self.y,self.y+4):
				self.matrix[i][j]=' '

	def new_place(self):
		for i in range(self.x,self.x+2):
			for j in range(self.y,self.y+4):
				self.matrix[i][j]='E'
		return self.matrix		
			
						
			
	def move_up(self):
		self.player=0
		if self.x-2>=0 and self.matrix[self.x-2][self.y]==' ':
			self.clear()
			self.x=self.x-2
			self.new_place()
		return self.matrix
			

	def move_down(self):
		self.player=0
		if self.x+2<=37 and self.matrix[self.x+2][self.y]==' ':
			self.clear()
			self.x=self.x+2
			self.new_place()
		
		return self.matrix	

	def move_left(self):
		self.player=0
		if self.y-4>=0 and self.matrix[self.x][self.y-4]==' ':
			self.clear()
			self.y=self.y-4
			self.new_place()
		return self.matrix

		
	def move_right(self):
		self.player=0
		if self.y+4<76 and self.matrix[self.x][self.y+4]==' ':
			self.clear()
			self.y=self.y+4
			self.new_place()
		return self.matrix


	def randommove(self):
		valcheck=0
		check=[0,0,0,0,0]
		if self.x-2>=0 and self.matrix[self.x-2][self.y]==' ':
			check[4]=1
			
		if self.x+2<=37 and self.matrix[self.x+2][self.y]==' ':
			check[3]=1	
			
		if self.y-4>=0 and self.matrix[self.x][self.y-4]==' ':
			check[2]=1
				
		if self.y+4<76 and self.matrix[self.x][self.y+4]==' ':
			check[1]=1
			
		for i in range(1,5):
			if check[i]==1:
				valcheck=1
				break
		choice=randint(1,4)		
		if valcheck!=0:				
			while(check[choice]!=1):
				choice=randint(1,4)

		if choice==1:
			self.move_right()
		elif choice==2:
			self.move_left()
		elif choice==3:
			self.move_down()
		else:
			self.move_up()				
	
	def getkill(self):					
		if self.x<=self.posx+3 and self.x>=self.posx-2 and self.y==self.posy :
			self.kill=1
		else:
			self.kill=0
		if self.y-4<=self.posy and self.y+7>=self.posy	and self.posx==self.x:
			self.kill=1	
		
		return self.kill				
		

	
