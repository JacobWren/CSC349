import itertools
from collections import defaultdict
import copy
import sys

#edges = [[1,2],[1,3],[2,3],[1,4],[0,5],[4,3],[3,0]]
#edges = [[0,1],[1,2],[2,0]]
#edges = [[0,1],[2,3],[4,5],[6,7],[8,9]]

# Input: A graph G = (V, E).
# Goal: Find a vertex cover of minimum size.


# We will implement a log(n)-approximation algorithm,
# a 2-approximation algorithm for this problem,
# and an exact (but slow) algorithm.


def main(argv):
    # read in file containing of edges, i.e., vertices separated by a space on different lines
    # This is just dirty work, nothing special
    X = []
    i = 0
    file_in = open(sys.argv[1], "r", newline="")
    for line in file_in:
        X.append(line)
        X[i] = X[i].rstrip('\n')
        i += 1
    X_prime = []
    for i in X:
        X_prime.append(i.split(" "))
    edges = []
    temp = []
    for j in X_prime:
        temp.append(int(j[0])), temp.append(int(j[1]))
        edges.append(temp)
        temp = []

    g = Graph(len(edges))

    print("log-Approximation:", end=' ')
    for i in g.SmartGreedyVertexCover(edges):
        print(i, end=' ')
    print()

    print("2-Approximation:", end=' ')
    for j in g.BasicGreedyVertexCover(edges):
        print(j, end=' ')
    print()

    print("Exact Solution:", end=' ')
    for k in g.BruteForceVertexCover(edges):
        print(k, end=' ')

    # command line to run:
    # python3 Approximation.py in1.txt


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

        self.A_L_builder(edges) # adjacency list

        C = set()  # C is initialized to be the empty set
        while len(self.adjacency_list) > 0:  # while G has at least one edge
            delete = [] # for later use
            # we can't sort a dictionary (self.adjacency_list is a dict) so we create a list, 'deg' instead
            # we need the vertex in G with maximum degree
            res = bool(self.adjacency_list)
            for i in self.adjacency_list:
                self.deg.append([len(self.adjacency_list[i]), i])
            self.deg.sort(reverse=True) # the first item in this list will be the vertex with max degree

            v = self.deg[0][1] # vertex in G with maximum degree
            del self.adjacency_list[v] # G ← G \ v
            for i in self.adjacency_list: # This also removes all edges adjacent to v
                if v in self.adjacency_list[i]:
                    self.adjacency_list[i].remove(v)
                    if self.adjacency_list[i] == []: # store "edges" (dead edges) to be deleted
                        delete.append(i)
            for i in delete: # clean up! If no edge exists, delete it!
                del self.adjacency_list[i]
            C.add(v)
            self.deg = [] # we need to rebuild this less v
        return C


    # 2-Approximation Algorithm for Vertex Cover
    def BasicGreedyVertexCover(self, edges):
        """Input: A graph G
            Output: A set of vertices that form a (not necessarily optimal) vertex cover."""

        E = copy.deepcopy(edges) # don't mess up edges, we need it later

        C_1 = set()  # C is initialized to be the empty set
        while len(E) > 0:  # while G has at least one edge
            # we choose any edge, (u,v) in G
            # the only restriction is that we choose a different edge each time, self.discard stores all previously
            # ... choosen edges
            # we also can't re use the same vertex, see below for enforcement
            not_satisfied = True
            while not_satisfied:
                if len(E) == 0:
                    break
                elif E[0][0] in self.discard or E[0][1] in self.discard:
                    del E[0] # G ← G \ {u, v}, this also removes any edges adjacent to u and to v
                else:
                    u = E[0][0]
                    v = E[0][1]
                    del E[0] # G ← G \ {u, v}, this also removes any edges adjacent to u and to v
                    not_satisfied = False # we can leave the loop if we found a satisfactory edge
            C_1.add(u), C_1.add(v)
            self.discard.append(u), self.discard.append(v) # stores "deleted" vertices
        return C_1


    # Brute force (exact) algorithm for vertex cover
    def BruteForceVertexCover(self, edges):
        self.A_L_builder(edges)  # adjacency list
        vertex_set = set() # initialize empty set

        for i in edges:
            vertex_set.add(i[0]), vertex_set.add(i[1])
        vertex_list = list(vertex_set)
        Current_best_vc = vertex_list # initialize vertex cover, clearly this the max vertex cover - i.e., we can't do worse
        # set low expectations, then exceed them :)

        # now, we will look at EVERY possible subset of vertices
        for length in range(1, len(vertex_list) + 1): # start at 1 to avoid empty set
            for subset in itertools.combinations(vertex_list, length): # we need every subset for all lengths
                sub_list = list(subset)
                number_of_edges_covered = 0
                double_count_edge = [] # need for later use... see below
                # is sub_list a v.c.?
                # let's count the number of edges covered to find out... vertex cover really is a poor name :(
                adjacent_vertices_and_vertices = set() # none yet...
                for i in sub_list:
                    for j in self.adjacency_list[i]: # j is adjacent to i
                        if j not in double_count_edge: # else we would count the same edge twice :(
                            number_of_edges_covered += 1
                    double_count_edge.append(i)
                if number_of_edges_covered == len(edges): # check if we have a v.c.
                    if len(sub_list) < len(Current_best_vc): # is this vertex cover any better, i.e., any smaller then
                        # ... what we currently have in Current_best_vc?
                        Current_best_vc = sub_list # we use sub_list here to update best vc since sub_list
                        # ... contains the vertices we are 'holding'
        return Current_best_vc

if __name__ == "__main__":
    main(sys.argv)
