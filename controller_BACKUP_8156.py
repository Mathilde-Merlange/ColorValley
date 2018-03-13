import pygame
from sys import exit
import time
import view
import model


score=0
width=800
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



def init_balle():
        global balle_surface
        global balle_rect
        balle_surface=view.balle()
        balle_rect=view.balle_rect()
        view.balle()

def update_obst_cercle():
        global obst_cercle_surf
        global obst_cercle_rect
        obst_cercle_surf=view.obst_cercle_surf()
        obst_cercle_rect=obst_cercle_surf.get_rect()
        obst_cercle_rect.x=275 
        obst_cercle_rect.y=120


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
    x=400
    y=500
    y_init=500
    y_max=500
    init_balle()
    update_obst_cercle()
    i=0.0
    
    while running==True:
		
        
        delta_ms=clock.tick(fps)
        i+=0.05
<<<<<<< HEAD
        view.draw_obst_cercle(obst_cercle_surf,i)
        
=======
        obst_cercle_surf=view.obst_cercle_surf(i)
        obst_cercle_rect=obst_cercle_surf.get_rect()
        obst_cercle_rect.x=275
        obst_cercle_rect.y=150
        model.coll_cercle(balle_rect,obst_cercle_rect)
>>>>>>> 15b52778180d41cecd303e329e0dfd79adaa07f6
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False


            if event.type==pygame.MOUSEBUTTONDOWN:
                y-=30
                balle_rect.y=y
<<<<<<< HEAD
                pos_max_balle(y,y_max)

       
        action_render(screen)
        if(y<=250):
            obst_cercle_rect.y+=1


        
        y=model.ball_gravity(y,y_init)
        balle_rect.y=y
        
=======

        #action_render(screen)
        screen.fill(B)
        screen.blit(obst_cercle_surf,obst_cercle_rect)
        screen.blit(balle_surface,balle_rect)
        if(y<=y_init):
        	y+=2
        	balle_rect.y=y
>>>>>>> 15b52778180d41cecd303e329e0dfd79adaa07f6

        pygame.display.flip()
	

    pygame.quit()
    exit()
    
    return 0

if __name__ == '__main__':
    main()
