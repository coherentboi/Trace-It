import pygame

from game import configMouse, start

from canvas import Canvas
from graphics import BACKBUTTON1, BACKBUTTON2, HOMEBACKGROUND, PLAYBUTTON1, PLAYBUTTON2, QUITBUTTON1, QUITBUTTON2, RULEBUTTON1, RULEBUTTON2, SETTINGSBUTTON1, SETTINGSBUTTON2, Button
from previous import showPrevious
from setup import removeGrading
from rules import openRules

from variables import BACKBUTTONCOL1, BACKBUTTONCOL2, BACKBUTTONPOS, BACKBUTTONPOS2, BACKBUTTONSIZE, BACKGROUNDCOLOR, BODYHEIGHT, BODYWIDTH, CANVASBORDERTHICKNESS, CANVASTOPLEFT, DELETEBUTTONPOS, FONT, NEXTBUTTONCOL1, NEXTBUTTONCOL2, NEXTBUTTONPOS, NEXTBUTTONPOS2, NEXTBUTTONSIZE, PLAYBUTTONCOL1, PLAYBUTTONCOL2, PLAYBUTTONPOS, PLAYBUTTONSIZE, PREVIOUSBUTTONPOS, QUITBUTTONCOL1, QUITBUTTONCOL2, QUITBUTTONPOS, QUITBUTTONSIZE, RULEBUTTONCOL1, RULEBUTTONCOL2, RULEBUTTONPOS, RULEBUTTONSIZE, SCREENWIDTH, SCREENHEIGHT, CANVASWIDTH, CANVASHEIGHT, SETTINGSBUTTONPOS, SETTINGSBUTTONSIZE, TITLEPOS, TITLESIZE

#Initialize Pygame
pygame.init()

#Setup Screen + Game
screen = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
pygame.display.set_caption("Trace It!")

#Variables for Different Parts of Game
running = True
startGame = False
mouseDown = False
showRules = False
showDrawings = False

#Initialize Canvas
canvas = Canvas()

#Create All Buttons
play = Button(PLAYBUTTONPOS, PLAYBUTTONSIZE, "PLAY", PLAYBUTTON1(), PLAYBUTTON2(), PLAYBUTTONCOL1, PLAYBUTTONCOL2)
previous = Button(PREVIOUSBUTTONPOS, PLAYBUTTONSIZE, "PREVIOUS DRAWINGS", PLAYBUTTON1(), PLAYBUTTON2(), PLAYBUTTONCOL1, PLAYBUTTONCOL2)
rules = Button(RULEBUTTONPOS, RULEBUTTONSIZE, "", RULEBUTTON1(), RULEBUTTON2(), RULEBUTTONCOL1, RULEBUTTONCOL2)
settings = Button(SETTINGSBUTTONPOS, SETTINGSBUTTONSIZE, "", SETTINGSBUTTON1(), SETTINGSBUTTON2(), QUITBUTTONCOL1, QUITBUTTONCOL2)
back = Button(BACKBUTTONPOS, BACKBUTTONSIZE, "BACK", BACKBUTTON1(), BACKBUTTON2(), BACKBUTTONCOL1, BACKBUTTONCOL2)
next = Button(NEXTBUTTONPOS, NEXTBUTTONSIZE, "NEXT", BACKBUTTON1(), BACKBUTTON2(), NEXTBUTTONCOL1, NEXTBUTTONCOL2)
next2 = Button(NEXTBUTTONPOS2, NEXTBUTTONSIZE, "NEXT", BACKBUTTON1(), BACKBUTTON2(), NEXTBUTTONCOL1, NEXTBUTTONCOL2)
back2 = Button(BACKBUTTONPOS2, NEXTBUTTONSIZE, "BACK", BACKBUTTON1(), BACKBUTTON2(), NEXTBUTTONCOL1, NEXTBUTTONCOL2)
delete = Button(DELETEBUTTONPOS, NEXTBUTTONSIZE, "DELETE", BACKBUTTON1(), BACKBUTTON2(), NEXTBUTTONCOL1, NEXTBUTTONCOL2)
quit = Button(QUITBUTTONPOS, QUITBUTTONSIZE, "QUIT", QUITBUTTON1(), QUITBUTTON2(), QUITBUTTONCOL1, QUITBUTTONCOL2)

#Main Game Loop
while running:

    #Blit Background
    screen.blit(HOMEBACKGROUND(), (0,0))
    
    #Blit Buttons
    screen.blit(play.surf, PLAYBUTTONPOS)
    screen.blit(previous.surf, PREVIOUSBUTTONPOS)
    screen.blit(rules.surf, RULEBUTTONPOS)
    screen.blit(quit.surf, QUITBUTTONPOS)

    #Config Buttons
    play.configButton(screen)
    rules.configButton(screen)
    previous.configButton(screen)
    settings.configButton(screen)
    quit.configButton(screen)

    #Title Text
    font = pygame.font.Font(FONT, 120)
    title = font.render("TRACE IT!", True, (0,0,0))
    titleSurf = pygame.surface.Surface(TITLESIZE, pygame.SRCALPHA, 32)
    titleSurf.fill(BACKGROUNDCOLOR)
    titleRect = title.get_rect()
    titleSurf.blit(title, (((TITLESIZE[0]-titleRect[2]))/2, (TITLESIZE[1]-titleRect[3])/2))
    screen.blit(titleSurf, TITLEPOS)

    #Event Loop
    for event in pygame.event.get():

        #Quit Game
        if event.type == pygame.QUIT:
            running = False

        #If Clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]   
            mouseDown = True

            #If Click On Start      
            if(x >= PLAYBUTTONPOS[0] and x <= PLAYBUTTONPOS[0] + PLAYBUTTONSIZE[0] and y >= PLAYBUTTONPOS[1] and y <= PLAYBUTTONPOS[1] + PLAYBUTTONSIZE[1]):         
                startGame = True
            #If Click On Previous
            if(x >= PREVIOUSBUTTONPOS[0] and x <= PREVIOUSBUTTONPOS[0] + PLAYBUTTONSIZE[0] and y >= PREVIOUSBUTTONPOS[1] and y <= PREVIOUSBUTTONPOS[1] + PLAYBUTTONSIZE[1]):         
                showDrawings = True

            #If Click On Rules
            if(x >= RULEBUTTONPOS[0] and x <= RULEBUTTONPOS[0] + RULEBUTTONSIZE[0] and y >= RULEBUTTONPOS[1] and y <= RULEBUTTONPOS[1] + RULEBUTTONSIZE[1]):         
                showRules = True

            #If Click On Quit
            if(x >= QUITBUTTONPOS[0] and x <= QUITBUTTONPOS[0] + QUITBUTTONSIZE[0] and y >= QUITBUTTONPOS[1] and y <= QUITBUTTONPOS[1] + QUITBUTTONSIZE[1]):         
                running = False

        #If Mouse Not Clicked
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

    #Start Game
    if(startGame):
        running = start(screen, canvas, back)
        startGame = False

    #Show Previous Drawings
    if(showDrawings):
        running = showPrevious(screen, canvas, next2, back2, delete, back)
        showDrawings = False

    #Show Rules
    if(showRules):
        running = openRules(screen, next, back)
        showRules = False

    #Update Display
    pygame.display.update()

#Quit Game
pygame.quit()