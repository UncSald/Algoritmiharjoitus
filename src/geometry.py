import pygame
import pygame.gfxdraw
from math import sqrt, acos, sin




class Triangle:
    def __init__(self, a, b, c):
        self._a_edge = (a,b)
        self._b_edge = (a,c)
        self._c_edge = (b,c)
        self._a_point = a
        self._b_point = b
        self._c_point = c
        self._edges = [self._a_edge,
                        self._b_edge,
                        self._c_edge]
        self._points = [a,b,c]
    
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
        return sqrt(abs(edge[0][0]-edge[1][0])**2\
                + (abs(edge[0][1]-edge[1][1]))**2)

    
    def triangle_angle(self,a,b,c):
        try:
            statement = (a**2+b**2-c**2)/(2*a*b)
            if statement > 1:
                statement = 1
            elif statement < -1:
                statement = -1
            return acos(statement)
        except ZeroDivisionError: print(self._points)
    
    def count_radius(self):
        return  (self.a_edge_len*self.b_edge_len*self.c_edge_len)/\
                sqrt(max((self.a_edge_len+self.b_edge_len+self.c_edge_len)*\
                (self.b_edge_len+self.c_edge_len-self.a_edge_len)*\
                (self.c_edge_len+self.a_edge_len-self.b_edge_len)*\
                (self.a_edge_len+self.b_edge_len-self.c_edge_len),1)
                )
    def check_point(self, point):
        xLocation = abs(max(self.circumcenter[0],point[0])-\
                        min(self.circumcenter[0],point[0]))**2
        yLocation = abs(max(self.circumcenter[1],point[1])-\
                        min(self.circumcenter[1],point[1]))**2
        d = sqrt(xLocation + yLocation)
        return round(d,4)<=round(self.radius,4)


    def draw(self, screen, color):
        for edge in self._edges:
            pygame.draw.aaline(screen, color, edge[0], edge[1])
        pygame.draw.circle(screen,'blue', self.circumcenter, self.radius, 1)



class Rectangle:
    def __init__(self, x0 :tuple[int,int], width :int, height :int):
        self.up = x0[1]
        self.down = x0[1]+height
        self.left = x0[0]
        self.right = x0[0]+width
        self.zero = x0
        self.width = width
        self.height = height
        self.center = (self.left+width/2,\
                        self.up+height/2)
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
            pygame.draw.rect(screen, color, [self.zero[0],self.zero[1],self.width,self.height])
