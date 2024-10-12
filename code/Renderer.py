import pygame as pg
from code import constants_parameters as C

class Renderer(object):
	def __init__(self, width, height, background_color, surface):
		self.width = width # Set display width.
		self.height = height # Set display height.
		self.background_color = background_color # Set background color.
		self.display_surface = surface
		self.surface = pg.display.get_surface() # Obtain surface object.
		self.pixel_scale = C.PPC
		self.font = pg.font.Font(C.FONT, C.FONT_SIZE)

	def draw_grid(self, grid, grid_colour):
		pg.draw.rect(self.surface, C.GRID_BACKGROUND_COLOR, grid.rect)
		for i in range(len(grid.matrix)):
			for j in range(len(grid.matrix[i])):
				cur_cell_rect = (grid.rect[0] + self.pixel_scale*j, grid.rect[1] + self.pixel_scale*i, self.pixel_scale, self.pixel_scale)
				if grid.matrix[i][j]:
					if cur_cell_rect[0] < grid.rect[0] + grid.rect[2] - cur_cell_rect[2] and cur_cell_rect[1] < grid.rect[1] + grid.rect[3] - cur_cell_rect[3]:
						pg.draw.rect(self.surface, grid_colour, cur_cell_rect)

	def draw_changing_text(self, text, pos, color, background_color):
		text = self.font.render(text, True, color, background_color) 
		textRect = text.get_rect()
		textRect.center = pos
		self.display_surface.blit(text, textRect)


		#pg.draw.rect(self.surface, grid_colour, grid.rect)

	def __enter__(self):
		self.surface.fill(self.background_color) # Fill the surface with a background color.

	def __exit__(self, exc_type, exc_value, exc_trace):
		pg.display.update()

