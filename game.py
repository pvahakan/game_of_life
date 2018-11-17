#!/usr/bin/env python3

import pygame
import numpy as np
import os
import time
from life import Life
from graphix import Graphix

if __name__ == "__main__":

    # Window parameters
    window_width = 600
    window_height = 600

    # Create objects
    game = Life(60, 60)
    gpx = Graphix(window_width, window_height)

    game.random_init()

    # Calculating cell size to draw
    cell_x = gpx.window_width / len(game.board[0])
    cell_y = gpx.window_height / len(game.board)

    # Game loop
    i = 0
    while i < 100:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        gpx.draw_array(gpx.display, game.board, (cell_x, cell_y))
        game.logic()
        gpx.clock.tick(20)
        gpx.display.fill(gpx.white)
        i += 1

    pygame.quit()
