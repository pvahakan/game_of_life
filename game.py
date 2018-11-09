#!/usr/bin/env python3

import pygame

if __name__ == "__main__":

    # Initialize
    pygame.init()

    # Create window
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Conway's game of life")

    clock = pygame.time.Clock()

    crashed = False

    # Game loop
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            print(event)
        pygame.display.update()
        clock.tick(40) # FPS

    pygame.quit()
    quit()
