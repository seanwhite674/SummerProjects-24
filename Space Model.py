# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:13:28 2024

@author: seanw
"""

import pygame
import numpy as np
import math

pygame.init()


WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Planet Simulation")
WHITE = (255,255,255)
YELLOW1 = (255,255,0)   
BLUE =  (128,166,206) 
RED = (180,21,0)
GREY = (169,169,169)
YELLOW = (252,244,163)

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
        pygame.draw.circle(win, self.color, (x, y), self.radius)
    def attraction(self,other):
        other_x , other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2+distance_y**2)
            
        if other.sun:
            self.distance_to_sun = distance
        
        force = (self.G*self.mass*other.mass)/(distance**2)
        theta = math.atan(distance_y/distance_x)
        force_x = math.cos(theta)*force
        force_y = math.sin(theta)*force
        
        return force_x,force_y
        
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            
            fx,fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
    
        self.x_vel +=  total_fx/self.mass * self.Timestep
        self.y_vel +=  total_fy/self.mass * self.Timestep
        
        self.x += self.x_vel * self.Timestep
        self.y += self.y_vel * self.Timestep
            
        self.orbit.append((self.x,self.y))
            

def main():
    run = True
    clock = pygame.time.Clock()
    
    sun = Planet(0, 0, 30, YELLOW1, 1.989*10**30)    
    sun.sun =  True
    
    earth = Planet(-1*Planet.AU, 0, 16, BLUE, 5.972*10**24)
    earth.y_vel = 29.783 * 1000
    
    mars = Planet(-1.5*Planet.AU, 0, 12, RED, 6.39*10**23)
    mars.y_vel = 24.077 * 1000
    
    mercury = Planet(0.387*Planet.AU,0,8,GREY,3.285*10**23)
    mercury.y_vel = -24.077*1000
    
    venus = Planet(0.75*Planet.AU, 0, 14, YELLOW, 4.867*10**24)
    venus.y_vel = -35.02 * 1000
    
    planets = [sun,earth,mars,mercury,venus]
    
    while run:
        clock.tick(60)
        WIN.fill((0,0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
                
        pygame.display.update()
            
    pygame.quit()
    
main()

