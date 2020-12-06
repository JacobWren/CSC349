import sys
from stack_array import *
from collections import defaultdict

'''We find the strongly connected components of a directed graph. This is essentially 
done by two DFS's. The only trick is that for the second DFS, we reverse the graph (i.e., change 
the direction of the arrows ) and then the order of our DFS is determined by the order of the stack from 
the first DFS (in contrast, the order of our first DFS didn't matter). The first element in the stack (top) finished 
last, while the last element (bottom) finished first.'''

def main(argv):
    # reads in file of tuples less the parantheses, such as: 1, 0. The 1 is a vertex that
    # has a 'path' or 'points' toward the zero.
    indices = [] # We will put edge/vertex information from file in here
    i = 0
    a = set() # need to count the number of vertices
    file_in = open(sys.argv[1], "r", newline="")
    for line in file_in:
        indices.append((line.split(', ')))
        indices[i][1] = indices[i][1].rstrip('\n')
        a.add(indices[i][0])
        a.add(indices[i][1])
        i += 1
    g = Graph(len(a))
    scc = g.conn_components(indices)
    for i in scc: # sort inner list first
        i.sort()
    scc.sort()
    print(len(scc), 'Strongly Connected Component(s):')
    for i in scc:  # print to screen
        print(*i, sep=", ")

# command line to run:
# python Graph.py test5.txt

class Graph:
    def __init__(self, num_verts):
        self.adjacency_list = defaultdict(list)  # Much better then a nested list!
        self.adjacency_list_reversed = defaultdict(list) # This is needed for the second DFS, rather than clearing
        # out the one above.
        self.connected_comps = []
        self.all_connected_comps = []
        self.num_vertices = num_verts

    # add_edge builds the adjacency list
    def add_edge(self, v, u):
        self.adjacency_list[int(v)].append(int(u))

    # build's adjacency list for reversed graph (v and u are switched when we pass them in)
    def add_edge_reverse(self, v, u):
        self.adjacency_list_reversed[int(v)].append(int(u))

    # each time neighbor_search_reversed is called it finds all of the vertices that are strongly connected
    # in that one of potentially many components!
    # This is a DFS but we don't push anything onto stack, instead we gather all vertices in the
    # strongly connected component
    # DFS #2
    def neighbor_search_reversed(self, v, discovered, connected_comps):
        discovered[v] = "discovered" # we found the vertex!
        connected_comps.append(v)

        for i in self.adjacency_list_reversed[v]:
            if discovered[i] == "not discovered":
                self.neighbor_search_reversed(i, discovered, connected_comps)

    # DFS #1
    def neighbor_search(self, v, discovered, stack):
        discovered[v] = "discovered"
        for i in self.adjacency_list[v]:
            if discovered[i] == "not discovered":
                self.neighbor_search(i, discovered, stack)
        stack = stack.push(v) # v has finished, i.e., all of its neighbors have been seen

    def conn_components(self, indices):
        for i in indices: # build the adjacency list
            self.add_edge(i[0], i[1])

        stack = Stack(self.num_vertices)

        discovered = ["not discovered"] * (self.num_vertices) # intially we haven't discovered any vertices

        # We are assuming that vertex identifiers are contiguous natural numbers —
        # they begin at 0, and there will be no “gaps” in the identifiers used.
        for i in range(self.num_vertices):
            if discovered[i] == "not discovered":
                self.neighbor_search(i, discovered, stack)

        for i in indices: # build the adjacency list for reversed graph
            self.add_edge_reverse(i[1], i[0])

        # intially we haven't discovered any vertices for DFS #2
        discovered = ["not discovered"] * (self.num_vertices)

        while not stack.is_empty(): # Structure for DFS #2
            i = stack.pop()
            if discovered[i] == "not discovered":
                self.neighbor_search_reversed(i, discovered, self.connected_comps)
                self.all_connected_comps.append(self.connected_comps)
                self.connected_comps = [] # clear sub list

        return self.all_connected_comps

if __name__ == "__main__":
    main(sys.argv)
