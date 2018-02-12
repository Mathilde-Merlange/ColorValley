#!/usr/bin/python3

import pygame
from pygame.locals import *

ROUGE=(255,0,0)
VERT=(0,255,0)
BLEU=(0,0,255)
JAUNE=(255,255,0)
colors=[ROUGE,VERT,BLEU,JAUNE]
horloge=pygame.time.Clock()



pygame.init()
fenetre=pygame.display.set_mode((640,480))


pygame.draw.circle(fenetre,(ROUGE),[200,300],60,5)

pygame.draw.circle(fenetre,(255,255,255),[0,0],5,0) # exemple
pygame.draw.circle(fenetre,(255,255,255),[320,400],10,0) # bille couleurs
pygame.draw.circle(fenetre,(VERT),[320,450],10,0) # balle



continuer = 1
while continuer:
	horloge.tick(10)# 10 fois par seconde
	pygame.display.flip()
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle



