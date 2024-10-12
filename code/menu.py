# Imports.
import pygame as pg
#from pygame.locals import *
import os, sys
import copy
import random as rd
import numpy as np

from code import Game
from code import Renderer
from code import Grid
from code import constants_parameters as C

 # Global variables.

pg.display.set_caption(C.GAME_TITLE) # Give the game a title.
display = pg.display.set_mode((C.SURFACE_WIDTH, C.SURFACE_HEIGHT), pg.FULLSCREEN)
#display = pg.display.set_mode((1920, 1080))


def start_game():
	g = Game.Game(display) # Initialize game object.
	while g.update():
		pass

def main_menu():
	while True:
		start_game()

		pg.display.update()
		#main_clock.tick(60)