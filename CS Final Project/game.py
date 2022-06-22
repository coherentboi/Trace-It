import pygame
import os
from grade import gradeApi
from graphics import CANVASBACKGROUND
from previous import getJSONData, writeJSONData

from variables import BACKBUTTONPOS, BACKBUTTONSIZE, BACKGROUNDCOLOR, FONT, PROGRESSBARWIDTH, SCREENWIDTH, SCREENHEIGHT, BODYWIDTH, BODYHEIGHT, CANVASTOPLEFT, CANVASBORDERTHICKNESS, CANVASWIDTH, CANVASHEIGHT, PENSIZE, TEXTPOSBOTTOM, TEXTPOSTOP, TIMERSIZEX, TIMERSIZEY
from setup import removeGrading

class DrawingPen(pygame.sprite.Sprite):
    def __init__(self):
        super(DrawingPen, self).__init__()

        #Create Circle Surface
        self.pointer = pygame.Surface((PENSIZE*2, PENSIZE*2), pygame.SRCALPHA, 32)
        self.pointer.convert_alpha()
        pygame.draw.circle(self.pointer, (0,0,0), (PENSIZE, PENSIZE), PENSIZE)

def configMouse(screen, canvas, kill =  False):
    """
    Args:
        Surface: screen
        Canvas: canvas
        boolean: kill = False

    Returns:
        none

    Function blits pen on canvas.
    """

    #Blit Canvas to Screen
    screen.blit(canvas.surf, (SCREENWIDTH/2 - CANVASWIDTH/2, SCREENHEIGHT/2 - CANVASHEIGHT/2))

    #Get Mouse Pos
    x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] 

    #Initialize Drawing Pen
    pen = DrawingPen()

    #Check If Inside Canvas Frame
    if(x >= CANVASTOPLEFT[0]+PENSIZE and x <= CANVASTOPLEFT[0] - PENSIZE + CANVASWIDTH and y >= CANVASTOPLEFT[1] + PENSIZE and y <= CANVASTOPLEFT[1] - PENSIZE + CANVASHEIGHT):
        pygame.mouse.set_visible(False)
        if(not kill):
            screen.blit(pen.pointer, (x-PENSIZE, y-PENSIZE))
    else: 
        pygame.mouse.set_visible(True)
        pen.kill()

def start(screen, canvas, back):
    """
    Args: 
        Surface: screen
        Canvas: canvas
        Button: back
    
    Returns:
        boolean

    Function starts the game.
    """

    #Blit Background
    screen.blit(CANVASBACKGROUND(), (0,0))

    #Blit Back Button
    screen.blit(back.surf, BACKBUTTONPOS)
    
    #Remove Previous Drawings
    removeGrading()

    #Display Image Function
    play, originalImage = displayImage(screen, canvas, 10, back)

    #Check If User Quits
    if(play == 1):
        return True
    elif(play == 0):
        return False

    #Play Game Function
    play = game(screen, canvas, 30, back)
    
    #Check If User Quits
    if(play == 1):
        return True
    elif(play == 0):
        return False
    
    #Grade Drawing Function
    play = grade(screen, canvas, originalImage, back)
    
    #Check If User Quits
    if(play == 0):
        return False
    return True

def displayImage(screen, canvas, time, back):
    """
    Args:
        Surface: screen
        Canvas: canvas
        int: time
        Button: back

    Returns:
        int
        str: originalImage

    Function starts first portion of the game, displays image to user.
    """

    #Define Mouse Variables
    mouseDown = False
    x = 0
    y = 0

    #Running Variable
    running = True

    #Get Image From Display Image Function --> Canvas Also Displays Image
    originalImage = canvas.displayImage()

    #Set Up Font And Text Fields
    font = pygame.font.Font(FONT, 20)
    textSurfTop = pygame.surface.Surface((TIMERSIZEX, TIMERSIZEY), pygame.SRCALPHA, 32)
    textSurfBottom = pygame.surface.Surface((TIMERSIZEX,TIMERSIZEY), pygame.SRCALPHA, 32)

    #Write "Memorize Image" On Top
    textTop = font.render("MEMORIZE THE IMAGE", True, (0, 0, 0))
    textSurfTop.fill(BACKGROUNDCOLOR)
    textRectTop = textTop.get_rect()
    textSurfTop.blit(textTop, ((TIMERSIZEX-textRectTop[2])/2,(TIMERSIZEY-textRectTop[3])/2))
    screen.blit(textSurfTop, TEXTPOSTOP)

    #Set Countdown Clock
    countdown = time
    TICK = pygame.USEREVENT + 100
    pygame.time.set_timer(TICK, 1000, time)

    #Set Delay
    WAIT = pygame.USEREVENT + 101

    #Game Loop
    while running:

        #Configure Mouse
        configMouse(screen, canvas, True)

        #Configure Back Button
        back.configButton(screen)
        
        #Display Countdown On Bottom 
        textBottom = font.render(str(countdown), True, (0, 0, 0))
        textRectBottom = textBottom.get_rect()
        textSurfBottom.fill(BACKGROUNDCOLOR)
        textSurfBottom.blit(textBottom, ((TIMERSIZEX-textRectBottom[2])/2,(TIMERSIZEY-textRectBottom[3])/2))
        screen.blit(textSurfBottom,TEXTPOSBOTTOM)

        #Event Loop
        for event in pygame.event.get():

            #Check If Mouse Down
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]  
                if(x >= BACKBUTTONPOS[0] and x <= BACKBUTTONPOS[0] + BACKBUTTONSIZE[0] and y >= BACKBUTTONPOS[1] and y <= BACKBUTTONPOS[1] + BACKBUTTONSIZE[1]):  
                    return 1, "none"

            #Check If Mouse Up
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False

            #Countdown + Set Delay
            if event.type == TICK:
                countdown -= 1
                if(countdown == 0):
                    countdown = "TIME TO DRAW!"
                    canvas.clear()
                    pygame.time.set_timer(WAIT, 2000, 1)

            #Check if Delay is Up
            if event.type == WAIT:
                return 2, originalImage

            #Check if User Quits
            if event.type == pygame.QUIT:
                return 0
        
        #Update Display
        pygame.display.update()

def game(screen, canvas, time, back):
    """
    Args:
        Surface: screen
        Canvas: canvas
        int: time
        Button: back
    
    Returns:
        int
    
    Funtion is drawing portion of the game.
    """

    #Set Mouse Variables
    mouseDown = False
    x = 0
    y = 0

    #Start Drawing
    draw = True

    #Running Variable
    running = True

    #Initialize Countdown
    countdown = time

    #Write "Replicate Image" At Top
    font = pygame.font.Font(FONT, 20)
    textSurfTop = pygame.surface.Surface((TIMERSIZEX, TIMERSIZEY), pygame.SRCALPHA, 32)
    textSurfBottom = pygame.surface.Surface((TIMERSIZEX,TIMERSIZEY), pygame.SRCALPHA, 32)
    textTop = font.render("REPLICATE THE IMAGE", True, (0, 0, 0))
    textSurfTop.fill(BACKGROUNDCOLOR)
    textRectTop = textTop.get_rect()
    textSurfTop.blit(textTop, ((TIMERSIZEX-textRectTop[2])/2,(TIMERSIZEY-textRectTop[3])/2))
    screen.blit(textSurfTop, TEXTPOSTOP)

    #Set Up Countdown
    TICK = pygame.USEREVENT + 102
    pygame.time.set_timer(TICK, 1000, time)
    WAIT = pygame.USEREVENT + 103

    #Game Loop
    while(running):

        #Blit Countdown To Screen
        textBottom = font.render(str(countdown), True, (0, 0, 0))
        textRectBottom = textBottom.get_rect()
        textSurfBottom.fill(BACKGROUNDCOLOR)
        textSurfBottom.blit(textBottom, ((TIMERSIZEX-textRectBottom[2])/2,(TIMERSIZEY-textRectBottom[3])/2))
        screen.blit(textSurfTop, TEXTPOSTOP)
        screen.blit(textSurfBottom,TEXTPOSBOTTOM)

        #Blit Mouse To Screen Depending On Game Status
        if(draw):
            configMouse(screen, canvas)
        else:
            configMouse(screen, canvas, True)

        #Config Button To Screen
        back.configButton(screen)

        #Event Game Loop
        for event in pygame.event.get():
            
            #Check If Mouse Clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]    
                if(x >= BACKBUTTONPOS[0] and x <= BACKBUTTONPOS[0] + BACKBUTTONSIZE[0] and y >= BACKBUTTONPOS[1] and y <= BACKBUTTONPOS[1] + BACKBUTTONSIZE[1]):  
                    return 1

            #Check If Mouse Up
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False

            #Check If Countdown Finished
            if event.type == TICK:
                countdown -= 1
                if(countdown == 0):
                    countdown = "TIME'S UP!"
                    draw = False
                    pygame.time.set_timer(WAIT, 4000, 1)

            #Check If Delay Up
            if event.type == WAIT:
                return 2

            #Check If User Quit
            if event.type == pygame.QUIT:
                return 0

        #If Mousedown, Draw
        if(draw and mouseDown and (x >= CANVASTOPLEFT[0] and x <= CANVASTOPLEFT[0] + CANVASWIDTH and y >= CANVASTOPLEFT[1] and y <= CANVASTOPLEFT[1] + CANVASHEIGHT)):
            #Draw Function
            canvas.draw()
        
        #Update Display
        pygame.display.update()

def grade(screen, canvas, originalImage, back):
    """
    Args:
        Surface: screen
        Canvas: canvas
        str: originalImage
        Button: back

    Return:
        int
    """

    #Mousedown Variable
    mouseDown = False

    #Loop Variable
    running = True

    #Blit Text To Bottom
    font = pygame.font.Font(FONT, 20)
    textSurf = pygame.surface.Surface((TIMERSIZEX,TIMERSIZEY), pygame.SRCALPHA, 32)
    text = font.render("", True, (0, 0, 0))
    textRect = text.get_rect()
    textSurf.fill(BACKGROUNDCOLOR)
    textSurf.blit(text, ((TIMERSIZEX-textRect[2])/2,(TIMERSIZEY-textRect[3])/2))
    screen.blit(textSurf,TEXTPOSBOTTOM)

    #Get and Save User Drawing
    drawing = pygame.Rect(CANVASTOPLEFT[0], CANVASTOPLEFT[1], CANVASWIDTH, CANVASHEIGHT)
    image = screen.subsurface(drawing)
    pygame.image.save(image, "grading/drawing.jpg")
    images, count = getJSONData()
    pygame.image.save(image, f"previous/{count+1}.png")
    images.insert(0, f"{count+1}.png")
    count += 1

    #Update JSON
    writeJSONData({"images": images, "count" : count})

    #Render Text
    text = font.render("ORIGINAL DRAWING", True, (0, 0, 0))
    textRect = text.get_rect()
    textSurf.fill(BACKGROUNDCOLOR)
    textSurf.blit(text, ((TIMERSIZEX-textRect[2])/2,(TIMERSIZEY-textRect[3])/2))
    screen.blit(textSurf,TEXTPOSTOP)

    #Display Image On Canvas
    canvas.displayChosen(originalImage)

    #Set Timers
    TICK = pygame.USEREVENT + 110
    pygame.time.set_timer(TICK, 4000, 1)
    WAIT = pygame.USEREVENT + 111
    PROGRESS = pygame.USEREVENT + 112
    SCORE = pygame.USEREVENT + 113

    #Progress Bar Variable
    progress = 0

    #Grade Drawing
    grade = (gradeApi(originalImage))

    #4 Checkpoints
    check1 = True
    check2 = True
    check3 = True
    check4 = True

    #Running Loop
    while(running):

        #Configure Mouse
        configMouse(screen, canvas, True)
        back.configButton(screen)

        #Event Loop
        for event in pygame.event.get():

            #If Click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]    
                if(x >= BACKBUTTONPOS[0] and x <= BACKBUTTONPOS[0] + BACKBUTTONSIZE[0] and y >= BACKBUTTONPOS[1] and y <= BACKBUTTONPOS[1] + BACKBUTTONSIZE[1]):  
                    return 1

            #If First Checkpoint
            if event.type == TICK and check1:

                #Blit "Your Drawing" To Screen
                text = font.render("YOUR DRAWING", True, (0, 0, 0))
                textRect = text.get_rect()
                textSurf.fill(BACKGROUNDCOLOR)
                textSurf.blit(text, ((TIMERSIZEX-textRect[2])/2,(TIMERSIZEY-textRect[3])/2))
                screen.blit(textSurf,TEXTPOSTOP)

                #Canvas Display Drawing
                canvas.clear()
                canvas.displayDrawing()

                pygame.time.set_timer(WAIT, 2000, 1)

            #If Second Checkpoint
            if event.type == WAIT and check2:
                check1 = False

                #Blit "Grading" To Screen
                text = font.render("GRADING", True, (0, 0, 0))
                textRect = text.get_rect()
                textSurf.fill(BACKGROUNDCOLOR)
                textSurf.blit(text, ((TIMERSIZEX-textRect[2])/2,(TIMERSIZEY-textRect[3])/2))
                screen.blit(textSurf,TEXTPOSTOP)

                pygame.time.set_timer(PROGRESS, 10, PROGRESSBARWIDTH)

            #If Third Checkpoint
            if event.type == PROGRESS and check3:
                check2 = False

                #Blit "Grading" To Screen
                text = font.render("GRADING", True, (0, 0, 0))
                textRect = text.get_rect()
                textSurf.fill(BACKGROUNDCOLOR)
                textSurf.blit(text, ((TIMERSIZEX-textRect[2])/2,(TIMERSIZEY-textRect[3])/2))
                screen.blit(textSurf,TEXTPOSTOP)

                #Progress Bar
                if(progress == PROGRESSBARWIDTH-1):
                    pygame.time.set_timer(SCORE, 1000, 1)
                    check3 = False
                progress += 1
                canvas.progressBar(progress)

            #If Fourth Checkpoint
            if event.type == SCORE and check4:
                check3 = False

                #Blit "Your Score" To Screen
                text = font.render("YOUR SCORE:", True, (0, 0, 0))
                textRect = text.get_rect()
                textSurf.fill(BACKGROUNDCOLOR)
                textSurf.blit(text, ((TIMERSIZEX-textRect[2])/2,(TIMERSIZEY-textRect[3])/2))
                screen.blit(textSurf,TEXTPOSTOP)

                #Display Grade
                canvas.displayScore(grade)
                check4 = False

            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False

            if event.type == pygame.QUIT:
                return 0

        #Update Screen
        pygame.display.update()