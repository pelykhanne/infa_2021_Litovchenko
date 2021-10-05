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
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (400, 506, 48, 12))
pygame.draw.circle(sc, (221, 233, 175),
                   (382, 516), 8)
pygame.draw.rect(sc, (221, 233, 175),
                 (382, 510, 42, 10))
surf2 = pygame.Surface((55, 12))
surf2.set_colorkey((0, 0, 0))
pygame.draw.ellipse(surf2, (221, 233, 175),
                    (0, 0, 55, 12))
surf3 = pygame.transform.rotate(surf2, -65)
sc.blit(surf3, (370, 516))
pygame.draw.circle(sc, (221, 233, 175),
                   (412, 558), 20)
surf4 = pygame.Surface((55, 12))
surf4.set_colorkey((0, 0, 0))
pygame.draw.ellipse(surf4, (221, 233, 175),
                    (0, 0, 55, 13))
surf5 = pygame.transform.rotate(surf4, -115)
sc.blit(surf5, (424, 510))
pygame.draw.polygon(sc, (221, 233, 175),
                    [(382, 516), (382, 534), (412, 575), (450, 512)])
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (386, 571, 42, 87))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (355, 457, 20, 15))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (360, 471, 14, 9))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (367, 480, 13, 14))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (375, 495, 8, 11))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (440, 501, 14, 12))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (448, 496, 7, 10))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (454, 481, 12, 13))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (484, 474, 18, 23))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (469, 475, 10, 9))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (373, 626, 25, 35))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (371, 654, 15, 36))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (353, 674, 20, 20))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (376, 576, 20, 20))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (367, 592, 17, 11))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (360, 605, 8, 12))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (421, 578, 20, 20))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (431, 589, 19, 13))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (450, 595, 25, 14))
pygame.draw.ellipse(sc, (0, 0, 0), 
                    (386, 518, 25, 25))
pygame.draw.ellipse(sc, (0, 0, 0), 
                    (426, 523, 19, 19))
pygame.draw.ellipse(sc, (255, 255, 255), 
                    (399, 531, 7, 7))
pygame.draw.ellipse(sc, (255, 255, 255), 
                    (435, 533, 5, 5))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (412, 638, 22, 31))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (418, 665, 17, 35))
pygame.draw.ellipse(sc, (221, 233, 175), 
                    (432, 686, 20, 20))
pygame.draw.ellipse(sc, (200, 55, 55), 
                    (464, 563, 40, 40))
pygame.draw.arc(sc, (0, 0, 0),
                (482, 545, 100, 50), np.pi-0.7, np.pi, 1)
pygame.draw.polygon(sc, (136, 170, 0),
                    [(486, 558), (484, 555), (482, 546), (486, 555)])
pygame.draw.arc(sc, (34, 43, 0),
                (392, 538, 40, 40), np.pi+0.5, 2*np.pi-0.3,2)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
