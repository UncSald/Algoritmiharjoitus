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
        if width<=0 or height<=0:
            raise ValueError ("Draw area cannot be 0 or negative.")
        if len(points) < 3:
            raise ValueError ("Triangles cannot be drawn with less than 3 points.")
        self.width = width
        self.height = height
        self.points = points
        self.triangulation = set()
        self.all_edges = set()
        self._original_triangle = Triangle((-width*2,height*2),\
                                           (width/2,-height*2), (width*4,height*2))
        self.triangulation.add(self._original_triangle)

    # RUN METHOD TO MAKE SURE EVERYTHING HAPPENS IN THE RIGHT ORDER
    def run(self):
        """Runs the algorithm on the set of points.

        Returns:
            set: Complete triangulation.
        """
        self.triangulate()
        self.remove_original()
        self.define_edges()


    def triangulate(self):
        """Creates a correct delaunay triangulation by adding each point to the set one by one.
        """
        for point in self.points:
            if self.width<point[0] or 0>point[0] or self.height<point[1] or 0>point[1]:
                self.points.remove(point)
                print(f"{point} is not inside the drawing area.")
                if len(self.points) < 3:
                    raise ValueError ("Too many bad points.\
                                      Triangles cannot be drawn with less than 3 points.")
                continue
            qualifying_edges = self.qualifying_edges(point)

            for edge in qualifying_edges:
                if point not in edge:
                    new_triangle = Triangle(edge[0], edge[1], point)
                    self.triangulation.add(new_triangle)

    def qualifying_edges(self,point:tuple[int,int]):
        """Define the edges in the triangulation which
        can be used for the new triangles.

        Args:
            point (tuple[int,int]): Point to be added to the triangulation

        Returns:
            list[tuple[tuple]]: list containing edges surrounding the new point.
        """
        unusable_triangles = []
        usable_edges = []
        for triangle in self.triangulation:
            if triangle.check_point(point):
                unusable_triangles.append(triangle)

        for triangle in unusable_triangles:
            for edge in triangle.edges:
                appears_in_others = False
                for other_triangle in unusable_triangles:
                    if edge in other_triangle.edges and other_triangle != triangle:
                        appears_in_others = True
                if appears_in_others is False:
                    usable_edges.append(edge)

        for triangle in unusable_triangles:
            self.triangulation.remove(triangle)

        return usable_edges

    def remove_original(self):
        """Removes all triangles containing a point of
        the super triangle from the final triangulation.
        """
        point_with_original = set()
        for point in self._original_triangle.points:
            for triangle in self.triangulation:
                if point in triangle.points:
                    point_with_original.add(triangle)
        for triangle in point_with_original:
            self.triangulation.remove(triangle)



    def define_edges(self):
        """Creates a set of all edges of the generated triangles.
        """
        for triangle in self.triangulation:
            for edge in triangle.edges:
                self.all_edges.add(edge)
