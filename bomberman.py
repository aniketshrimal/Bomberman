from enemy import *
from getch import *
from board import *
from bomb import *
from wall import *
from bricks import *
from player import *
import os,signal,copy,sys,time
from alarmexception import *
from datetime import datetime
getch = GetchUnix()

def alarmHandler(signum, frame):
    raise AlarmException

def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)

    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
    	
    #signal.signal(signal.SIGALRM, signal.SIG_IGN)
    	return '%'
    	

game_board=board()
matrix=game_board.returnboard()

w=wall(matrix)

	
matrix=w.form_wall()

b=bricks(matrix)
matrix=b.modify_wall()

x=0
y=0

p=player(x,y,matrix)
		

enemy_numbers=0
total=3
enemy1=[]

for i in range(enemy_numbers):	
	q=enemy(matrix)
	q.initial()
	enemy1.append(q)


def print_board(matrix):
	for i in range(38):
		for j in range(76):
			if matrix[i][j]=='B':
				print('B',end='')
			else:
				print(matrix[i][j],end='')	

		print()
	print("\n")	
	print("LEVEL:",p.level,"\t\tLIVES LEFT-",p.lives,"\t\t","SCORE: ",p.score)
				

print_board(matrix)			
st=0
	
bomb1=bomb(p.x,p.y,matrix)
while p.level<=3:

	if(enemy_numbers==0):
		p.level+=1
		print("LEVEL COMPLETED")
		time.sleep(2)
		os.system('cls' if os.name == 'nt' else 'clear')		
		matrix=bomb1.clear()
		matrix=p.clear()
		matrix=p.initial()
		matrix=p.new_place()
		enemy_numbers=total*p.level
		total=enemy_numbers
		for i in range(enemy_numbers):	
			q=enemy(matrix)
			q.initial()
			enemy1.append(q)
		count=-3
		bomb1.val=0
		print_board(matrix)
		continue			
	
	text=input_to()
	if text=='a':
		matrix=p.move_left()
	elif text=='s':
		matrix=p.move_down()
	elif text=='d':
		matrix=p.move_right()
	elif text=='w':
		matrix=p.move_up()
	elif text=='q':
		st=1
		print("quit")
		break	
	elif text=='b' and bomb1.val==0:
		bomb1.posx=p.x
		bomb1.posy=p.y
		bomb1.display=2
		matrix=bomb1.bomb_plant()			
		count=5		

	if p.die==3:
		os.system('cls' if os.name == 'nt' else 'clear')		
		print_board(matrix)
		print("Lost a life(:")
		time.sleep(1)
		p.initial()
		p.new_place()
		continue


	for i in range(0,enemy_numbers):
		enemy1[i].randommove()
	
		
	if bomb1.val==1:
		matrix=bomb1.bomb_display()
		count-=1

	if count==1:
		for i in range(0,total):
			if i<enemy_numbers:
				enemy1[i].posx=bomb1.posx
				enemy1[i].posy=bomb1.posy
				temp=enemy1[i].getkill()

				if temp==1:
					enemy1.pop(i)
					enemy_numbers-=1
					p.score+=100
					temp=0
					i-=1
		bomb1.check_block()
		p.score+=(20*bomb1.brcount)	
		p.posx=bomb1.posx
		p.posy=bomb1.posy
					
		quer=p.getkill()		
		if quer==1:
			p.lives-=1
			p.die=1
		bomb1.bomb_explode()
		bomb1.val=2


	if bomb1.val==2 and count==0:
		bomb1.clear()
		bomb1.val=0		
		count=-1
		if p.die==2:
			os.system('cls' if os.name == 'nt' else 'clear')		
			print_board(matrix)
			print("Lost a life(:")
			time.sleep(1)
			p.initial()
			p.new_place()	
	
	if bomb1.val==2:
		count=0
		if p.die==1:
			p.die=2

	if p.die==1:
		os.system('cls' if os.name == 'nt' else 'clear')		
		print_board(matrix)
		print("You Lost a life(:")
		time.sleep(2)
		p.initial()
		p.new_place()
			
			
	os.system('cls' if os.name == 'nt' else 'clear')		
	print_board(matrix)
	if p.lives<=0:
		print("GAME OVER")
		break
			

