# %% Graph class
# this is adjacency list
class Graph:
    def __init__(self, argv_vertices_count) -> None:
        # array
        self.vertices = [None] * argv_vertices_count
        for i in range(argv_vertices_count):
            self.vertices[i] = Vertex(i)

    def add_edges(self, argv_edges, argv_direct=True):
        for edge in argv_edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            # add u to v
            current_edge = Edge(u, v, w)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)
            # add v to u
            if not argv_direct:
                current_edge = Edge(v, u, w)
                current_vertex = self.vertices[v]
                current_vertex.add_edge(current_edge)

    def __str__(self) -> str:
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex " + str(vertex) + "\n"
        return return_string

    def bfs(self, source):
        """
        Function for BFS, starting from source
        INCOMPLETE -> UNRRUNABLE
        """
        source = self.vertices[source]
        return_bfs = []
        discovered = []  # this is a queue
        discovered.append(source)
        while len(discovered) > 0:
            # serve from queue
            # u = discovered.serve()
            u = discovered.pop(0)  # pop(0) same as serve
            u.visited = True  # means I have visited u
            return_bfs.append(u)
            for edge in u.edges:
                v = edge.v
                v = self.vertices[v]
                if v.discovered == False:
                    discovered.append(v)
                    v.discovered = True  # means I have discovered v, adding it to queue
        return return_bfs


class Vertex:
    def __init__(self, id) -> None:
        self.id = id
        # list
        self.edges = []
        # for traversal
        self.discovered = False
        self.visited = False
        # distance
        self.distance = 0
        # backtracking / where i was from
        self.previous = None

    def add_edge(self, edge):
        self.edges.append(edge)

    def added_to_queue(self):
        self.discovered = True

    def visit_node(self):
        self.visited = True

    def __str__(self) -> str:
        return_string = str(self.id)
        for edge in self.edges:
            return_string += "\n with edges" + str(edge)
        return return_string


class Edge:
    def __init__(self, u, v, w) -> None:
        self.u = u
        self.v = v
        self.w = w

    def __str__(self) -> str:
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w)
        return return_string


# %% create a graph w/ 5 edges
if __name__ == "__main__":
    pass
