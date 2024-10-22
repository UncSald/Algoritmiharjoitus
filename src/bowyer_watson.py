from src.geometry import Triangle


class BowyerWatson:
    """Main algorithm for the project.
    The bowyer-watson algorithm generates a delaunay triangulation between a set of points.
    """
    def __init__(self, points :set, width :int, height :int):
        """Class constructor which creates a new BowyerWatson -object.

        Args:
            points (set): Set containing points which will be added to triangulation.
            width (int): Width of the area containing all points.
            height (int): Height of the area containing all points.
        """
        self._points = points
        self._triangulation = set()
        self._all_edges = set()
        self._original_triangle = Triangle((-width*2,height*2),\
                                           (width/2,-height*2), (width*4,height*2))
        self._triangulation.add(self._original_triangle)

    # RUN METHOD TO MAKE SURE EVERYTHING HAPPENS IN THE RIGHT ORDER
    def run(self):
        """Runs the algorithm on the set of points.

        Returns:
            set: Complete triangulation.
        """
        self.triangulate()
        self.remove_original()
        self.define_edges()
        return self._triangulation

    def triangulate(self):
        """Creates a correct delaunay triangulation by adding each point to the set one by one.
        """
        for point in self._points:
            unusable_triangles = set()
            for triangle in self._triangulation:
                if triangle.check_point(point):
                    unusable_triangles.add(triangle)
            usable_edges = set()

            for triangle in unusable_triangles:
                for edge in triangle.edges:
                    appears_in_others = False
                    for other_triangle in unusable_triangles:
                        if edge in other_triangle.edges and other_triangle != triangle:
                            appears_in_others = True
                    if appears_in_others is False:
                        usable_edges.add(edge)


            for triangle in unusable_triangles:
                self._triangulation.remove(triangle)

            for edge in usable_edges:
                if point not in edge:
                    new_triangle = Triangle(edge[0], edge[1], point)
                    self._triangulation.add(new_triangle)


    def remove_original(self):
        """Removes all triangles containing a point of
        the super triangle from the final triangulation.
        """
        point_with_original = set()
        for point in self._original_triangle._points:
            for triangle in self._triangulation:
                if point in triangle._points:
                    point_with_original.add(triangle)
        for triangle in point_with_original:
            self._triangulation.remove(triangle)



    def define_edges(self):
        """Creates a set of all edges of the generated triangles.
        """
        for triangle in self._triangulation:
            for edge in triangle.edges:
                self._all_edges.add(edge)
