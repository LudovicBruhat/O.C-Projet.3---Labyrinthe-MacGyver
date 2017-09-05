"""Class for the game"""


import pygame #peut être pas besoin

from pygame.locals import * 

from constantes import *

import random 

class Perso:
	""" This is the class used for both MacGyver and the BadGuy sprites"""
	def __init__(self, Image, level):
		self.Image = pygame.image.load(MacGyver).convert_alpha()
		"""self.Position = perso.get_rect()"""
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		self.level = level

	#Keyboard touch used to moove MacGyver:
	def mooving(self, direction):
		if direction == 'right':
			if self.case_x < (nombre_sprite_cote - 1):
				if self.level.structure[self.case_y][self.case_x+1] != 'm':
					self.case_x += 1
					self.x = self.case_x * taille_sprite

		if direction == 'left':
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite

		if direction == 'up':
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] !='m': 
					self.case_y -= 1
					self.y = self.case_y * taille_sprite

		if direction == 'down':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.level.structure[self.case_y+1][self.case_x] !='m':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
					print(self.x, self.y)

				"""if event.key == K_DOWN: 
					position_perso = position_perso.move(0,60) 
				if event.key == K_UP:
					position_perso = position_perso.move(0,-60)
				if event.key == K_LEFT:
					position_perso = position_perso.move(-60,0)
				if event.key == K_RIGHT:
					position_perso = position_perso.move(60,0)"""

class Level:
	"""class used for the maze"""
	def __init__(self, file):
		self.file = "Level.txt"
		self.structure = 0

	def generate(self):
		with open(self.file, "r") as file:
			level_structure = []

			for line in file:
				line_level = []
				for sprite in line:
					if sprite !='\n':
						line_level.append(sprite)
				level_structure.append(line_level)
			self.structure = level_structure



	def display(self, fenetre):
		wall = pygame.image.load('images/mur.png').convert()
		gardien = pygame.image.load(Gardien).convert_alpha()

		num_line = 0
		for line in self.structure:
			num_case = 0
			for sprite in line:
				x = num_case * taille_sprite
				y = num_line * taille_sprite
				if sprite == 'm':
					fenetre.blit(wall, (x,y))
				elif sprite == 'a':
					fenetre.blit(gardien, (x,y))
				num_case += 1
			num_line += 1


class loot: #the class for the items
	def __init__(self, image_objet, level):
		self.case_y = 0
		self.case_x = 0
		self.x = 0
		self.y = 0
		self.level = level
		self.loaded = True        
		self.image_objet = image_objet

	def display(self, image_objet, fenetre):
		while self.loaded :
			self.case_x = random.randint(0,14)
			self.case_y = random.randint(0,14)
			if self.level.structure[self.case_y][self.case_x] == '0':#l'inversement de self.case_x, self.case_y permet de faire ce que je veux !!! (l'inverse fais apparaitre les objets dans les murs. Youpi !)
				self.y = self.case_y * taille_sprite
				self.x = self.case_x * taille_sprite
				self.loaded = False
				print(self.x, self.y)


				"""if self.level.structure[self.case_x][self.case_y] != 'm':
				if self.level.structure[self.case_x][self.case_y] != 'a':
					if self.level.structure[self.case_x][self.case_y] != 'd':"""

