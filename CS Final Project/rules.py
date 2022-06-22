import pygame
from graphics import CANVASBACKGROUND, RULESBACKGROUND

from variables import BACKBUTTONPOS, BACKBUTTONSIZE, NEXTBUTTONPOS, NEXTBUTTONSIZE

def openRules(screen, next, back):

    running = True
    slideNum = 1

    while running:

        screen.blit(RULESBACKGROUND(slideNum), (0,0))
        screen.blit(back.surf, BACKBUTTONPOS)
        screen.blit(next.surf, NEXTBUTTONPOS)

        back.configButton(screen)
        next.configButton(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]   
                mouseDown = True      
                if(x >= BACKBUTTONPOS[0] and x <= BACKBUTTONPOS[0] + BACKBUTTONSIZE[0] and y >= BACKBUTTONPOS[1] and y <= BACKBUTTONPOS[1] + BACKBUTTONSIZE[1]):         
                    return True
                if(x >= NEXTBUTTONPOS[0] and x <= NEXTBUTTONPOS[0] + NEXTBUTTONSIZE[0] and y >= NEXTBUTTONPOS[1] and y <= NEXTBUTTONPOS[1] + NEXTBUTTONSIZE[1]):         
                    if(slideNum == 3):
                        return True
                    slideNum += 1

            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False

        pygame.display.update()