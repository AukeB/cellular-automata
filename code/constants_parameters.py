from collections import namedtuple
import pygame as pg
import os, glob

 ### SURFACE SIZE ###

infoObject = pg.display.Info() # Obtain screen resolution
SURFACE_WIDTH = infoObject.current_w
SURFACE_HEIGHT = infoObject.current_h
if SURFACE_WIDTH > 1920: SURFACE_WIDTH = int(SURFACE_WIDTH / 2) # If two screens are attached.
BOUNDARY = 40

 ### GRID INITIALIZION ###

GRID_WIDTH = 100
GRID_HEIGHT = 100
DIM = (GRID_WIDTH, GRID_HEIGHT)
PPC = 5 # Pixels per cell.
ZOOM_FACTOR = 1.03

 ### COLOURS

FONT = 'fonts/8-bit-pusab.ttf'
FONT_SIZE = 24

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
GREEN = (0, 255, 0)

GAME_TITLE = 'Cellular Automata'
SURFACE_BACKGROUND_COLOR = GREY
GRID_BACKGROUND_COLOR = BLACK
GRID_COLOUR = WHITE



