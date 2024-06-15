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
WHITE = (255,255,255)
YELLOW = (255,255,0)    


class Planet:
        
    AU  =  1.49597e6*1000
    G = 6.6743e-11
    SCALE  =  250 / AU    #1AU = 100  pixels
    Timestep  = 60*60*24  # 1 day
    
    
    
    def __init__(self, x,y ,radius ,color     ,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.orbit = []
        self.sun =  False
        self.distance_to_sun = 0
        
        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color, (x,y),  self.radius)

def main():
    run = True
    clock = pygame.time.Clock()
    
    sun = Planet(0, 0, 20, YELLOW, 1.989e30)    
    sun.sun =  True
    
    planets = [sun]
    
    while run:
        clock.tick(60)
       # WIN.fill(WHITE)
       # pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        for planet in planets:
            planet.draw(WIN)
        
        pygame.display.update()
            
    pygame.quit()

    
main()