#!/usr/bin/env python3

import pygame
import numpy as np
import os
import time
from life import Life

# display_width = 800
# display_height = 600
# 
# cell_size = 20 # Color block size
# 
# # Calculating number of color boxes
# x = np.linspace(0, display_width, display_width/cell_size)
# y = np.linspace(0, display_height, display_height/cell_size)
# 
# # Columns and rows opposite to the (x,y) notation
# board = np.zeros((len(y), len(x)))
# 
# # Colors
# green = (0, 255, 0)
# white = (255, 255, 255)

def graphix():
    # Initialize
    pygame.init()

    # Create window
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Conway's game of life")

    clock = pygame.time.Clock()

    crashed = False

    # Game loop
    # while not crashed:
    gameDisplay.fill(white)

    for xi in x:
        pygame.draw.rect(gameDisplay, green, [xi, xi, cell_size, cell_size])
        
    pygame.display.update()
    clock.tick(40) # FPS

    pygame.quit()
    quit()

def init_window(width, height):
    """
    Initializes the PyGame window
    :return display:    PyGame display object.
    :return clock:      PyGame clock object.
    """
    pygame.init()
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Graphics window")
    clock = pygame.time.Clock()
    display.fill(white)

    return display, clock



def draw_array(display, array, cell_size):
    """
    Function to draw occupied cells in array.
    :param display:     PyGame display, figure will be drawn in this.
    :param array:       Numpy array, array of cells. 
                        Cell value of 1 means occupied and 0 unoccupied
    :param cell_size:   tuple, the size of cell to be drawn.
    """
    x, y = 0, 0

    # Find occupied cells
    for i in range(array_width):
        x = 0
        for j in range(array_height):
            if array[i][j] == 1:
                pygame.draw.rect(
                        display, green, [x, y, cell_size[0], cell_size[1]]
                        )
            x += cell_size[0]
        y += cell_size[1]

    pygame.display.update()

if __name__ == "__main__":
    # g = Life(20, 20)
    # g.glider_init()
    # g.small_exploder_init()

    # Window parameters
    window_width = 600
    window_height = 600

    # Color definitions
    white = (255, 255, 255)
    green = (0, 255, 0)

    # Create array to be plotted
    array_width, array_height = 60, 60
    array = np.random.randint(2, size=(array_width, array_height))

    # Calculating cell size
    cell_x = window_width / len(array[0])
    cell_y = window_height / len(array)

    # Init and show
    display, clock = init_window(window_width, window_height)
    draw_array(display, array, (cell_x, cell_y))

    print(array)
    time.sleep(9)
    pygame.quit()
