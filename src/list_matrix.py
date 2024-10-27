"""Module contains matrix manipulation tools.
Others for creating a new matrix, others for manipulating the data
inside a re-existing matrix.
"""
from src.geometry import Rectangle

def list_to_matrix(rooms :list, width :int,height :int,\
                    start :tuple[int,int], end:tuple[int,int], tile_size :int):
    """Creates a matrix from a given list of rooms, a start point, and the end point.

    Args:
        rooms (list): A list of Rectangle class objects.
        width (int): Width divided by tilesize of the draw area will be width of the matrix.
        height (int): Height divided by tilesize of the draw area will be width of the matrix.
        start (tuple[int,int]): Start point location.
        end (tuple[int,int]): Goal int location.
        tile_size (int): Size of a single value in the matrix.

    Returns:
        list[list[int]]: Created matrix is returned.
    """
    matrix = []
    for _ in range((height-height%tile_size)//tile_size):
        matrix.append([])
    for row in matrix:
        for _ in range((width-width%tile_size)//tile_size):
            row.append(0)
    for room in rooms:
        for point in rect_to_coord(room, tile_size):
            x,y = point
            matrix[y][x] = 1
    sx,sy = point_to_coord(start,tile_size)
    matrix[sy][sx] = 3
    ex, ey = point_to_coord(end,tile_size)
    matrix[ey][ex] = 4
    for y,row in enumerate(matrix):
        for x in enumerate(row):
            if y == 0 or x[0] == 0 or x [0]== len(row)-1 or y == len(matrix)-1:
                matrix[y][x[0]] = 9
    return matrix




def point_to_coord(point: tuple[int,int], tile_size:int):
    """Turns a point to coordinates in the matrix according to the matrix tile size.

    Args:
        point (tuple[int,int]): The point to be placed in the matrix.
        tile_size (int): Size of a single value in the matrix.

    Returns:
        tuple[int,int]: Coordinates of the given point transformed to coordinates in the matrix.
    """
    x = int((point[0]-point[0]%tile_size)//tile_size)
    y = int((point[1]-point[1]%tile_size)//tile_size)
    return (x,y)




def rect_to_coord(rect :Rectangle, tile_size :int):
    """Creates a list of points contained in the area of a rectangle.

    Args:
        rect (Rectangle): Rectangle to be added to the matrix
        tile_size (int): Size of a single value in the matrix.

    Returns:
        list[tuple[int,int]]: A list of all the points within the area of the rectangle.
    """
    coords = []
    x, y = rect.edges[0][0]
    x = int(x//tile_size)
    y = int(y//tile_size)
    width = rect.width//tile_size
    height = rect.height//tile_size
    for r in range(height):
        for c in range(width):
            coords.append((x+c,y+r))
    return coords

def closest_walls(matrix:list):
    """Changes walls next to a room or corridor to different wall.
    This is to have different sprite images for different walls.

    Args:
        matrix (list): Matrix to be changed.

    Returns:
        matrix (list): New matrix with changed values.
    """
    new_matrix = matrix.copy()
    for y,col in enumerate(new_matrix):
        for x,item in enumerate(col):
            if item in (0,9):
                if y==0 and x==0:
                    if new_matrix[y+1][x] in (1,2)\
                        or new_matrix[y][x+1] in (1,2)\
                        or new_matrix[y+1][x+1] in (1,2):
                        new_matrix[y][x]=5
                elif y==len(new_matrix)-1 and x==len(col)-1:
                    if new_matrix[y-1][x] in (1,2)\
                    or new_matrix[y][x-1] in (1,2):
                        new_matrix[y][x]=5
                elif y==0 and x==len(col)-1:
                    if new_matrix[y+1][x] in (1,2)\
                    or new_matrix[y][x-1] in (1,2):
                        new_matrix[y][x]=5
                elif x==0 and y==len(matrix)-1:
                    if matrix[y-1][x] in (1,2)\
                    or matrix[y][x+1] in (1,2):
                        matrix[y][x]=5
                elif y==0:
                    if new_matrix[y][x-1] in (1,2)\
                        or new_matrix[y][x+1] in (1,2)\
                        or new_matrix[y+1][x] in (1,2):
                        new_matrix[y][x]=5
                elif x==0:
                    if new_matrix[y-1][x] in (1,2)\
                        or new_matrix[y][x+1] in (1,2)\
                        or new_matrix[y+1][x] in (1,2):
                        new_matrix[y][x]=5
                elif y==len(new_matrix)-1:
                    if new_matrix[y-1][x] in (1,2)\
                        or new_matrix[y][x-1] in (1,2):
                        new_matrix[y][x]=5
                elif x==len(col)-1:
                    if new_matrix[y-1][x] in (1,2)\
                        or new_matrix[y][x-1] in (1,2)\
                        or new_matrix[y+1][x] in (1,2):
                        new_matrix[y][x]=5
                else:
                    if new_matrix[y-1][x] in (1,2)\
                        or new_matrix[y][x-1] in (1,2)\
                        or new_matrix[y][x+1] in (1,2)\
                        or new_matrix[y+1][x] in (1,2):
                        new_matrix[y][x]=5
    return new_matrix
