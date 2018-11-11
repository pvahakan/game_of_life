#!/usr/bin/env python3

import pygame
import numpy as np
import os
import time

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

def console_print(M):
    """
    Function to print game in console.
    """
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == 0 or j == 0:
                print("# ", end="")
            elif i == len(M) - 1 or j == len(M[0]) - 1:
                print("# ", end="")
            elif M[i][j] == 1:
                print("x ", end="")
            else:
                print("  ", end="")

        print()

def logic(M):
    """
    Game logic.
    """
    copy = M.copy()
    for i in range(1, len(y)-1):
        for j in range(1, len(x)-1):
            surroundings = look_around(M, i, j)

            if M[i][j] == 0:
                # unpopulated cells
                if surroundings == 3:
                    copy[i][j] = 1

            elif M[i][j] == 1:
                # populated cells
                if surroundings < 2 or surroundings > 3:
                    copy[i][j] = 0
                else:
                    copy[i][j] = 1

    return copy

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
    # board = np.array([[1,1,1],[2,2,2],[3,3,3]])
    i = 0
    board = test_init_board(board)
    # Glider
    # board[2][3] = 1
    # board[3][4] = 1
    # board[4][2] = 1
    # board[4][3] = 1
    # board[4][4] = 1
    # Small exploder
    # board[4][6] = 1
    # board[5][5] = 1
    # board[5][6] = 1
    # board[5][7] = 1
    # board[6][5] = 1
    # board[6][7] = 1
    # board[7][6] = 1
    while i < 10:
        os.system("clear")
        console_print(board)
        board = logic(board)
        i += 1
        time.sleep(0.5)
