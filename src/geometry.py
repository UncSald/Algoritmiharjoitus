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
        self._edges = [a_edge,
                        b_edge,
                        c_edge]
        self._poins = [a_edge[0],
                       a_edge[1],
                       b_edge[1]]
    
        # TO CALCULATE THE CIRCUMCIRCLE OF THE TRIANGLE WE NEED THE
        # LENGHTS OF THE TRIANGLES SIDES AND THE SIZES OF EACH ANGLE

        self.a_edge_len = self.edge_length(self._a_edge)
        self.b_edge_len = self.edge_length(self._b_edge)
        self.c_edge_len = self.edge_length(self._c_edge)

        self.a_angle = self.triangle_angle(self.a_edge_len, self.b_edge_len, self.c_edge_len)
        self.b_angle = self.triangle_angle(self.a_edge_len, self.c_edge_len, self.b_edge_len)
        self.c_angle = self.triangle_angle(self.b_edge_len, self.c_edge_len, self.a_edge_len)

        # CALCULATE THE CIRCUMCENTER AND RADIUS OF THE CIRCLE

        self.circumcenter = (((self._a_point[0]*sin(2*self.a_angle))+\
                            (self._b_point[0]*sin(2*self.b_angle))+\
                            (self._c_point[0]*sin(2*self.c_angle)))/\
                            ((sin(2*self.a_angle))+sin(2*self.b_angle)+sin(2*self.c_angle)),
                            ((self._a_point[1]*sin(2*self.a_angle))+\
                            (self._b_point[1]*sin(2*self.b_angle))+\
                            (self._c_point[1]*sin(2*self.c_angle)))/\
                            ((sin(2*self.a_angle))+sin(2*self.b_angle)+sin(2*self.c_angle))
                            )
    
    def edge_length(self,edge):
        print(((max(edge[0][0],edge[1][0])-min(edge[0][0],edge[1][0]))**2\
                + (max(edge[0][1],edge[1][1])-min(edge[0][1],edge[1][1]))**2))
        return sqrt((max(edge[0][0],edge[1][0])-min(edge[0][0],edge[1][0]))**2\
                + (max(edge[0][1],edge[1][1])-min(edge[0][1],edge[1][1]))**2)

    def triangle_angle(self,a,b,c):
        return (acos((a**2+b**2-c**2)/(2*a*b)))
    



class Box:
    def __init__(self):
        pass


