from src.sprites import Floor, Wall, Door



def create_objects(matrix :list[list[int]], tile_size :int, floor, walls, doors):
    """Creates objects according to their location in the matrix.
    Objects are then addded to sprite gtoups.

    Args:
        matrix (list[list[int]]): Matrix holding value for each sprite type.
        tile_size (int): Size of tiles in the matrix
        floor (pygame.sprite.Group): Group where floor sprites will be added.
        walls (pygame.sprite.Group): Group where wall sprites will be added.
        doors (pygame.sprite.Group): Group where door sprites will be added.
    """
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):

            if matrix[row][column] == 1:
                new_tile = Floor(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size),1)
                new_tile.add(floor)
            elif matrix[row][column] == 2:
                new_tile = Floor(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size),2)
                new_tile.add(floor)
            elif matrix[row][column] == 3:
                new_tile = Door(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size),3)
                new_tile.add(floor)
            elif matrix[row][column] == 4:
                new_tile = Door(tile_size, tile_size,\
                                 (column*tile_size, row*tile_size),4)
                new_tile.add(doors)
            else:
                new_tile = Wall(tile_size, tile_size,\
                                (column*tile_size, row*tile_size))
                new_tile.add(walls)
