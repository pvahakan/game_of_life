#!/usr/bin/env python3

import pygame
import numpy as np

display_width = 800
display_height = 600

x_block = 10
y_block = 10
a_block = 50 # Color block size

# Calculating number of color boxes
x = np.linspace(0, display_width, display_width/a_block)
y = np.linspace(0, display_height, display_height/a_block)

# Columns and rows opposite to the (x,y) notation
board = np.zeros((len(y), len(x)))

# Colors
green = (0, 255, 0)
white = (255, 255, 255)

def test_init_board(M):
    """
    Create random matrix of 0 and 1
    """
    M = np.random.randint(2, size=(len(y), len(x)))
    return M

def look_around(M, i, j):
    """
    Calculates the sum of matrix values around M[i][j]
    """
    sum = (
        M[i-1][j-1] + M[i][j-1] + M[i+1][j-1] + 
        M[i-1][j] + M[i+1][j] + 
        M[i-1][j+1] + M[i][j+1] + M[i+1][j+1]
        )
    return sum

def logic(M):
    for i in range(1, len(y)-1):
        for j in range(1, len(x)-1):
            print(look_around(M, i, j))

def main():
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
        pygame.draw.rect(gameDisplay, green, [xi, xi, a_block, a_block])
        
    pygame.display.update()
    clock.tick(40) # FPS

    pygame.quit()
    quit()


if __name__ == "__main__":
    board = test_init_board(board)
    print(board)
    logic(board)
