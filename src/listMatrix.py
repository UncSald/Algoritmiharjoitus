from src.geometry import Rectangle

# LIST TO MATRIX TAKES A LIST OF RECTANGLES AND A LIST OF THEIR CENTERS
# AS PARAMETERS
# IT THEN RETURNS THE ROOMS AND THEIR CENTERS PLACED IN A MATRIX


def list_to_matrix(rooms :list, width :int,\
                   height :int, start :tuple[int,int], end:tuple[int,int], tile_size :int):
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
    for i in range((height-height%tile_size)//tile_size):
        matrix.append([])
    for row in matrix:
        for i in range((width-width%tile_size)//tile_size):
            row.append(0)
    for room in rooms:
        for point in rect_to_coord(room, tile_size):
            x,y = point
            matrix[y][x] = 1
    sx,sy = point_to_coord(start,tile_size)
    matrix[sy][sx] = 3
    ex, ey = point_to_coord(end,tile_size)
    matrix[ey][ex] = 4
    y = 0
    for row in matrix:
        x = 0
        for column in row:
            if y == 0 or x == 0 or x == len(row)-1 or y == len(matrix)-1:
                matrix[y][x] = 9
            x+=1
        y+=1
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
