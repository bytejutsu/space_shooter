from random import randint

import pygame
from os.path import join

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True

# plain surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

# importing an image
player_surf = pygame.image.load(join('..', 'images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('..', 'images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(40)]

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('darkgray')

    for position in star_positions:
        display_surface.blit(star_surf, (position[0], position[1]))

    x += 0.1
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()

pygame.quit()
