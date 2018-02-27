import pygame
from pygame.locals import *
import math





PURPLE=(127,0,255)
RED=(255,0,0)
BLUE=(0,0,200)
YELLOW=(255,255,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
ORANGE=(255,127,0)
colors=[PURPLE,RED,BLUE,YELLOW]

def barre_score(fenetre):
	barre_score=pygame.draw.line(fenetre,BLACK,(310,470),(310,460),200)

def chg_color(fenetre):
	chg_color=pygame.draw.circle(fenetre,ORANGE,[320,100],20,0)

def obst_cercle_init(fenetre,i):
	PI=math.pi
	x1=PI/2
	y1=PI
	x2=0
	x3=3*PI/2
	y3=2*PI
	r=20
	pygame.draw.arc(fenetre,PURPLE, [187,150,250,200],x1+i,y1+i,r) #cercle 4 couleurs
	pygame.draw.arc(fenetre,RED, [187,150,250,200], x2+i, x1+i,r)
	pygame.draw.arc(fenetre, BLUE, [187,150,250,200], x3+i, y3+i, r)
	pygame.draw.arc(fenetre, YELLOW, [187,150,250,200], y1+i, x3+i, r)

def obst_carre_init(fenetre):
	v=40
	
	pygame.draw.line(fenetre, PURPLE, (320-v,400+v),(320+v,400+v),5)
	pygame.draw.line(fenetre, RED, (320-v,320+v),(320+v,320+v),5)
	pygame.draw.line(fenetre, BLUE, (320-v,400+v),(320-v,320+v),5)
	pygame.draw.line(fenetre, YELLOW, (320+v ,400+v),(320+v,320+v),5)
	
	
def obst_barres_init(fenetre,i):
	pygame.draw.line(fenetre, PURPLE, (0+i,400+i),(160+i,400+i),5)
	pygame.draw.line(fenetre, RED, (160+i,400+i),(320+i,400+i),5)
	pygame.draw.line(fenetre, BLUE, (320+i,400+i),(480+i,400+i),5)
	pygame.draw.line(fenetre, YELLOW, (480+i,400+i),(640+i,400+i),5)
	

def balle(fenetre):
	balle=pygame.draw.circle(fenetre,WHITE,[320,750],10,0) # balle
