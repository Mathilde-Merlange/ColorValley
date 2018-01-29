#!/usr/bin/python3

import pygame
from pygame.locals import *

ROUGE=(255,0,0)
VERT=(0,255,0)
BLEU=(0,0,255)
JAUNE=(255,255,0)
colors=[ROUGE,VERT,BLEU,JAUNE]




pygame.init()
fenetre=pygame.display.set_mode((640,480))


pygame.draw.circle(fenetre,(ROUGE),[200,300],60,5)
#pygame.draw.line(fenetre, (0,255,0), [0, 0], [50,30], 5)
pygame.draw.circle(fenetre,(255,255,255),[0,0],5,0) # exemple
pygame.draw.circle(fenetre,(VERT),[320,400],10,0) # balle
pygame.draw.circle(fenetre,(VERT),[320,450],10,0) # balle


pygame.display.flip()


continuer = 1
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle



