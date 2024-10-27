from src.sprites import GameTile




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
    for row, col in enumerate(matrix):
        for column, value in enumerate(col):
            if value in (1,2):
                new_tile = GameTile(tile_size,(column*tile_size, row*tile_size),\
                                    value)
                new_tile.add(floor)
            elif value == 3:
                new_tile = GameTile(tile_size,(column*tile_size, row*tile_size),\
                                    value)
                new_tile.add(floor)
            elif value == 4:
                new_tile = GameTile(tile_size,(column*tile_size, row*tile_size),\
                                    value)
                new_tile.add(doors)
            else:
                new_tile = GameTile(tile_size,(column*tile_size, row*tile_size),\
                                    value)
                new_tile.add(walls)
