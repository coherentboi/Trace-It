import json
import pygame
import os

from graphics import CANVASBACKGROUND
from variables import BACKBUTTONPOS, BACKBUTTONPOS2, BACKBUTTONSIZE, CANVASHEIGHT, CANVASWIDTH, DELETEBUTTONPOS, NEXTBUTTONPOS, NEXTBUTTONPOS2, NEXTBUTTONSIZE, SCREENHEIGHT, SCREENWIDTH

#Show Previous Drawings
def showPrevious(screen, canvas, next, back2, delete, back):
    """
    Args:
        surface: screen
        canvas: canvas
        Button: next
        Button: back2
        Button: delete
        Button: back
    
    Returns:
        bool
    
    Allows user to scroll through previous drawings
    """

    #Running Variable
    running = True

    #Get Image + Image Count
    images, count = getJSONData()

    #Clear Canvas
    canvas.clear()

    #Slide Number Variable
    slideNum = 0

    #Running Loop
    while running:

        #Blit Background + Back Button + Canvas
        screen.blit(CANVASBACKGROUND(), (0,0))
        screen.blit(back.surf, BACKBUTTONPOS)
        screen.blit(canvas.surf, (SCREENWIDTH/2 - CANVASWIDTH/2, SCREENHEIGHT/2 - CANVASHEIGHT/2))

        #Configure Back Button
        back.configButton(screen)

        #Checks if there are previous drawings
        if(len(images) == 0):
            #No Previous Drawings Screen
            canvas.noPreviousDrawings()
        else:
            #Blit Delete Button
            screen.blit(delete.surf, DELETEBUTTONPOS)
            
            #Display Image
            canvas.displayPrevious(images[slideNum])
            
            #If First Slide
            if(slideNum != 0):
                screen.blit(back2.surf, BACKBUTTONPOS2)
                back2.configButton(screen)
            
            #If Last Slide
            if(slideNum != len(images)-1):
                screen.blit(next.surf, NEXTBUTTONPOS2)
                next.configButton(screen)
            
            #Config Delete
            delete.configButton(screen)
            
        #Event Loop
        for event in pygame.event.get():
            
            #If Quit
            if event.type == pygame.QUIT:
                return False

            #If Mouse Clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]   
                mouseDown = True      

                #Back To Menu
                if(x >= BACKBUTTONPOS[0] and x <= BACKBUTTONPOS[0] + BACKBUTTONSIZE[0] and y >= BACKBUTTONPOS[1] and y <= BACKBUTTONPOS[1] + BACKBUTTONSIZE[1]):         
                    return True

                #Next Image
                if(x >= NEXTBUTTONPOS2[0] and x <= NEXTBUTTONPOS2[0] + NEXTBUTTONSIZE[0] and y >= NEXTBUTTONPOS2[1] and y <= NEXTBUTTONPOS2[1] + NEXTBUTTONSIZE[1]) and (slideNum != len(images)-1):         
                    if(slideNum != len(images)-1):
                        slideNum += 1

                #Previous Image
                if(x >= BACKBUTTONPOS2[0] and x <= BACKBUTTONPOS2[0] + NEXTBUTTONSIZE[0] and y >= BACKBUTTONPOS2[1] and y <= BACKBUTTONPOS2[1] + NEXTBUTTONSIZE[1]) and (slideNum != 0):         
                    if(slideNum != 0):
                        slideNum -= 1
                
                #Delete Image From JSON
                if(x >= DELETEBUTTONPOS[0] and x <= DELETEBUTTONPOS[0] + NEXTBUTTONSIZE[0] and y >= DELETEBUTTONPOS[1] and y <= DELETEBUTTONPOS[1] + NEXTBUTTONSIZE[1]) and len(images) != 0:         
                    os.remove(os.path.join("previous", images[slideNum]))
                    images.pop(slideNum)
                    writeJSONData({"images": images, "count": count})
                    if(slideNum != 0):
                        slideNum -= 1

            #If Mouse Up
            if event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False

        #Update Display
        pygame.display.update()

#Gets And Parses JSON Data
def getJSONData():
    """
    Args:
        None
    Returns:
        list: data['images']
        int: data['count']
    
    Reads and parses data to JSON file.
    """
    f = open('drawings.json', "r")
    data = json.loads(f.read())

    return data['images'], data['count']

#Writes JSON Data To File
def writeJSONData(data):
    """
    Args:
        dict: data
    Returns:
        None
    
    Writes data to JSON file.
    """
    f = open('drawings.json', "w")
    json.dump(data, f)