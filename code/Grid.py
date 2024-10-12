import pygame as pg
import random as rd
import itertools
from collections import namedtuple
from code import constants_parameters as C
import os
import numpy as np


class Grid(object):
	def __init__(self, dimensions, rect):
		self.dimensions = dimensions
		self.rect = rect
		#self.grid_matrix = np.zeros(shape=dimensions)
		self.matrix = np.random.randint(2, size=dimensions)

	def get_next_state(self, grid):
		nb_sum = 0
		nb_x_arr = [-1, 0, 1, -1, 1, -1, 0, 1]
		nb_y_arr = [-1, -1, -1, 0, 0, 1, 1, 1]

		virtual_grid = np.zeros(grid.dimensions)

		for i in range(1, len(grid.matrix)-1):
			for j in range(1, len(grid.matrix[i])-1):
				for k, l in zip(nb_x_arr, nb_y_arr):
					nb_sum += grid.matrix[i+k][j+l]
					#print(i,j,k,l,i+k,j+l,grid.matrix[i+k][j+l])
					#print(nb_sum)
				if grid.matrix[i][j] == True and (nb_sum == 2 or nb_sum == 3): virtual_grid[i][j] = 1
				if grid.matrix[i][j] == False and nb_sum == 3: virtual_grid[i][j] = 1

				nb_sum = 0

		grid.matrix = virtual_grid

	def __iter__(self):
		return itertools.product(range(self.dimensions.width),
			range(self.dimensions.height))