import pygame
import os

from variables import BACKBUTTONCOL1, BACKBUTTONCOL2, BACKBUTTONPOS, FONT, SCREENHEIGHT, SCREENWIDTH

#colour palette:
#e9eaec - silver
#f4dcea - pink
#fcf5cd - yellow
#d4ccac - brown
#dcf4fc - blue

#Loads Homescreen
def HOMEBACKGROUND():
    return pygame.image.load(os.path.join("graphics", "homeBackground.png"))

#Loads Canvas Background
def CANVASBACKGROUND():
    return pygame.image.load(os.path.join("graphics", "canvasBackground.png"))

#Loads Play Button
def PLAYBUTTON1():
    return pygame.image.load(os.path.join("graphics", "PlayButton1.png"))

#Loads Play Button
def PLAYBUTTON2():
    return pygame.image.load(os.path.join("graphics", "PlayButton2.png"))

#Loads Back Button
def BACKBUTTON1():
    return pygame.image.load(os.path.join("graphics", "BackButton1.png"))

#Loads Back Button
def BACKBUTTON2():
    return pygame.image.load(os.path.join("graphics", "BackButton2.png"))

#Loads Rule Button
def RULEBUTTON1():
    return pygame.image.load(os.path.join("graphics", "RuleButton1.png"))

#Loads Rule Button
def RULEBUTTON2():
    return pygame.image.load(os.path.join("graphics", "RuleButton2.png"))

#Loads Rules
def RULESBACKGROUND(num):
    return pygame.image.load(os.path.join("graphics", f"Rules{num}.png"))

#Loads Quit Button
def QUITBUTTON1():
    return pygame.image.load(os.path.join("graphics", "QuitButton1.png"))

#Loads Quit Button
def QUITBUTTON2():
    return pygame.image.load(os.path.join("graphics", "QuitButton2.png"))

#Loads Settings Button
def SETTINGSBUTTON1():
    return pygame.image.load(os.path.join("graphics", "SettingsButton1.png"))

#Loads Settings Button
def SETTINGSBUTTON2():
    return pygame.image.load(os.path.join("graphics", "SettingsButton2.png"))


class Button(pygame.sprite.Sprite):
    """
    Attributes:
        tuple: pos
        tuple: size
        str: text
        pygame.image: c1
        pygame.image: c2
        str: buttonCol1
        str: buttonCol2
    
    Methods:
        configButton()
    """

    def __init__(self, pos, size, text, c1, c2, buttonCol1, buttonCol2):
        super(Button, self).__init__()
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.pos = pos
        self.text = text
        self.buttonCol1 = buttonCol1
        self.buttonCol2 = buttonCol2

        #Blit Button Image 1 To Screen
        self.surf = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.surf = self.surf.convert_alpha()
        self.surf.blit(c1, (0,0))

    def configButton(self, screen):
        """
        Args:
            surface: screen
        Returns:
            none
        
        Adds responsiveness functionality to all buttons.
        """
        #Set Up Mouse
        x, y = pygame.mouse.get_pos()

        #Set Up Font
        font = pygame.font.Font(FONT, 20)
        textSurf = pygame.surface.Surface(self.size, pygame.SRCALPHA, 32)

        #If Inside Button Range
        if(x >= self.pos[0] and x <= self.pos[0] + self.size[0] and y >= self.pos[1] and y <= self.pos[1] + self.size[1]):
            #Blit Second Image (c2)
            self.surf.blit(self.c2, (0,0))
            text = font.render(self.text, True, pygame.Color(self.buttonCol2))
            textRect = text.get_rect()
            textSurf.blit(text, ((self.size[0]-textRect[2])/2,(self.size[1]-textRect[3])/2))
            self.surf.blit(textSurf, (0,0))
            screen.blit(self.surf, self.pos)
        else:
            #Blit First Image (c1)
            self.surf.blit(self.c1, (0,0))
            text = font.render(self.text, True, self.buttonCol1)
            textRect = text.get_rect()
            textSurf.blit(text, ((self.size[0]-textRect[2])/2,(self.size[1]-textRect[3])/2))
            self.surf.blit(textSurf, (0,0))
            screen.blit(self.surf, self.pos)

    