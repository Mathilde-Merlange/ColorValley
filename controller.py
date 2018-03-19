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
    screen.blit(pie,rect_pie)


def init_balle(color_init):
        global balle_surface
        global balle_rect
        balle_surface=view.balle()
        balle_rect=view.balle_rect()
        view.draw_balle(balle_surface,color_init)

def obst_cercle():
        global obst_cercle_surf
        global obst_cercle_rect
        obst_cercle_surf=view.obst_cercle_surf()
        obst_cercle_rect=obst_cercle_surf.get_rect()
        obst_cercle_rect.x=125
        obst_cercle_rect.y=225



def obst_carre(angle,x,y):
    global rect_carre
    global rotated_surface
    surface=view.obst_carre()
    rotated_surface = pygame.transform.rotate(surface, angle)
    rect_carre = rotated_surface.get_rect()
    rect_carre.center=(x,y)
    return rect_carre

    
def cercle_change_color():
    global pie 
    global rect_pie
    pie=view.cercle_change_color()
    rect_pie=pie.get_rect()
    rect_pie.center=(200,100)
    



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
    #x=150
    y=500
    y_init=500
    y_max=500
    i=0.0
    color_init=model.newColor()
    init_balle(color_init)
    cercle_change_color()
   
    angle = 0
    carre_grav=-125
    obst_cercle()
    score=0


    while running==True:
		
        
        delta_ms=clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False


            if event.type==pygame.MOUSEBUTTONDOWN:
                y-=30
                balle_rect.y=y
                if(y<=350):
                    if (obst_cercle_rect.y>=600):
                        obst_cercle_rect.y=-125
                    else: 
                        obst_cercle_rect.y+=20

                    if (carre_grav>=600):
                        carre_grav=-125
                    else:
                        carre_grav+=20
                    
                    rect_pie.y+=20
                   
                    
                pos_max_balle(y,y_max)

       
        

        y=model.ball_gravity(y,y_init)
        balle_rect.y=y
        
        
        angle=model.rotate_carre(angle)
        rect_carre=obst_carre(angle,190,carre_grav)
        

        
        i=model.rotate_cercle(i,obst_cercle_surf)
        coul_cercle_bas= model.couleur_arc_bas(i)
        coul_cercle_haut=model.couleur_arc_haut(i)
        
        balle_cercle_coll=model.coll_cercle(balle_rect,obst_cercle_rect,coul_cercle_bas,color_init)
        rect_pie.y=model.coll_pie(balle_surface,balle_rect,rect_pie,score)
        


        action_render(screen)
        
        screen.blit(rotated_surface, (rect_carre.x, rect_carre.y))
        

    


        pygame.display.flip()
	

    pygame.quit()
    exit()
    
    return 0

if __name__ == '__main__':
    main()
