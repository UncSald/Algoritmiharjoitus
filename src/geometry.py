import pygame
import pygame.gfxdraw
from math import sqrt, acos, sin




class Triangle:
    """Triangle data type which is used to correctly create a delaunay triangulation.
    """
    def __init__(self, a:tuple[int,int], b:tuple[int,int], c:tuple[int,int]):
        """Class constructor holding all information of a triangle.

        Args:
            a (tuple[int,int]): Triangle corner a
            b (tuple[int,int]): Triangle corner b
            c (tuple[int,int]): Triangle corner c
        """

        self._a_edge = (a,b)
        self._b_edge = (a,c)
        self._c_edge = (b,c)
        self._a_point = a
        self._b_point = b
        self._c_point = c
        self.edges = [self._a_edge,
                        self._b_edge,
                        self._c_edge]
        self.points = [a,b,c]

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
        """Calculates the exact lenght between points in the edge.

        Args:
            edge (tuple[tuple,tuple]): Edge between two points.

        Returns:
            float: Distance between the two points.
        """
        return sqrt(abs(edge[0][0]-edge[1][0])**2\
                + (abs(edge[0][1]-edge[1][1]))**2)

    def triangle_angle(self,a,b,c):
        """Using the lenghts of the triangles edges, calculates the angles of the triangle.

        Args:
            a (float): Lenght of the edge facing the angle.
            b (float): Lenght of the edge next to the angle
            c (float): Lenght of the other edge next to the angle

        Returns:
            float: The angle in radians.
        """
        try:
            statement = (a**2+b**2-c**2)/(2*a*b)
            if statement > 1:
                statement = 1
            elif statement < -1:
                statement = -1
            return acos(statement)
        except ZeroDivisionError:
            print(self.points)

    def count_radius(self):
        """Method counts the radius of the circumcircle.

        Returns:
            float: The radius of the circumcircle.
        """
        return  (self.a_edge_len*self.b_edge_len*self.c_edge_len)/\
                sqrt(max((self.a_edge_len+self.b_edge_len+self.c_edge_len)*\
                (self.b_edge_len+self.c_edge_len-self.a_edge_len)*\
                (self.c_edge_len+self.a_edge_len-self.b_edge_len)*\
                (self.a_edge_len+self.b_edge_len-self.c_edge_len),1)
                )

    def check_point(self, point):
        """Check if a point is inside the circumcircle of the triangle.

        Args:
            point (tuple[int,int]): Point to be checked.

        Returns:
            bool: True if in circumcircle, False if not.
        """
        xLocation = abs(max(self.circumcenter[0],point[0])-\
                        min(self.circumcenter[0],point[0]))**2
        yLocation = abs(max(self.circumcenter[1],point[1])-\
                        min(self.circumcenter[1],point[1]))**2
        d = sqrt(xLocation + yLocation)
        return round(d,4)<=round(self.radius,4)


    def draw(self, screen, color, val):
        """Method which draws triangle on pygame display.

        Args:
            screen (pygame.surfac.surface): Screen to be drawn on.
            color (tuple[float,float,float]): Color for the triangle drawn.
            val (int): 0 - draw only triangle, 1 - draw triangle and circumcenter.
        """
        for edge in self.edges:
            pygame.draw.aaline(screen, color, edge[0], edge[1])
            if val == 1:
                pygame.draw.circle(screen,'yellow', self.circumcenter, self.radius, 1)



class Rectangle:
    """A rectangle data type used for creating rooms in roomGeneration.py.
    """
    def __init__(self, x0 :tuple[int,int], width :int, height :int):
        """Class constructor for a rectangle.

        Args:
            x0 (tuple[int,int]): Top left point of rectangle.
            width (int): Width of rectagle.
            height (int): Height of rectangle.
        """
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
        """Method to check wether two rectangles collide with eachother.

        Args:
            other (Rectangle): Rectangle which may or may not collide.

        Returns:
            bool: True if collides, False if there is no collision.
        """
        left_clip = other.left <= self.left <= other.right
        right_clip = other.left <= self.right <= other.right
        up_clip = other.up <= self.up <= other.down
        down_clip = other.up <= self.down <= other.down

        lleft_clip = self.left <= other.left <= self.right
        lright_clip = self.left <= other.right <= self.right
        lup_clip = self.up <= other.up <= self.down
        ldown_clip = self.up <= other.down <= self.down

        if up_clip and down_clip and lright_clip and lleft_clip:
            return True
        if lup_clip and ldown_clip and right_clip and left_clip:
            return True
        if left_clip and up_clip:
            return True
        if left_clip and down_clip:
            return True
        if right_clip and up_clip:
            return True
        if right_clip and down_clip:
            return True
        if lleft_clip and lup_clip:
            return True
        if lleft_clip and ldown_clip:
            return True
        if lright_clip and lup_clip:
            return True
        if lright_clip and ldown_clip:
            return True
        return False

    def draw(self, screen, color):
        """Method to draw the rectangle on a pygame screen.

        Args:
            screen (pygame.surface.Surface): A pygame screen to be drawn on.
            color (tuple[float,float,float]): A color for the rectangle drawn.
        """
        pygame.draw.rect(screen, color, [self.zero[0],self.zero[1],self.width,self.height])
