import pygame as pg
from code import Grid
from code import Renderer
from collections import namedtuple
from code import constants_parameters as C
import numpy as np
import sys
import random as rd
import copy


class Game(object):
	def __init__(self, surface):
		self.renderer = Renderer.Renderer(C.SURFACE_WIDTH, C.SURFACE_HEIGHT, C.SURFACE_BACKGROUND_COLOR, surface)
		self.grid = Grid.Grid(C.DIM, pg.Rect(C.BOUNDARY, C.BOUNDARY, 3/4 * C.SURFACE_WIDTH, C.SURFACE_HEIGHT - 2*C.BOUNDARY))
		self.generation_counter = 0


	def update(self):
		with self.renderer:
			self.renderer.draw_grid(self.grid, C.GRID_COLOUR)
			self.renderer.draw_changing_text(f'Generation {self.generation_counter}', (7/8 * C.SURFACE_WIDTH, 1.5*C.BOUNDARY), C.WHITE, C.SURFACE_BACKGROUND_COLOR)

		self.grid.get_next_state(self.grid)
		self.generation_counter += 1

		return self.handle_events()

	def handle_events(self):
		for ev in pg.event.get():
			if ev.type == pg.QUIT or ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE:
				return False
			elif ev.type == pg.MOUSEBUTTONDOWN or ev.type == pg.MOUSEBUTTONUP:
				if ev.button == 4:
					self.renderer.pixel_scale *= C.ZOOM_FACTOR
				if ev.button == 5:
					self.renderer.pixel_scale /= C.ZOOM_FACTOR

		return True