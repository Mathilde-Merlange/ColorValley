#!/usr/bin/python3

import pygame
from pygame.locals import *
import math 
import time 

PURPLE=(140,19,251)
RED=(255,0,128)
BLUE=(53,226,242)
YELLOW=(246,223,14)
colors=[PURPLE,RED,BLUE,YELLOW]
PI=math.pi
x1=PI/2
y1=PI
x2=0
x3=3*PI/2
y3=2*PI
r=20


pygame.init()
fenetre=pygame.display.set_mode((640,480))
pygame.display.set_caption("Color Valley")




continuer = 1
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle

	x1+=1
	y1+=1
	x2+=1
	x3+=1
	y3+=1

	#obstacle
	pygame.draw.arc(fenetre,PURPLE, [187,150,250,200],x1,y1,r) #cercle 4 couleurs
	pygame.draw.arc(fenetre,RED, [187,150,250,200], x2, x1,r)
	pygame.draw.arc(fenetre, BLUE, [187,150,250,200], x3, y3, r)
	pygame.draw.arc(fenetre, YELLOW, [187,150,250,200], y1, x3, r)
	pygame.time.wait(350)

	pygame.draw.line(fenetre,BLUE,(187,60),(450,60),20)
	pygame.draw.line(fenetre,PURPLE,(187,0),(60,185),20)
	#dessiner un triangle avec polygone
	#pygame.draw.polygon(fenetre,BL, [[100, 100], [0, 200], [200, 200]], 5)

	pygame.draw.circle(fenetre,(PURPLE),[320,400],10,0) # balle


	pygame.display.flip()

	
			


