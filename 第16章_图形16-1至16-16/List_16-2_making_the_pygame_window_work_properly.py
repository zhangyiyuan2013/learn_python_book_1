# Copyright Zhang Yiyuan,2023
# Released under MIT license    https://opensource.org/licenses/mit-license.php
# ------------


import pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
