"""Class for the game"""


import pygame  # needed ?

from pygame.locals import *

from constantes import *

import random


class Char:

    """ This is the class used for MacGyver sprite"""
    def __init__(self, Image, level):
        self.Image = pygame.image.load(MacGyver).convert_alpha()
        """self.Position = Char.get_rect()"""
        self.case_x = 0
        self.case_y = 1  # Starting from 1 instead of 0 so the character effectively move down the first time DOWN_KEY is pressed.
        self.x = 0
        self.y = 30  # Initial position of character is set bellow the upper black margin.
        self.level = level

    # Keyboard touch used to moove MacGyver:
    def mooving(self, direction):
        if direction == 'right':
            if self.case_x < (Nbr_Sprite_Side - 1):  # Character can't go off screen
                if self.level.structure[self.case_y][self.case_x + 1] != 'm':  # He can't pass trough walls etheir ! (he's MacGyver, not a ghost)
                    self.case_x += 1
                    self.x = self.case_x * Sprite_Size
                    print(self.x, self.y)


        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * Sprite_Size
                    print(self.x, self.y)

        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    if self.level.structure[self.case_y - 1][self.case_x] != 'c':
                        self.case_y -= 1
                        self.y = self.case_y * Sprite_Size
                        print(self.x, self.y)

        if direction == 'down':
            if self.case_y < (Nbr_Sprite_Side):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * Sprite_Size
                    print(self.x, self.y)


class Level:
    """class used for the maze"""
    def __init__(self, file):
        self.file = "Level.txt"
        self.structure = 0

    def generate(self):
        with open(self.file, "r") as file: # Opening Level.txt as only readable
            level_structure = [] # defining level structure as an empty list

            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite) # We had each sprite to the line level_level list, except for \n
                level_structure.append(line_level) # We append the line_level list to the level_structure_list
            self.structure = level_structure # we re-define the structure

    def display(self, Window):
        wall = pygame.image.load('images/wall.png').convert()
        badguy = pygame.image.load(BadGuy).convert_alpha()

        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:  # We check for each sprite in line
                x = num_case * Sprite_Size  # each sprites position is calculated
                y = num_line * Sprite_Size
                if sprite == 'm':  # m = wall
                    Window.blit(wall, (x, y))  # We blit the wall-img to the position on the case
                elif sprite == 'a':  # a = BadGuy (exit)
                    Window.blit(badguy, (x, y))  # We blit the badguy-img
                num_case += 1  # once done with a sprite, we follow with the next entry
            num_line += 1  # once done with a line, we follow with the next


class loot:  # the class for the items
    def __init__(self, Loot_Image, level):
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 0
        self.level = level
        self.loaded = True
        self.Loot_Image = Loot_Image

    def display(self, Loot_Image, Window):
        while self.loaded:
            self.case_x = random.randint(0, 14)  # We randomize the case_x position
            self.case_y = random.randint(0, 14)  # same for case_y position
            if self.level.structure[self.case_y][self.case_x] == '0': # if the randomized position is located on a free space
                self.y = self.case_y * Sprite_Size  # We define/accept the position for the object
                self.x = self.case_x * Sprite_Size
                self.loaded = False  # Once we have defined a position for one object, the script is over
