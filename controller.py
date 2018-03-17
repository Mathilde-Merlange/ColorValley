import pygame
from sys import exit
import time
import view
import model
import math

score=0
width=400
height=600
fps=20
SPEED=30.0
B=(0,0,0)
continuer=1

RED=(255,0,128)





def action_render(screen):
    screen.fill(B)
    screen.blit(obst_cercle_surf,obst_cercle_rect)
    screen.blit(balle_surface,balle_rect)



def init_balle(color_init):
        global balle_surface
        global balle_rect
        balle_surface=view.balle()
        balle_rect=view.balle_rect()
        view.draw_balle(balle_surface,color_init)

def update_obst_cercle():
        global obst_cercle_surf
        global obst_cercle_rect
        obst_cercle_surf=view.obst_cercle_surf()
        obst_cercle_rect=obst_cercle_surf.get_rect()
        obst_cercle_rect.x=125
        obst_cercle_rect.y=225


def obst_carre(angle,surface,x,y):
    global rotated_surface
    global rect
    
    rotated_surface = pygame.transform.rotate(surface, angle)
    rect = rotated_surface.get_rect()
    rect.center=(x,y)
    




def pos_max_balle(y,y_max):
    if(y<y_max):
        y_max=y
    return y_max



def main():
    pygame.init()
    running=True
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('Color Valley')

    clock=pygame.time.Clock()
    x=150
    y=500
    y_init=500
    y_max=500
    i=0.0
    color_init=model.newColor()
    init_balle(color_init)
    surface =view.obst_carre()
    angle = 0
    carre_grav=0
    update_obst_cercle()
    while running==True:
		
        
        delta_ms=clock.tick(fps)
        
        
        if(i>math.radians(360)):
            i=0.0
        else:
            i+=math.radians(2)
        
        view.draw_obst_cercle(obst_cercle_surf,i)
        coul_cercle_bas= model.couleur_arc_bas(i)
        coul_cercle_haut=model.couleur_arc_haut(i)
        
        balle_cercle_coll=model.coll_cercle(balle_rect,obst_cercle_rect,coul_cercle_bas,color_init)
        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False


            if event.type==pygame.MOUSEBUTTONDOWN:
                y-=30
                balle_rect.y=y
                if(y<=300):
                    obst_cercle_rect.y+=10
                    carre_grav+=10
                   
                pos_max_balle(y,y_max)

       
        
        y=model.ball_gravity(y,y_init)

        balle_rect.y=y
        angle+=2
        obst_carre(angle,surface,190,carre_grav)
        


        action_render(screen)
        screen.blit(rotated_surface, (rect.x, rect.y))
        

        if(y<=y_init):
        	y+=2
        	balle_rect.y=y


        pygame.display.flip()
	

    pygame.quit()
    exit()
    
    return 0

if __name__ == '__main__':
    main()
