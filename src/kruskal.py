"""Module holds the kruskal function which generates a minimum
spanning tree from a set of edges between points.
The find function is a recursive function that checks if two points
already have a link. If they don't they can be connected.
"""

def kruskal(edge_list :set, start_point :tuple[int,int]):
    """Kruskal algorithm creates a minimum spanning tree.

    Args:
        edge_list (set): A list of edges between two points.
        start_point (tuple[int,int]): A point from which the path starts.

    Returns:
        list: Returns new edges without loops between them.
    """
    edges = []
    new_edges = []
    point_list = set()
    for edge in edge_list:
        point_list.add(edge[0])
        point_list.add(edge[1])
    linked = {point : None for point in point_list}
    size = {point: 1 for point in point_list}
    for edge in edge_list:
        if start_point in edge:
            edges.append((edge[0], edge[1], 0))
        else:
            edges.append((edge[0], edge[1], 1))
    edge_count = 0
    tree_weight = 0
    for edge in edges:
        point_a, point_b, weight = edge
        if find(linked,point_a) != find(linked,point_b):
            a = find(linked,point_a)
            b = find(linked,point_b)
            if a == b:
                continue
            if size[a] > size[b]:
                a, b = b, a
            linked[a] = b
            size[b] += size[a]
            new_edges.append((point_a,point_b))
            edge_count += 1
            tree_weight += weight
    return new_edges

def find(link, x):
    """Find a point in the dictionary

    Args:
        link (dict): Dictionary containing points already linked to the mst.
        x (tuple[int,int]): Point to be found in the dict.

    Returns:
        tuple[int,int]: Returns the point which is connected to the original point.
    """
    while link[x]:
        x = link[x]
    return x
