from queue import PriorityQueue
from src.list_matrix import point_to_coord




def build_path(matrix :list[list[int]], edges:set, tile_size:int):
    """Function brings together all needed functions to form
    paths between all points in the point list,
    and inserting information of paths to a matrix

    Args:
        matrix (list[list[int]]): Original matrix used.
        edges (set): List of tuples containing two points.
        Paths are formed between the two points
        tile_size (int): Size of tiles in the matrix.

    Returns:
        list[list[int]]: A new matix with all paths formed.
    """
    new_matrix = matrix.copy()
    for edge in edges:
        start, end = edge
        sx,sy = point_to_coord(start,tile_size)
        start = (sy,sx)
        ex,ey = point_to_coord(end,tile_size)
        end = (ey,ex)
        graph = weighted_graph(new_matrix)
        path = shortest_path(a_star(graph, start, end), start, end)
        for point in path:
            row,col = point
            if new_matrix[row][col] != 3 and new_matrix[row][col] != 4:
                new_matrix[row][col] = 2
    return new_matrix




def shortest_path(previous, start, goal):
    """Creates a list containing each point belonging to the shortest path from start to goal.

    Args:
        previous (dict): A dict with points as a key and value.
        start (tuple[int,int]): Starting point.
        goal (tuple[int,int]): Goal point.

    Returns:
        list: List containing each point in the shortest path between two points.
    """
    path = []
    location = goal
    if goal not in previous:
        return []
    while location != start:
        path.append(location)
        location = previous[location]
    path.append(start)
    return path




def a_star(graph:dict, start_point:tuple[int,int], end_point:tuple[int,int]):
    """A* pathfinding algorithm used in a weighted graph or a weighted and directed graph.
    Generates a path between two points.

    Args:
        graph (dict): Weighted graph in which both starting and end point are.
        start_point (tuple[int,int]): Starting point of A*.
        end_point (tuple[int,int]): The goal point of A*.

    Returns:
        dict: Path between the two points.
        A dict with nodes as keys and their previous node as item.
    """
    passed = PriorityQueue(0)
    passed.put((0,start_point))
    previous = {}
    cost_so_far = {}
    previous[start_point] = None
    cost_so_far[start_point] = 0

    while not passed.empty():
        location = passed.get()[1]

        if location == end_point:
            break

        for next in graph[location]:
            cost = cost_so_far[location] + next[1]
            if next[0] not in cost_so_far or cost < cost_so_far[next[0]]:
                cost_so_far[next[0]] = cost
                priority = cost + heuristics(next[0], end_point)
                passed.put((priority,next[0]))
                previous[next[0]] = location
    return previous




def heuristics(a:tuple[int,int], b:tuple[int,int]):
    """Heuristic to see how close point a is to point b.

    Args:
        a (tuple[int,int]): Current location of pathfinding algorithm.
        b (tuple[int,int]): Goal of the pathfinding algorithm.

    Returns:
        int: The current distance between the two points.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1-x2) + abs(y1-y2)




def weighted_graph(matrix:list[list[int]]):
    """Function creates a weighted graph.
    Weights of edges depend on the nodes values in the matrix.

    Args:
        matrix (list[list[int]]): Matrix holding node values.

    Returns:
        dict: A weighted and directed graph,
        which pahtfinding algorithms can use to find fastest path.
    """
    nodes = []
    for row in enumerate(matrix):
        for column in enumerate(matrix[row[0]]):
            new_node = (row[0],column[0])
            nodes.append(new_node)
    map = {node : [] for node in nodes}
    for node in nodes:
        if node == (0,0):
            new_edge(node, (0,1), map,matrix)
            new_edge(node, (1,0), map,matrix)
        elif node == (len(matrix)-1,len(matrix[0])-1):
            new_edge(node, (len(matrix)-2,len(matrix[0])-1),map,matrix)
            new_edge(node, (len(matrix)-1,len(matrix[0])-2),map,matrix)
        elif node == (0,len(matrix[0])-1):
            new_edge(node,(0,len(matrix[0])-2),map,matrix)
            new_edge(node,(1,node[1]),map,matrix)
        elif node == (len(matrix)-1,0):
            new_edge(node,(len(matrix)-2,0),map,matrix)
            new_edge(node,(len(matrix)-1,1),map,matrix)
        elif node[0] == 0:
            new_edge(node,(0,node[1]-1),map,matrix)
            new_edge(node,(1,node[1]),map,matrix)
            new_edge(node, (0,node[1]+1),map,matrix)
        elif node[1] == 0:
            new_edge(node,(node[0]-1,0),map,matrix)
            new_edge(node,(node[0],1),map,matrix)
            new_edge(node, (node[0]+1,0),map,matrix)
        elif node[0] == len(matrix)-1:
            new_edge(node,(len(matrix)-1,node[1]-1),map,matrix)
            new_edge(node,(len(matrix)-2,node[1]),map,matrix)
            new_edge(node,(len(matrix)-1,node[1]+1),map,matrix)
        elif node[1] == len(matrix[0])-1:
            new_edge(node,(node[0]-1,len(matrix[0])-1),map,matrix)
            new_edge(node,(node[0],len(matrix[0])-2),map,matrix)
            new_edge(node, (node[0]+1,len(matrix[0])-1),map,matrix)
        else:
            new_edge(node,(node[0],node[1]-1),map,matrix)
            new_edge(node,(node[0],node[1]+1),map,matrix)
            new_edge(node,(node[0]-1,node[1]),map,matrix)
            new_edge(node,(node[0]+1,node[1]),map,matrix)
    return map




def new_edge(node_a:tuple[int,int], node_b:tuple[int,int], map:dict, matrix):
    """Function used by weighted_graph to
    generate correct weights to the graph.

    Args:
        node_a (tuple[int,int]): Starting node from which we move to end node.
        node_b (tuple[int,int]): End node which defines the weight
        together with starting node.
        map (dict): Weighted graph where node weights are added.
        matrix (list[list[int]]): Matrix holding information about node values.
    """

    if matrix[node_b[0]][node_b[1]]==2:
        map[node_a].append((node_b, 1))
    elif matrix[node_a[0]][node_a[1]]==1 and matrix[node_b[0]][node_b[1]]==1:
        map[node_a].append((node_b, 4))
    elif matrix[node_a[0]][node_a[1]]==9 and matrix[node_b[0]][node_b[1]]==9:
        map[node_a].append((node_b, 6))
    elif matrix[node_b[0]][node_b[1]]==9:
        map[node_a].append((node_b, 5))
    elif matrix[node_b[0]][node_b[1]]==1:
        map[node_a].append((node_b, 3))
    else:
        map[node_a].append((node_b, 2))
