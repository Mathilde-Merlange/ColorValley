import pygame
from pygame.locals import *
import math





PURPLE=(140,19,251)
RED=(255,0,128)
BLUE=(53,226,242)
YELLOW=(246,223,14)
colors=[PURPLE,RED,BLUE,YELLOW]



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




def balle(fenetre):
	pygame.draw.circle(fenetre,(PURPLE),[320,400],10,0) # balle