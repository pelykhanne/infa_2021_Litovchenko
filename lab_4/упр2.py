import pygame
import numpy as np

pygame.init()

FPS = 30

sc = pygame.display.set_mode((595, 842))
pygame.draw.rect(sc, (0, 34, 43), (0, 0, 595, 450))

pygame.draw.rect(sc, (34, 43, 0), (0, 450, 595, 842))

pygame.draw.circle(sc, (255, 255, 255),
                   (395, 240), 91)
pygame.draw.ellipse(sc, (130, 127, 127), 
                    (350, -10, 560, 100))
pygame.draw.ellipse(sc, (130, 127, 127), 
                    (-200, 40, 560, 100))
pygame.draw.ellipse(sc, (130, 127, 127), 
                    (-250, 80, 560, 110))
pygame.draw.ellipse(sc, (130, 127, 127), 
                    (240, 135, 560, 100))
pygame.draw.ellipse(sc, (130, 127, 127), 
                    (-164, 220, 560, 100))
pygame.draw.ellipse(sc, (130, 127, 127), 
                    (180, 260, 560, 100))
pygame.draw.ellipse(sc, (61, 60, 60), 
                    (120, 90, 560, 100))
pygame.draw.ellipse(sc, (61, 60, 60), 
                    (-280, 185, 560, 110))
pygame.draw.ellipse(sc, (61, 60, 60), 
                    (120, 330, 560, 100))
surf1 = pygame.Surface((270, 200))
surf1.set_colorkey((0, 0, 0))
pygame.draw.polygon(surf1, (255, 255, 255),
                    [(0, 200), (135, 0), (270, 200)])
surf1.set_alpha(128)
sc.blit(surf1, (3, 395))
pygame.draw.ellipse(sc, (140, 140, 140), 
                    (3, 340, 270, 89))
pygame.draw.ellipse(sc, (170, 170, 170), 
                    (43, 330, 191, 75))
pygame.draw.ellipse(sc, (255, 255, 255), 
                    (10, 379, 30, 12))
pygame.draw.ellipse(sc, (255, 255, 255), 
                    (236, 379, 30, 12))
pygame.draw.ellipse(sc, (255, 255, 255), 
                    (46, 400, 30, 12))
pygame.draw.ellipse(sc, (255, 255, 255), 
                    (200, 400, 30, 12))
pygame.draw.ellipse(sc, (255, 255, 255), 
                    (95, 410, 30, 12))
pygame.draw.ellipse(sc, (255, 255, 255), 
                    (151, 410, 30, 12))
def alien(x,y,s):
    pygame.draw.ellipse(sc, (221, 233, 175), 
                    ((x+400-386)*s, (y+506-571)*s, 48*s, 12*s))
    pygame.draw.circle(sc, (221, 233, 175),
                       ((x+382-386)*s, (y+516-571)*s), 8*s)
    pygame.draw.rect(sc, (221, 233, 175),
                     ((x+382-386)*s, (y+510-571)*s, 42*s, 10*s))
    surf2 = pygame.Surface((55*s, 12*s))
    surf2.set_colorkey((0, 0, 0))
    pygame.draw.ellipse(surf2, (221, 233, 175),
                        (0, 0, 55*s, 12*s))
    surf3 = pygame.transform.rotate(surf2, -65)
    sc.blit(surf3, ((x+370-386)*s, (y+516-571)*s))
    pygame.draw.ellipse(sc, (221, 233, 175),
                       ((x+392-386)*s, (y+538-571)*s, 40*s, 40*s))
    surf4 = pygame.Surface((55*s, 12*s))
    surf4.set_colorkey((0, 0, 0))
    pygame.draw.ellipse(surf4, (221, 233, 175),
                        (0, 0, 55*s, 13*s))
    surf5 = pygame.transform.rotate(surf4, -115)
    sc.blit(surf5, ((x+424-386)*s, (y+510-571)*s))
    pygame.draw.polygon(sc, (221, 233, 175),
                        [((x+382-386)*s, (y+516-571)*s), ((x+382-386)*s, (y+534-571)*s), ((x+412-386)*s, (y+575-571)*s), ((x+450-386)*s, (y+512-571)*s)])
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        (x*s, y*s, 42*s, 87*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x-31)*s, (y-114)*s, 20*s, 15*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x-26)*s, (y-100)*s, 14*s, 9*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x-19)*s, (y-91)*s, 13*s, 14*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x-11)*s, (y-76)*s, 8*s, 11*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+54)*s, (y-70)*s, 14*s, 12*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+62)*s, (y-75)*s, 7*s, 10*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+454-386)*s, (y-90)*s, 12*s, 13*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+484-386)*s,(y+474-571)*s, 18*s, 23*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+469-386)*s,(y+475-571)*s, 10*s, 9*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+373-386)*s, (y+626-571)*s, 25*s, 35*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+371-386)*s, (y+654-571)*s, 15*s, 36*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+353-386)*s, (y+674-571)*s, 20*s, 20*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+376-386)*s, (y+576-571)*s, 20*s, 20*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+367-386)*s, (y+592-571)*s, 17*s, 11*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+360-386)*s, (y+605-571)*s, 8*s, 12*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+421-386)*s, (y+578-571)*s, 20*s, 20*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+431-386)*s, (y+589-571)*s, 19*s, 13*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+450-386)*s, (y+595-571)*s, 25*s, 14*s))
    pygame.draw.ellipse(sc, (0, 0, 0), 
                        ((x+386-386)*s, (y+518-571)*s, 25*s, 25*s))
    pygame.draw.ellipse(sc, (0, 0, 0), 
                        ((x+426-386)*s, (y+523-571)*s, 19*s, 19*s))
    pygame.draw.ellipse(sc, (255, 255, 255), 
                        ((x+399-386)*s, (y+531-571)*s, 7*s, 7*s))
    pygame.draw.ellipse(sc, (255, 255, 255), 
                        ((x+435-386)*s, (y+533-571)*s, 5*s, 5*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+412-386)*s, (y+638-571)*s, 22*s, 31*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+418-386)*s, (y+665-571)*s, 17*s, 35*s))
    pygame.draw.ellipse(sc, (221, 233, 175), 
                        ((x+432-386)*s, (y+686-571)*s, 20*s, 20*s))
    pygame.draw.ellipse(sc, (200, 55, 55), 
                        ((x+464-386)*s, (y+563-571)*s, 40*s, 40*s))
    pygame.draw.arc(sc, (0, 0, 0),
                    ((x+482-386)*s, (y+545-571)*s, 100*s, 50*s), np.pi-0.7, np.pi, 1)
    pygame.draw.polygon(sc, (136, 170, 0),
                        [((x+486-386)*s, (y+558-571)*s), ((x+484-386)*s, (y+555-571)*s), ((x+482-386)*s, (y+546-571)*s), ((x+486-386)*s, (y+555-571)*s)])
    pygame.draw.arc(sc, (34, 43, 0),
                    ((x+392-386)*s, (y+538-571)*s, 40*s, 40*s), np.pi+0.5, 2*np.pi-0.3,2)

alien(386,571,0.5)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
