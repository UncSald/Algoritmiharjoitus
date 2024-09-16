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
        self._points = [a_edge[0],
                       a_edge[1],
                       b_edge[1]]
    
        # TO CALCULATE THE CIRCUMCIRCLE OF THE TRIANGLE WE NEED THE
        # LENGHTS OF THE TRIANGLES SIDES AND THE SIZES OF EACH ANGLE

        self.a_edge_len = self.edge_length(self._a_edge)
        self.b_edge_len = self.edge_length(self._b_edge)
        self.c_edge_len = self.edge_length(self._c_edge)

        self.a_angle = self.triangle_angle(self.a_edge_len,
                                           self.b_edge_len,
                                           self.c_edge_len)
        self.b_angle = self.triangle_angle(self.a_edge_len,
                                           self.c_edge_len,
                                           self.b_edge_len)
        self.c_angle = self.triangle_angle(self.b_edge_len,
                                           self.c_edge_len,
                                           self.a_edge_len)

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

        self.radius = self.count_radius()
    
    def edge_length(self,edge):
        return sqrt((max(edge[0][0],edge[1][0])-min(edge[0][0],edge[1][0]))**2\
                + (max(edge[0][1],edge[1][1])-min(edge[0][1],edge[1][1]))**2)

    
    def triangle_angle(self,a,b,c):
        return (acos((a**2+b**2-c**2)/(2*a*b)))
    
    def count_radius(self):
        if self.a_edge_len == self.b_edge_len or\
            self.a_edge_len == self.c_edge_len or\
            self.b_edge_len == self.c_edge_len:
            return max(self.a_edge_len, self.b_edge_len, self.c_edge_len)/2
        return  (self.a_edge_len*self.b_edge_len*self.c_edge_len)/\
                sqrt((self.a_edge_len+self.b_edge_len+self.c_edge_len)*\
                (self.b_edge_len+self.c_edge_len-self.a_edge_len)*\
                (self.c_edge_len+self.a_edge_len-self.b_edge_len)*\
                (self.a_edge_len+self.b_edge_len-self.c_edge_len)
                )

    def check_point(self, point):
        xLocation = abs(max(self.circumcenter[0],point[0])-\
                        min(self.circumcenter[0],point[0]))**2
        yLocation = abs(max(self.circumcenter[1],point[1])-\
                        min(self.circumcenter[1],point[1]))**2
        d = sqrt(xLocation + yLocation)
        return d<self.radius

    def draw(self, screen, color):
        for edge in self._edges:
            pygame.draw.aaline(screen, color, edge[0], edge[1])




class Rectangle:
    def __init__(self, x0, width, height):
        self.up = x0[1]
        self.down = x0[1]+height
        self.left = x0[0]
        self.right = x0[0]+width
        self.width = width
        self.height = height
        self.center = (self.right-(self.right-self.left)/2,\
                        self.down-(self.down-self.up)/2)
        self.edges = [[x0,(x0[0]+width,x0[1])],
                       [x0,(x0[0],x0[1]+height)],
                       [(x0[0]+width,x0[1]),(x0[0]+width,x0[1]+height)],
                       [(x0[0],x0[1]+height),(x0[0]+width,x0[1]+height)]]

    def collision(self, other):
        leftClip = other.left <= self.left <= other.right
        rightClip = other.left <= self.right <= other.right
        upClip = other.up <= self.up <= other.down
        downClip = other.up <= self.down <= other.down

        lleftClip = self.left <= other.left <= self.right
        lrightClip = self.left <= other.right <= self.right
        lupClip = self.up <= other.up <= self.down
        ldownClip = self.up <= other.down <= self.down

        if upClip and downClip and lrightClip and lleftClip:
            return True
        if lupClip and ldownClip and rightClip and leftClip:
            return True
        if leftClip and upClip:
            return True
        if leftClip and downClip:
            return True
        if rightClip and upClip:
            return True
        if rightClip and downClip:
            return True
        if lleftClip and lupClip:
            return True
        if lleftClip and ldownClip:
            return True
        if lrightClip and lupClip:
            return True
        if lrightClip and ldownClip:
            return True
        return False
    
    def __repr__(self) -> str:
        return f"{self.up}, {self.down}, {self.left}, {self.down}"

    def draw(self, screen, color):
        for edge in self.edges:
            pygame.draw.aaline(screen, color, edge[0], edge[1])
