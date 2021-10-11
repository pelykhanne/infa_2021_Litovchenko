import pygame
import pygame.draw

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))

# Библиотека цветов

black = (0, 0, 0)
red_fish = (210, 0, 0)
grey_fish = (160, 160, 160)
blue_fish = (0, 0, 255)
white_bear = (240, 255, 255)
yellow_sun = (240, 230, 140)
blue_sky = (135, 206, 250)

def bear(x, y, orientation, size):
    '''
    Функция рисует медведя.
    x и y - координаты медведя.
    orientation - ориентация медведя (при 1 - смотрит вправо, при -1 - смотрит влево).
    size - коэффициент размера.
    '''
    pygame.draw.ellipse(screen, white_bear, (x+100*orientation*size-50*size+50*orientation*size,y+300*size,100*size,200*size))
    pygame.draw.ellipse(screen, black, (x+100*orientation*size-50*size+50*size*orientation,y+300*size,100*size,200*size),1)
    pygame.draw.ellipse(screen, white_bear, (x+140*orientation*size-35*size+35*orientation*size,y+270*size,70*size,40*size))
    pygame.draw.ellipse(screen, black, (x+140*orientation*size-35*size+35*orientation*size,y+270*size,70*size,40*size),1)
    pygame.draw.circle(screen, black, (x+170*orientation*size,y+284*size),4*size)
    pygame.draw.circle(screen, black, (x+208*orientation*size,y+288*size),4*size)
    pygame.draw.ellipse(screen, white_bear, (x+163*orientation*size-40*size+40*orientation*size,y+338*size,80*size,35*size))
    pygame.draw.ellipse(screen, black, (x+163*orientation*size-40*size+40*orientation*size,y+338*size,80*size,35*size),1)
    pygame.draw.ellipse(screen, white_bear, (x+140*orientation*size-40*size+40*orientation*size,y+450*size,80*size,60*size))
    pygame.draw.ellipse(screen, black, (x+140*orientation*size-40*size+40*orientation*size,y+450*size,80*size,60*size),1)
    pygame.draw.ellipse(screen, white_bear, (x+183*orientation*size-30*size+30*orientation*size,y+487*size,60*size,28*size))
    pygame.draw.ellipse(screen, black, (x+183*orientation*size-30*size+30*orientation*size,y+487*size,60*size,28*size),1)
    pygame.draw.circle(screen, white_bear, (x+146*orientation*size,y+274*size),7*size)
    pygame.draw.circle(screen, black, (x+146*orientation*size,y+274*size),7*size,1)

def rod(x, y, orientation, size):
    '''
    Функция рисует удочку.
    x и y - координаты удочки.
    orientation - ориентация удочки (при 1 - смотрит вправо, при -1 - смотрит влево).
    size - коэффициент размера.
    '''
    s = pygame.Surface((30*size,200*size),pygame.SRCALPHA)
    s.set_alpha(100)
    pygame.draw.ellipse(s, black,(0,0,100*size,200*size),3)
    s2=pygame.transform.rotate(s,-90+45*orientation)
    screen.blit(s2,(x+190*orientation*size-80*size+80*orientation*size,y+190*size))
    pygame.draw.line(screen, black, (x+341*orientation*size,y+220*size),(x+341*orientation*size,y+440*size))

def hole(x, y, orientation, size):
    '''
    Функция рисует прорубь.
    x и y - координаты проруби.
    orientation - ориентация проруби (при 1 - смотрит вправо, при -1 - смотрит влево).
    size - коэффициент размера.
    '''
    pygame.draw.ellipse(screen, (105, 105, 105), (x+291*orientation*size-50*size+50*orientation*size,y+410*size,100*size,45*size))
    pygame.draw.ellipse(screen, (47, 79, 79), (x+301*orientation*size-40*size+40*orientation*size,y+425*size,80*size,30*size))

def sun():   
    '''
    функция рисует Солнце.
    '''
    pygame.draw.circle(screen,yellow_sun,(275,105),100)
    pygame.draw.circle(screen,blue_sky,(275,105),80)
    pygame.draw.circle(screen,yellow_sun,(275,105),20)
    pygame.draw.rect(screen, yellow_sun, (180, 97, 190, 20))
    pygame.draw.rect(screen, yellow_sun, (265, 18, 20, 180))

def background():
    '''
    Функция рисует задний фон (небо и снег ).
    '''
    pygame.draw.rect(screen, white_bear, (0, 350, 400, 250))
    pygame.draw.rect(screen, blue_sky, (0, 0, 400, 350))

background()

def fish(x,y,orientation,size):
    '''
    Функция рисует рыбу.
    x и y - координаты рыбы.
    orientation - ориентация рыбы (при 1 - смотрит вправо, при -1 - смотрит влево).
    size - коэффициент размера.
    '''
    pygame.draw.ellipse(screen, grey_fish, (x + 21 * orientation * size - 20 * size + 20 * orientation * size, y + 16 * size, 40 * size, 15 * size))
    pygame.draw.ellipse(screen, black, (x + 21 * orientation * size - 20 * size + 20 * orientation * size, y + 16 * size, 40 * size, 15 * size), 1)
    pygame.draw.polygon(screen,red_fish,[(x+8*size*orientation,y+14*size),(x+21*size*orientation,y+22*size),(x+11*size*orientation,y+31*size),(x+8*size*orientation,y+14*size)])
    pygame.draw.polygon(screen, red_fish, [(x+32*size*orientation, y+9*size), (x+42*size*orientation, y+8*size), (x+48*size*orientation, y+16*size), (x+37*size*orientation, y+16*size), (x+32*size*orientation, y+9*size)])
    pygame.draw.polygon(screen, red_fish, [(x+34*size*orientation, y+29*size), (x+50*size*orientation, y+29*size), (x+47*size*orientation, y+34*size), (x+31*size*orientation, y+34*size), (x+34*size*orientation, y+29*size)])
    pygame.draw.circle(screen, blue_fish, (x+52*size*orientation, y+21*size), 2 * size)

def MEBEB(x, y, orientation, size):
    '''
    Функция рисует МИБИБА.
    x и y - координаты МИБИБА.
    orientation - ориентация МИБИБА (при 1 - смотрит вправо, при -1 - смотрит влево).
    size - коэффициент размера.
    '''
    hole(x, y, orientation, size)
    rod(x, y, orientation, size)
    bear(x, y, orientation, size)
    fish(x + 410 * size * orientation, y  + 455 * size, -1 * orientation, 1 * size)
    fish(x + 280 * size * orientation, y  + 440 * size, 1 * orientation, 1 * size)
    fish(x + 345 * size * orientation, y  + 378 * size, -1 * orientation, 1 * size)
    fish(x + 300 * size * orientation, y  + 360 * size, 1 * orientation, 1 * size)
    fish(x + 410 * size * orientation, y  + 383 * size, -1 * orientation, 1 * size)

    pygame.draw.line(screen, black, (x+341*orientation*size,y+220*size),(x+341*orientation*size,y+440*size))

MEBEB(500,100, -1, 0.8)
MEBEB(-35,170, 1, 0.5)
MEBEB(-120,180, 1, 0.85)

sun()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)

pygame.quit()
