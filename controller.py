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
W=(255,25,255)
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
    rect_pie.center=(200,125)



def pos_max_balle(y,y_max):
    if(y<y_max):
        y_max=y
    return y_max




def jeu():
    
    running=True
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('Color Valley')

    clock=pygame.time.Clock()
    
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


            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                y-=40
                balle_rect.y=y
                if(y<=350):
                    if (obst_cercle_rect.y>=600):
                        obst_cercle_rect.y=-125
                    else: 
                        obst_cercle_rect.y+=30

                    if (carre_grav>=600):
                        carre_grav=-125
                    else:
                        carre_grav+=30
                    
                    rect_pie.y+=30
                   
                    
                pos_max_balle(y,y_max)

       
        

        y=model.ball_gravity(y,y_init)
        balle_rect.y=y
        
        
        if(model.collision(balle_rect,rect_pie)):
            color_init=model.update_ball(balle_surface)
            score=model.score_add(score)
            rect_pie.y=-125


        i=model.rotate_cercle(i,obst_cercle_surf)
        coul_cercle_bas= model.couleur_arc_bas(i)
        coul_cercle_haut=model.couleur_arc_haut(i)
        
        balle_cercle_coll_bas=model.coll_balle_obs_bas(balle_rect,obst_cercle_rect,coul_cercle_bas,color_init)
        balle_cercle_coll_haut=model.coll_balle_obs_haut(balle_rect,obst_cercle_rect,coul_cercle_haut,color_init)
        
        angle=model.rotate_carre(angle)  #rotation 360 du carre
        coul_carre_bas=model.couleur_carre_bas(angle)
        coul_carre_haut=model.couleur_carre_haut(angle)
        rect_carre=obst_carre(angle,190,carre_grav)
        balle_carre_coll_bas=model.coll_balle_obs_bas(balle_rect,rect_carre,coul_carre_bas,color_init)
        balle_carre_coll_haut=model.coll_balle_obs_haut(balle_rect,rect_carre,coul_carre_haut,color_init)
        
        if( balle_cercle_coll_bas!=True or balle_cercle_coll_haut !=True or balle_carre_coll_haut !=True or balle_carre_coll_bas!=True):
            game_over(score)
        
        
        action_render(screen)
        
        screen.blit(rotated_surface, (rect_carre.x, rect_carre.y))
        

    


        pygame.display.flip()

   
    
def menu():
    pygame.init()
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('Color Valley')
    font=pygame.font.Font(None,40)
    
    menu=font.render("Color Valley",1,(0,100,255))
    
    play_button=view.play()

    
    
    intro=True
    while intro:

        screen.blit(menu,(120,100,400,200))
        b=screen.blit(play_button,(136,236))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                intro=False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=pygame.mouse.get_pos()
                if b.collidepoint(pos):
                    jeu()
        
        
        pygame.display.flip()
        
    pygame.quit()
    
    
def game_over(score):
    pygame.init()
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('Color Valley')
    font=pygame.font.Font(None,40)  
    game=font.render("GAME",5,(255,0,128))
    over=font.render("OVER",5,(53,226,242))
    scoreAff=font.render("Score : ",1,(255,255,255))
    scoreF=str(score) #int to string
    scoreFinal=font.render(scoreF,1,(255,255,255))
    retry=view.retry()
    
    end=True
    while end:
        r=screen.blit(retry, (136,410))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=pygame.mouse.get_pos()
                if r.collidepoint(pos):
                        jeu()

        
        screen.blit(game,(150,150,400,200))
        screen.blit(over,(155,180,400,210))
        screen.blit(scoreAff,(100,250,200,400))
        screen.blit(scoreFinal,(250,250,400,400))
        
        pygame.display.flip()
        
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    pygame.quit()
    
    
    
    
        
   
    
    
def main():
    menu()   
    

if __name__ == '__main__':
    main()
