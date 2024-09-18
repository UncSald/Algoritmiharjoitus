def kruskal(edge_list :set, start_point):
    edges = []
    point_list = set()
    for edge in edge_list:
        point_list.add(edge[0])
        point_list.add(edge[1])

    linked = {point : None for point in point_list}
    size = {point: 1 for point in point_list}
    x = 0
    new_edges = []
    for edge in edge_list:
        if start_point in edge:
            edges.append((edge[0], edge[1], 0))
        else:
            edges.append((edge[0], edge[1], x))
        x+=1
    edge_count = 0
    tree_weight = 0
    for edge in edges:
        point_a, point_b, weight = edge
        if find(linked,point_a) != find(linked,point_b):
            a = find(linked,point_a)
            b = find(linked,point_b)
            if a == b:
                print(a,b)
                return
            if size[a] > size[b]:
                a, b = b, a
                print("sizes", size[a], size[b])
            linked[a] = b
            size[b] += size[a]
            new_edges.append((point_a,point_b))
            edge_count += 1
            tree_weight += weight
    

    return new_edges

def find(link, x):
    while link[x]:
        x = link[x]
    return x