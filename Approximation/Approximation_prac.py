from collections import defaultdict

edges = [[1,2],[1,3],[2,3],[1,4],[0,5],[4,3],[3,0]]

class Graph:
    def __init__(self, num_verts):
        self.adjacency_list = defaultdict(list)
        self.deg = [] # store degree of each vertex in nested list where each inner-list is [vertex, degree]
        self.discard = [] # this is used for the 2-Approximation Algorithm for Vertex Cover

    def A_L_builder(self, indices):
        for i in indices: # build the adjacency list
            self.add_edge(i[0], i[1])

    # add_edge builds the adjacency list
    def add_edge(self, v, u):
        # we add both edges since this is a undirected graph
        self.adjacency_list[int(v)].append(int(u))
        self.adjacency_list[int(u)].append(int(v))

    # log(n)-Approximation Algorithm for Vertex Cover
    def SmartGreedyVertexCover(self, edges):
        """Input: A graph G
            Output: A set of vertices that form a (not necessarily optimal) vertex cover."""

        self.A_L_builder(edges)

        C = set()  # C is initialized to be the empty set
        while len(self.adjacency_list) > 0:  # while G has at least one edge
            # we can't sort a dictionary (self.adjacency_list is a dict) so we create a list, 'deg' instead
            # we need the vertex in G with maximum degree
            for i in self.adjacency_list:
                self.deg.append([len(self.adjacency_list[i]), i])
            self.deg.sort(reverse=True) # the first item in this list will be the vertex with max degree

            v = self.deg[0][1] # vertex in G with maximum degree
            del self.adjacency_list[v] # G ← G \ v
            for i in self.adjacency_list: # This also removes all edges adjacent to v
                if v in self.adjacency_list[i]:
                    self.adjacency_list[i].remove(v)
            C.add(v)
            self.deg = [] # we need to rebuild this less v
        return C


    # 2-Approximation Algorithm for Vertex Cover
    def BasicGreedyVertexCover(self, edges):
        """Input: A graph G
            Output: A set of vertices that form a (not necessarily optimal) vertex cover."""

        self.A_L_builder(edges)

        C_1 = set()  # C is initialized to be the empty set
        while len(edges) > 0:  # while G has at least one edge
            # we choose any edge, (u,v) in G
            # the only restriction is that we choose a different edge each time, self.discard stores all previously
            # ... choosen edges
            # we also can't re use the same vertex, see below for enforcement
            not_satisfied = True
            while not_satisfied:
                if len(edges) == 0:
                    break
                elif edges[0][0] in self.discard or edges[0][1] in self.discard:
                    del edges[0] # G ← G \ {u, v}, this also removes any edges adjacent to u and to v
                else:
                    u = edges[0][0]
                    v = edges[0][1]
                    del edges[0] # G ← G \ {u, v}, this also removes any edges adjacent to u and to v
                    not_satisfied = False # we can leave the loop if we found a satisfactory edge
            '''
            # we delete each vertex of edge i, u, v, and all edges adjacent to vertices u and to v
            del self.adjacency_list[u] # G ← G \ u
            del self.adjacency_list[v]  # G ← G \ v
            for i in self.adjacency_list: # This also removes all edges adjacent to u and to v
                if u in self.adjacency_list[i]:
                    self.adjacency_list[i].remove(u)
                if v in self.adjacency_list[i]:
                    self.adjacency_list[i].remove(v)
            '''
            C_1.add(u), C_1.add(v)
            self.discard.append(u), self.discard.append(v) # stores "deleted" vertices
        return C_1





g = Graph(len(edges))
print(g.SmartGreedyVertexCover(edges))

print(g.BasicGreedyVertexCover(edges))







