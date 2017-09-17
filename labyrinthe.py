"""
 Aider MacGyver à s'échapper
Jeu dans lequel on doit déplacer McGyver à travers un labyrinthe
 et lui faire ramasser des objets pour qu'il puisse endormir le garde à la fin 
 du niveau et sortir.

 Script Python
 Fichiers : labyrinthe.py, classes.py, constantes.py, level.txt + images
 """

#Import of the libraries needed
import pygame
from pygame.locals import *
from constantes import *
from classes import *
import random 

#Init of the Pygame library
pygame.init()

#Displaying the windows
Window = pygame.display.set_mode((Window_Size, 480))
#Icone
icone = pygame.image.load(MacGyver).convert_alpha()
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(Window_Title)


#displaying a background for the tile of the maze
Background_Tiles = pygame.image.load(background).convert()
Window.blit(Background_Tiles, (30,30))

#displaying the character .png
Char_img = pygame.image.load(MacGyver).convert_alpha() #Add the png and transparency
"""position_Char = Char.get_rect()
Window.blit(Char, position_Char)"""

#displaying the walls of the maze
wall = pygame.image.load(Wall).convert()

#displaying the objects png's
tubeIMG = pygame.image.load(Tube).convert_alpha()
needleIMG = pygame.image.load(Needle).convert_alpha()
etherIMG = pygame.image.load(Ether).convert_alpha()


#refreshing the screen for the background to be visible over the default one
pygame.display.flip()

#Variable for the infinite loop
continue_game = 1

#Variables to check if the items have been picked or not:
TubeNotPicked = True
EtherNotPicked = True
NeedleNotPicked = True

GAME_WON = False
GAME_LOOSE = False

pygame.key.set_repeat(400, 30) #Moving MaGyver by maintening a arrow_key pressed

level = Level('Level.txt')
level.generate()
level.display(Window)
Mac = Char(Char_img, level)
tube = loot(tubeIMG, level)
tube.display(tubeIMG, Window)
needle = loot(needleIMG, level)
needle.display(needleIMG, Window)
ether = loot(etherIMG, level)
ether.display(etherIMG, Window)


#infinite loop
while continue_game:
    
    pygame.time.Clock().tick(30) #Limiting the loop speed to 30f/s to save processor ressources

    for event in pygame.event.get():    #Seeking every events happening while the game is running
        if event.type == QUIT:  #If any of these events is QUIT type
            continue_game = 0   #Loop is stopped and the game windows is closed

        #Keyboard touch used to moove MacGyver:
        elif event.type == KEYDOWN:
            if event.key == K_DOWN: #If ARROW DOWN pressed
                Mac.mooving('down')
            elif event.key == K_UP:
                Mac.mooving('up')
            elif event.key == K_LEFT:
                Mac.mooving('left')
            elif event.key == K_RIGHT:
                Mac.mooving('right')


    #Re-pasting after the events
    Window.blit(Background_Tiles, (0,30))
    level.display(Window)
    Window.blit(Mac.Image, (Mac.x, Mac.y))

    if TubeNotPicked :
        Window.blit(tube.Loot_Image, (tube.x, tube.y))
    if (Mac.x, Mac.y) == (tube.x, tube.y):
        TubeNotPicked = False
        Window.blit(tube.Loot_Image, (0, 0))
        


    if NeedleNotPicked :    
        Window.blit(needle.Loot_Image, (needle.x, needle.y))
    if (Mac.x, Mac.y) == (needle.x, needle.y):
        NeedleNotPicked = False
        Window.blit(needle.Loot_Image, (10, 0))
        


    if EtherNotPicked :
        Window.blit(ether.Loot_Image, (ether.x, ether.y))
    if (Mac.x, Mac.y) == (ether.x, ether.y):
        EtherNotPicked = False
        Window.blit(ether.Loot_Image, (30, 0))
        

    #refreshing screen
    pygame.display.flip()


    #EndGame Victory or loose
    if level.structure[Mac.case_y][Mac.case_x] == 'a': #If MacGyver reach the guard :
        if TubeNotPicked == False and NeedleNotPicked == False and EtherNotPicked == False :  # If every objects have been looted, he won.
            GAME_WON = True
        else :
            GAME_LOOSE = True  # Else it's game over !
                    

    if GAME_WON == True :
        Window.blit(Background_Tiles, (0, 30)) # draw over everything on the screen now by re-drawing the background
        font = pygame.font.Font(None, 25)
        text = font.render("You won ! MacGyver is safe thanks to you !", 1, (255,255,255))
        textrect = text.get_rect()
        textrect.centerx, textrect.centery = Window_Size/2,Window_Size/2
        Window.blit(text, textrect)

        pygame.display.flip()

    if GAME_LOOSE == True :
        Window.blit(Background_Tiles, (0, 30)) # draw over everything on the screen now by re-drawing the background
        font = pygame.font.Font(None, 25)
        text = font.render("Game over! You just died.", 1, (255,255,255))
        textrect = text.get_rect()
        textrect.centerx, textrect.centery = Window_Size/2,Window_Size/2
        Window.blit(text, textrect)

        pygame.display.flip()
        """continuer = 0"""



