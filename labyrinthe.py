"""
Jeu Aider MacGyver à s'échapper
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
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(MacGyver).convert_alpha()
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)


#displaying a background for the tile of the maze
fond = pygame.image.load(background).convert()
fenetre.blit(fond, (0,0))

#displaying the character .png
perso = pygame.image.load(MacGyver).convert_alpha() #Add the png and transparency
"""position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)"""

#displaying the walls of the maze
wall = pygame.image.load(Wall).convert()

#displaying the objects png's
tubeIMG = pygame.image.load(Tube).convert_alpha()
needleIMG = pygame.image.load(Needle).convert_alpha()
etherIMG = pygame.image.load(Ether).convert_alpha()


#refreshing the screen for the background to be visible over the default one
pygame.display.flip()

#Variable for the infinite loop
continuer = 1

#Variables to check if the items have been picked or not:
TubeNotPicked = True
EtherNotPicked = True
NeedleNotPicked = True

pygame.key.set_repeat(400, 30) #Moving MaGyver by maintening a arrow_key pressed

level = Level('Level.txt')
level.generate()
level.display(fenetre)
Mac = Perso(perso, level)
tube = loot(tubeIMG, level)
tube.display(tubeIMG, fenetre)
needle = loot(needleIMG, level)
needle.display(needleIMG, fenetre)
ether = loot(etherIMG, level)
ether.display(etherIMG, fenetre)

#infinite loop
while continuer:
	
	pygame.time.Clock().tick(30) #Limiting the loop speed to 30f/s to save processor ressources

	for event in pygame.event.get(): 	#Seeking every events happening while the game is running
		if event.type == QUIT:	#If any of these events is QUIT type
			continuer = 0	#Loop is stopped and the game windows is closed

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
	fenetre.blit(fond, (0,0))
	level.display(fenetre)
	fenetre.blit(Mac.Image, (Mac.x, Mac.y))

	if TubeNotPicked :
		fenetre.blit(tube.image_objet, (tube.x, tube.y))
	if NeedleNotPicked :	
		fenetre.blit(needle.image_objet, (needle.x, needle.y))
	if EtherNotPicked :
		fenetre.blit(ether.image_objet, (ether.x, ether.y))

	#refreshing screen
	pygame.display.flip()


	#EndGame Victory or loose
	if level.structure[Mac.case_y][Mac.case_x] == 'a': #If MacGyver reach the guard he win and the game is terminated.
		continuer = 0


