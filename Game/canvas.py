import pygame
import os
import random

from variables import CANVASBORDERTHICKNESS, CANVASWIDTH, CANVASHEIGHT, BODYWIDTH, BODYHEIGHT, FONT, PROGRESSBARHEIGHT, PROGRESSBARWIDTH, SCREENHEIGHT, SCREENWIDTH, PENSIZE

#Create Canvas
class Canvas(pygame.sprite.Sprite):
    """
    Attributes:
        surface: body
        surface: surf
        str: image
        surface: loadImage
    
    Methods:
        draw()
        displayImage()
        displayChosen()
        displayDrawing()
        displayPrevious()
        clear()
        progressBar()
        displayScore()
        displayPrevious()
        noPreviousDrawings()
    """
    def __init__(self):
        super(Canvas, self).__init__()
        self.body = pygame.Surface((BODYWIDTH, BODYHEIGHT), pygame.SRCALPHA, 32)
        self.body = self.body.convert_alpha()
        self.surf = pygame.Surface((CANVASWIDTH, CANVASHEIGHT))
        self.surf.fill((255,255,255))

        self.body.blit(self.surf, (BODYWIDTH/2 - CANVASWIDTH/2, BODYHEIGHT/2 - CANVASHEIGHT/2))

    def draw(self):
        """
        Args:
            none
        Return:
            none
        
        Draws one black circle on canvas (user drawing).
        """
        pygame.draw.circle(self.surf, (0,0,0), (pygame.mouse.get_pos()[0]-(SCREENWIDTH/2-CANVASWIDTH/2), pygame.mouse.get_pos()[1]-(SCREENHEIGHT/2-CANVASHEIGHT/2)),PENSIZE)
        self.body.blit(self.surf, (BODYWIDTH/2 - CANVASWIDTH/2, BODYHEIGHT/2 - CANVASHEIGHT/2))

    def displayImage(self):
        """
        Args:
            none
        Returns:
            str: image
        
        Chooses and displays random image for user.
        """
        #Gets Random Image
        self.image = random.choice(os.listdir("images"))

        #Blit Image To Screen
        self.loadImage = pygame.image.load(os.path.join("images", self.image))
        self.surf.blit(self.loadImage, (0,0))
        return self.image

    def displayChosen(self, image):
        """
        Args:
            str: image
        Returns:
            none
        
        Displays chosen image to user
        """
        self.surf.blit(pygame.image.load(os.path.join("images", image)),(0,0))

    def displayDrawing(self):
        """
        Args:
            none
        Returns:
            none
        
        Displays graded drawing to user
        """
        self.surf.blit(pygame.image.load(os.path.join("grading", "drawing.jpg")),(0,0))

    def displayPrevious(self, name):
        """
        Args:
            name
        Returns:
            none
        
        Redundant Function (Too scared to remove as may mess up code) --> displays a previous drawing from grading folder.
        """
        self.surf.blit(pygame.image.load(os.path.join("grading", f"{name}.jpg")))

    def clear(self):
        """
        Args:
            none
        Returns:
            none
        
        Fills the canvas with white
        """
        self.surf.fill((255,255,255))

    def progressBar(self, value):
        """
        Args:
            int: value
        Returns:
            none
        
        Display progress bar with value passed.
        """
        #Clear Screen
        self.clear()

        #Load And Blit Progress Bar
        progress = pygame.Surface((value, PROGRESSBARHEIGHT))
        progress.fill(pygame.Color("#dcf4fc"))
        blank = pygame.Surface((PROGRESSBARWIDTH, PROGRESSBARHEIGHT))
        blank.fill((255,255,255))
        blank.blit(progress, (0,0))
        trace = pygame.Surface((PROGRESSBARWIDTH+4, PROGRESSBARHEIGHT+4))
        trace.fill((0,0,0))
        trace.blit(blank, (2,2))
        self.surf.blit(trace, (CANVASWIDTH/2-PROGRESSBARWIDTH/2-2, CANVASHEIGHT/2-PROGRESSBARHEIGHT/2-2))

    def displayScore(self, grade):
        """
        Args:
            int: grade
        Returns:
            none
        
        Displays score on canvas
        """

        #Blit Score To Canvas
        self.clear()
        font = pygame.font.Font(FONT, 40)
        text = font.render(f"{grade}%", True, (0, 0, 0))
        textRect = text.get_rect()
        self.surf.blit(text, ((CANVASWIDTH-textRect[2])/2,(CANVASHEIGHT-textRect[3])/2))

    def displayPrevious(self, image):
        """
        Args:
            str: image
        Returns:
            none
        
        Displays a previous image to user
        """
        
        self.clear()
        self.loadImage = pygame.image.load(os.path.join("previous", image))
        self.surf.blit(self.loadImage, (0,0))

    def noPreviousDrawings(self):
        """
        Args:
            none
        Returns:
            none

        Displays "no previous drawings" screen on canvas.
        """
        self.clear()
        font = pygame.font.Font(FONT, 20)
        text = font.render("NO PREVIOUS DRAWINGS", True, (0, 0, 0))
        textRect = text.get_rect()
        self.surf.blit(text, ((CANVASWIDTH-textRect[2])/2,(CANVASHEIGHT-textRect[3])/2))