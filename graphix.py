import pygame

class Graphix:
    """
    Class to draw graphix of game of life.
    """
    def __init__(self, width, height):
        # Init everything in PyGame
        pygame.init()

        # Create window and clock
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Graphics window")
        self.window_width = width
        self.window_height = height

        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.white = (255, 255, 255)

    def draw_array(self, display, array, cell_size):
        """
        Function to draw occupied cells in array.
        :param display:     PyGame display, figure will be drawn in this.
        :param array:       Numpy array, array of cells. 
                            Cell value of 1 means occupied and 0 unoccupied
        :param cell_size:   tuple, the size of cell to be drawn.
        """
        x, y = 0, 0

        # Find occupied cells
        for i in range(len(array)):
            x = 0
            for j in range(len(array[0])):
                if array[i][j] == 1:
                    pygame.draw.rect(
                            self.display, self.green, 
                            [x, y, cell_size[0], cell_size[1]]
                            )
                x += cell_size[0]
            y += cell_size[1]

        pygame.display.update()
