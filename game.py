#!/usr/bin/env python3

import pygame
import numpy as np
import os
import time
from life import Life

display_width = 800
display_height = 600

cell_size = 20 # Color block size

# Calculating number of color boxes
x = np.linspace(0, display_width, display_width/cell_size)
y = np.linspace(0, display_height, display_height/cell_size)

# Columns and rows opposite to the (x,y) notation
board = np.zeros((len(y), len(x)))

# Colors
green = (0, 255, 0)
white = (255, 255, 255)

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


if __name__ == "__main__":
    g = Life(20, 20)
    g.glider_init()
    # g.small_exploder_init()
    nIter = 0
    while nIter < 20:
        os.system("clear")
        g.console_print()
        g.logic()
        time.sleep(0.2)
        nIter += 1

