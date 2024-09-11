import pygame
import pygame.gfxdraw
from math import sqrt, acos, sin




class Triangle:
    def __init__(self, a, b, c):
        self.pointA = a
        self.pointB = b
        self.pointC = c
        self.edges = [[a,b],[a,c],[b,c]]




class Box:
    def __init__(self):
        pass
