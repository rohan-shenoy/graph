class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def is_edge(self, vertices):
        if self.vertex1 in vertices and self.vertex2 in vertices:
            return True
        else:
            return False

    def __repr__(self):
        """Edge format: (vertex1, vertex2)"""
        return "("  + str(self.vertex1) + "," + str(self.vertex2) + ")"

    def contains_vertex(self, vertex):
        """Returns True if an Edge contains vertex and False otherwise"""
        if vertex == self.vertex1 or vertex == self.vertex2:
            return True
        else:
            return False
    def other_vertex(self, vertex):
        if vertex == self.vertex1:
            return self.vertex2
        else:
            return self.vertex1




class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        self.edges = []
        for i in edges:
            if i.is_edge(self.vertices):
                self.edges.append(i)

    def neighbors(self, vertex):
        """Returns all the given neighbors(adjacent vertices) of a given vertex"""
        assert vertex in self.vertices
        neighborhood = []
        for edge in self.edges:
            if edge.contains_vertex(vertex):
                neighborhood.append(edge.other_vertex(vertex))
        return neighborhood
                
            

    def is_connected(self):
        """Returns True if a graph is connected and false otherwise"""