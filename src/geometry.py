import pygame
import pygame.gfxdraw
from math import sqrt, acos, sin




class Triangle:
    def __init__(self, a_edge, b_edge, c_edge):
        self._a_edge = a_edge
        self._b_edge = b_edge
        self._c_edge = c_edge
        self._a_point = a_edge[0] 
        self._b_point = a_edge[1]
        self._c_point = b_edge[1]
        self._edges = [a_edge
                      ,b_edge,
                      c_edge]
        self._poins = [a_edge[0], a_edge[1], b_edge[1]]




class Box:
    def __init__(self):
        pass
