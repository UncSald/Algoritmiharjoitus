from random import randint
from geometry import Rectangle

# FUNCTION WHICH GENERATES RECTANGLES WHEN GIVEN
# THE MAX AMOUNT OF RECTANGLES CREATED AND THE SIZE
# OF THE SIZE OF THE AREA WHERE RECTANGLES WILL BE DRAWN
# ON. RETURNS A SET OF RECTANGLES AND A SET OF THEIR 
# CENTER POINTS.

def generate_rooms(how_many, width, height):
    rect_set = set()
    point_set = set()

    while len(rect_set) <= how_many:
        x_point = randint(1, ((width-(width%32))//32))*32
        y_point = randint(1, ((height-(height%32))//32))*32
        max_width = int((width-x_point)//32)
        max_height = int((height-y_point)//32)
        if max_width < 3 or max_height < 4:
            continue
        if max_width > 7:
            max_width = 7
        if max_height > 7:
            max_height = 7
        rect_width = int(randint(2, max_width)*32)
        rect_height = int(randint(3, max_height)*32)
        new_rect = Rectangle((x_point,y_point), rect_width, rect_height)
        collision = False
        for rect in rect_set:
            if rect.collision(new_rect):
                collision = True
        if not collision:
            rect_set.add(new_rect)
            point_set.add(new_rect.center)

    return (rect_set, point_set)




def start_end(points :set):
    i = 0
    start = (0,0)
    end = (0,0)
    for point in points:
        if i == 1:
            start = point
        if i == len(points)-2:
            end  = point
        i += 1
    return start, end