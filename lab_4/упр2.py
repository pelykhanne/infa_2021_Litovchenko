import pygame
import numpy as np

pygame.init()

FPS = 30

sc = pygame.display.set_mode((595, 842))
pygame.draw.rect(sc, (0, 34, 43), (0, 0, 595, 450))

pygame.draw.rect(sc, (34, 43, 0), (0, 450, 595, 842))

surf6 = pygame.Surface((594, 450))

pygame.draw.circle(sc, (255, 255, 255),
                   (395, 240), 91)
pygame.draw.ellipse(surf6, (130, 127, 127), 
                    (350, -10, 560, 100))
pygame.draw.ellipse(surf6, (130, 127, 127), 
                    (-200, 40, 560, 100))
pygame.draw.ellipse(surf6, (130, 127, 127), 
                    (-250, 80, 560, 110))
pygame.draw.ellipse(surf6, (130, 127, 127), 
                    (240, 135, 560, 100))
pygame.draw.ellipse(surf6, (130, 127, 127), 
                    (-164, 220, 560, 100))
pygame.draw.ellipse(surf6, (130, 127, 127), 
                    (180, 260, 560, 100))
pygame.draw.ellipse(surf6, (61, 60, 60), 
                    (120, 90, 560, 100))
pygame.draw.ellipse(surf6, (61, 60, 60), 
                    (-280, 185, 560, 110))
pygame.draw.ellipse(surf6, (61, 60, 60), 
                    (120, 330, 560, 100))

surf6.set_alpha(128)
sc.blit(surf6, (0, 0))

def ufo(x, y, s):

    surf1 = pygame.Surface((270*s, 200*s))
    surf1.set_colorkey((0, 0, 0))
    pygame.draw.polygon(surf1, (255, 255, 255),
                        [(0, 200*s), (135*s, 0), (270*s, 200*s)])
    surf1.set_alpha(128)
    sc.blit(surf1, (x, y))
    pygame.draw.ellipse(sc, (140, 140, 140), 
                        (x, y+(340-395)*s, 270*s, 89*s))
    pygame.draw.ellipse(sc, (170, 170, 170), 
                        (x+(43-3)*s, y+(330-395)*s, 191*s, 75*s))
    pygame.draw.ellipse(sc, (255, 255, 255), 
                        (x+(10-3)*s, y+(379-395)*s, 30*s, 12*s))
    pygame.draw.ellipse(sc, (255, 255, 255), 
                        (x+(236-3)*s, y+(379-395)*s, 30*s, 12*s))
    pygame.draw.ellipse(sc, (255, 255, 255), 
                        (x+(46-3)*s, y+(400-395)*s, 30*s, 12*s))
    pygame.draw.ellipse(sc, (255, 255, 255), 
                        (x+(200-3)*s, y+(400-395)*s, 30*s, 12*s))
    pygame.draw.ellipse(sc, (255, 255, 255), 
                        (x+(95-3)*s, y+(410-395)*s, 30*s, 12*s))
    pygame.draw.ellipse(sc, (255, 255, 255), 
                        (x+(151-3)*s, y+(410-395)*s, 30*s, 12*s))
def alien(x,y,s,t):
    pygame.draw.ellipse(sc, (221, 233, 175), 
                    (x+(400-386)*s*t, y+(506-571)*s, 48*s*t, 12*s))
    pygame.draw.circle(sc, (221, 233, 175),
                       (x+(382-386)*s*t, y+(516-571)*s), 8*s)
    surf2 = pygame.Surface((55*s, 12*s))
    surf2.set_colorkey((0, 0, 0))
    pygame.draw.ellipse(surf2, (221, 233, 175),
                        (0, 0, 55*s, 12*s))
    surf3 = pygame.transform.rotate(surf2, -65*t)
    sc.blit(surf3, (x+(370-386)*s*t+33*s*(-1+t)/2, y+(516-571)*s))
    pygame.draw.ellipse(sc, (221, 233, 175),
                       (x+(392-386)*s*t, y+(538-571)*s, 40*s*t, 40*s))
    surf4 = pygame.Surface((55*s, 12*s))
    surf4.set_colorkey((0, 0, 0))
    pygame.draw.ellipse(surf4, (221, 233, 175),
                        (0, 0, 55*s, 13*s))
    surf5 = pygame.transform.rotate(surf4, -115*t)
    sc.blit(surf5, (x+(424-386)*s*t+33*s*(-1+t)/2, y+(510-571)*s))
    pygame.draw.polygon(sc, (221, 233, 175),
                        [(x+(382-386)*s*t, y+(510-571)*s), (x+(382-386)*s*t, y+(534-571)*s), (x+(412-386)*s*t, y+(575-571)*s), (x+(452-386)*s*t, y+(510-571)*s)])
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x, y, 42*s*t, 87*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x-(31)*s*t, y-(114)*s, 20*s*t, 15*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x-(26)*s*t, y-(100)*s, 14*s*t, 9*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x-(19)*s*t, y-(91)*s, 13*s*t, 14*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x-(11)*s*t, y-(76)*s, 8*s*t, 11*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(54)*s*t, y-(70)*s, 14*s*t, 12*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(62)*s*t, y-(75)*s, 7*s*t, 10*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(454-386)*s*t, y-(90)*s, 12*s*t, 13*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(484-386)*s*t,y+(474-571)*s, 18*s*t, 23*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(469-386)*s*t,y+(475-571)*s, 10*s*t, 9*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(373-386)*s*t, y+(626-571)*s, 25*s*t, 35*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(371-386)*s*t, y+(654-571)*s, 15*s*t, 36*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(353-386)*s*t, y+(674-571)*s, 20*s*t, 20*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(376-386)*s*t, y+(576-571)*s, 20*s*t, 20*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(367-386)*s*t, y+(592-571)*s, 17*s*t, 11*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(360-386)*s*t, y+(605-571)*s, 8*s*t, 12*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(421-386)*s*t, y+(578-571)*s, 20*s*t, 20*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(431-386)*s*t, y+(589-571)*s, 19*s*t, 13*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(450-386)*s*t, y+(595-571)*s, 25*s*t, 14*s))
    pygame.draw.ellipse(sc, (0, 0, 0), 
                        (x+(386-386)*s*t, y+(518-571)*s, 25*s*t, 25*s))
    pygame.draw.ellipse(sc, (0, 0, 0), 
                        (x+(426-386)*s*t, y+(523-571)*s, 19*s*t, 19*s))
    pygame.draw.ellipse(sc, (255, 255, 255), 
                        (x+(399-386)*s*t, y+(531-571)*s, 7*s*t, 7*s))
    pygame.draw.ellipse(sc, (255, 255, 255), 
                        (x+(435-386)*s*t, y+(533-571)*s, 5*s*t, 5*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(412-386)*s*t, y+(638-571)*s, 22*s*t, 31*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(418-386)*s*t, y+(665-571)*s, 17*s*t, 35*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x+(432-386)*s*t, y+(686-571)*s, 20*s*t, 20*s))
    pygame.draw.ellipse(sc, (200, 55, 55), 
                        (x+(464-386)*s*t, y+(563-571)*s, 40*s*t, 40*s))
    pygame.draw.arc(sc, (0, 0, 0),
                    (x+(482-386)*s*t, y+(545-571)*s, 100*s*t, 50*s), np.pi-0.7, np.pi, 1)
    pygame.draw.polygon(sc, (136, 170, 0),
                        [(x+(486-386)*s*t, y+(558-571)*s), (x+(484-386)*s*t, y+(555-571)*s), (x+(482-386)*s*t, y+(546-571)*s), (x+(486-386)*s*t, y+(555-571)*s)])
    pygame.draw.arc(sc, (34, 43, 0),
                    (x+(392-386)*s*t, y+(538-571)*s, t*40*s, 40*s), np.pi+0.5, 2*np.pi-0.3,2)
alien(175, 550, 0.3, -1)
ufo(3, 395, 1)
ufo(300, 430, 0.3)
ufo(450, 395, 0.5)
alien(368, 600, 1, 1)
alien(225, 600, 0.3, 1)

alien(50, 600, 0.3, -1)
alien(175, 700, 0.7, -1)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
