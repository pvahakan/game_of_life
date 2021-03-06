#!/usr/bin/env python3

import numpy as np
import random

class Life():
    def __init__(self, x, y):
        # Board creation
        self.board = np.zeros((x, y))
        self.x = x
        self.y = y
        print("\nBoard created\n")

    def random_init(self):
        """
        Create random initialization of board.
        """
        self.board = np.random.randint(2, size=(self.x, self.y))
        
    def glider_init(self):
        """
        Initializes board to glider
        """
        self.board[2][3] = 1
        self.board[3][4] = 1
        self.board[4][2] = 1
        self.board[4][3] = 1
        self.board[4][4] = 1

    def small_exploder_init(self):
        """
        Initializes board to small exploder
        """
        cent_x = int(len(self.board) / 2)
        cent_y = int(len(self.board[0]) / 2)
        self.board[cent_x, cent_y - 1] = 1
        self.board[cent_x - 1, cent_y] = 1
        self.board[cent_x, cent_y] = 1
        self.board[cent_x + 1, cent_y] = 1
        self.board[cent_x - 1, cent_y + 1] = 1
        self.board[cent_x + 1, cent_y + 1] = 1
        self.board[cent_x, cent_y + 2] = 1

    def look_around(self, i, j):
        """
        Calculates the sum of matrix cell values around M[i][j]
        """
        sum = (
        self.board[i-1][j-1] + self.board[i][j-1] + self.board[i+1][j-1] +
        self.board[i-1][j] + self.board[i+1][j] +
        self.board[i-1][j+1] + self.board[i][j+1] + self.board[i+1][j+1] 
        )
        return sum

    def console_print(self):
        """
        Function to print game in console
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if i == 0 or j == 0:
                    print("# ", end="")
                elif i == len(self.board)-1 or j == len(self.board[0])-1:
                    print("# ", end="")
                elif self.board[i][j] == 1:
                    print("x ", end="")
                else:
                    print("  ", end="")

            print()


    def logic(self):
        """
        Game logic.
        """
        copy = self.board.copy()
        for i in range(1, self.y-1):
            for j in range(1, self.x-1):
                surroundings = Life.look_around(self, i, j)

                if self.board[i][j] == 0:
                    # unpopulated cells
                    if surroundings == 3:
                        copy[i][j] = 1

                elif self.board[i][j] == 1:
                    # populated cells
                    if surroundings < 2 or surroundings > 3:
                        copy[i][j] = 0
                    else:
                        copy[i][j] = 1

        self.board = copy
