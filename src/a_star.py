from queue import PriorityQueue
from src.listMatrix import point_to_coord


# FUNCTION BRINGS TOGETHER ALL OF THE NEEDED STEPS
# TO CREATE PATHS TO THE MATRIX
def build_path(matrix, edges, tile_size:int):
    for edge in edges:
        start, end = edge
        sx,sy = point_to_coord(start,tile_size)
        start = (sy,sx)
        ex,ey = point_to_coord(end,tile_size)
        end = (ey,ex)
        graph = weighted_graph(matrix)
        path = shortest_path(a_star(graph, start, end), start, end)
        for point in path:
            row,col = point
            matrix[row][col] = 2
    return matrix


# FUNCTION TAKES AS INPUT THE EDGES TAKEN BY
# A* TO FIND THE SHORTEST PATH AND OUTPUTS A
# LIST OF THE POINTS
def shortest_path(previous, start, goal):
    path = []
    location = goal
    if goal not in previous:
        return []
    while location != start:
        path.append(location)
        location = previous[location]
    path.append(start)
    return path



# A* FUNCTION WHICH TAKES IN A MATRIX, A STARTING POINT
# AND AN ENDPOINT, AND FINDS THE SHORTEST PATH BETWEEN
# THE POINTS. OUTPUTS TWO DICTS
def a_star(graph, start_point, end_point):
    passed = PriorityQueue(0)
    passed.put((start_point, 0))
    previous = {}
    cost_so_far = {}
    previous[start_point] = None
    cost_so_far[start_point] = 0

    while not passed.empty():
        location = passed.get()[0]

        if location == end_point:
            break

        for next in graph[location]:
            cost = cost_so_far[location] + next[1]
            if next[0] not in cost_so_far or cost < cost_so_far[next[0]]:
                cost_so_far[next[0]] = cost
                priority = cost + heuristics(next[0], end_point)
                passed.put((next[0], priority))
                previous[next[0]] = location
    return previous



# HEURISTIC TO DETERMINE CURRENT POINT DISTANCE TO GOAL
def heuristics(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1-x2) + abs(y1-y2)



# A FUNCTION WHICH CREATES A WEIGHTED GRAPH
# BASED ON A MATRIX

def weighted_graph(matrix):
    nodes = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            new_node = (row,column)
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




# CREATES A NEW EDGE WITH 1 WHEIGHT TO THE MAP
def new_edge(node_a, node_b, map, matrix):

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
