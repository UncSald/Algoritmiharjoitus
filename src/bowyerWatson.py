from geometry import Triangle



# MAIN ALGORITHM FOR THE PROJECT

class BowyerWatson:
    # DEFINE POINTS, SET CONTAINING FINAL TRIANGULATION
    # AND EDGES USED IN TRIANGULATION
    # ALSO ADD SUPER TRIANGLE, WHICH IS ALWAYS BIG ENOUGH TO
    # CONTAIN THE WHOLE SCREEN WE DRAW ON
    def __init__(self, points, width, height):
        self._points = points
        self._triangulation = set()
        self._all_edges = set()
        self._original_triangle = Triangle((-width*2,height*2),\
                                           (width/2,-height*2), (width*4,height*2))
        self._triangulation.add(self._original_triangle)

    # RUN METHOD TO MAKE SURE EVERYTHING HAPPENS IN THE RIGHT ORDER
    def run(self):
        self.triangulate()
        self.remove_original()
        self.define_edges()
        return self._triangulation

    # TRIANGULATE METHOD CREATES A CORRECT DELAUNAY TRIANGULATION
    # FOR THE SET OF POINTS BY ADDING A POINT TO THE TRIANGULATION
    # ONE BY ONE
    def triangulate(self):
        for point in self._points:
            
            unusable_triangles = set()
            for triangle in self._triangulation:
                if triangle.check_point(point):
                    unusable_triangles.add(triangle)
            usable_edges = set()

            for triangle in unusable_triangles:
                for edge in triangle._edges:
                    appears_in_others = False
                    for other_triangle in unusable_triangles:
                        if edge in other_triangle._edges and other_triangle != triangle:
                            appears_in_others = True
                    if appears_in_others is False:
                        usable_edges.add(edge)


            for triangle in unusable_triangles:
                self._triangulation.remove(triangle)
            
            for edge in usable_edges:
                if point not in edge:
                    new_triangle = Triangle(edge[0], edge[1], point)
                    self._triangulation.add(new_triangle)


    # REMOVES ALL TRIANGLES CONTAINING POINTS WHICH
    # BELONG TO THE SUPER TRIANGLE
    def remove_original(self):
        point_with_original = set()
        for point in self._original_triangle._points:
            for triangle in self._triangulation:
                if point in triangle._points:
                    point_with_original.add(triangle)
        for triangle in point_with_original:
            self._triangulation.remove(triangle)



    # SIMPLE METHOD TO SAVE ALL THE EDGES IN THE TRIANGULATION
    def define_edges(self):
        for triangle in self._triangulation:
            for edge in triangle._edges:
                self._all_edges.add(edge)
                