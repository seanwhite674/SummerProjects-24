# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:13:28 2024

@author: seanw
"""

import pygame
import math
import numpy as np

pygame.init()
WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Planet Simulation")
WHITE = (200,200,200)

def main():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        WIN.fill(WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()    

main()