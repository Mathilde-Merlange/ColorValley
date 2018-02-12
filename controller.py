import model
import view
import time
import pygame
from pygame.locals import *


pygame.init()
fenetre=pygame.display.set_mode((640,480))
pygame.display.set_caption("Color Valley")

horloge=pygame.time.Clock()
i=0



continuer = 1
while continuer:
	horloge.tick(20)
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrêt
	pygame.display.flip()
	i+=1
	view.obst_cercle_init(fenetre,i)
	pygame.time.wait(350)
	view.balle(fenetre)
			


			


