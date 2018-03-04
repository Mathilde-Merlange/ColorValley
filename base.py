#!/usr/bin/python3

import pygame
from pygame.locals import *
import math 
import time 

PURPLE=(127,0,255)
RED=(255,0,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
ORANGE=(255,127,0)
colors=[PURPLE,RED,BLUE,YELLOW]
PI=math.pi
x1=PI/2
y1=PI
x2=0
x3=3*PI/2
y3=2*PI
r=20

horloge=pygame.time.Clock()

score=0

def augmenter_score(score):
	score=score+1
	


pygame.init()
fenetre=pygame.display.set_mode((640,480))
pygame.display.set_caption("Color Valley")

a=320
b=400

#def collision(balle,obj):

continuer = 1
while continuer:
	horloge.tick(20)# 20 fois par seconde
	pygame.display.flip()
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
		if event.type== MOUSEBUTTONDOWN:
			b+= 10

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
	pygame.time.wait(350) # vitesse rotation

	pygame.draw.circle(fenetre,WHITE,[a,b],15,0)
	barre_score=pygame.draw.line(fenetre,BLACK,(310,470),(310,460),200)
	chg_color=pygame.draw.circle(fenetre,ORANGE,[320,100],20,0)
	
	

	
pygame.quit()			
