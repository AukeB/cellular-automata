# Imports and initialisations.
import sys
import pygame as pg
import random as rd
import os

pg.mixer.pre_init(44100, -16, 1, 512) # Makes sure sound effects don't have lag.
pg.mixer.init()
pg.init()

# Import classes.
from code import constants_parameters as C
from code import menu

def main():
	menu.start_game()

if __name__ == '__main__':
	main()
	
