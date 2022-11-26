#  File: TopoSort.py

#  Description: Uses TopoSort to sort vertices of a graph

#  Student Name: Reece Mathew

#  Student UT EID: rtm2244

#  Partner Name: Sai Chandrasekar

#  Partner UT EID: svc439

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/25/2022

#  Date Last Modified: 11/28/2022

import sys

# ---------------------------------------------------------------------------------------------------------------


class Vertex (object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine label of vertex
    def get_label(self):
        return self.label

    # string repr. of vertex
    def __str__(self):
        return str(self.label)
# ---------------------------------------------------------------------------------------------------------------


class Graph (object):
    def __init__(self):
        self.Vertices = []
        # 2d list of edges
        self.adjMat = []
    # ===========================================================================================
    # check if a vertex is already in the graph

    def has_Vertex(self, label):
        nVert = len(self.Vertices)

        # check every vertex for matching label
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False
    # ===========================================================================================
    # given the label, get the index of a vertex

    def get_index(self, label):
        nVert = len(self.Vertices)
        # return index of vertex with matching label
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1
    # ===========================================================================================
    # Add a Vertex with a given label to the graph

    def add_Vertex(self, label):
        # checks for redundancy
        if (self.has_Vertex(label)):
            return

        # add Vertex to list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert-1):
            (self.adjMat[i]).append(0)  # add a zero to end of each row

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)  # add a row of zeroes to adjMatrix
    # ===========================================================================================
    # add weighted directed edge to graph

    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
    # ===========================================================================================
    # add weighted undirected edge to graph

    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight
    # ===========================================================================================

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix

    def delete_vertex(self, vertexLabel):
        # get index of vertex and delete it from Vertices using index
        v = self.get_index(vertexLabel)
        del self.Vertices[v]

        del self.adjMat[v]  # delete the row containing the vertex's adjEdges
        for i in range(len(self.Vertices)):  # delete column containing adjEdges
            del self.adjMat[i][v]

    # ===========================================================================================

    ###################################### NEW CODE BELOW ########################################

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle(self):

        n = len(self.Vertices)

        for j in range(n):
            # Checks each vertex if there is a cycle starting from there. Returns true if so
            if (self.has_cycle_helper(j, [])):
                return True
        # Cycle not found across adjacency matrix
        return False

    def has_cycle_helper(self, index, indices_observed):
        n = len(self.Vertices)
        # Initializes list of indices observed starting at given vertex
        indices_observed.append(index)

        for i in range(n):
            # If vertex points to another
            if self.adjMat[index][i] == 1:

                # Checks if loop is made
                if i in indices_observed:
                    return True

                # Checks path
                elif (self.has_cycle_helper(i, indices_observed)):
                    return True

                # Loop is not made
                else:
                    return False

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
        # Final list of sorted vertices
        toposort_vertices = []

        # Add vertices until none remaining
        while len(self.Vertices) > 0:
            n = len(self.Vertices)
            # Initialize list of vertices removed in current level
            popped_vertices = []

            for i in range(n):
                no_incoming_edges = True

                for j in range(n):
                    # Check column-by-column
                    # If any value is 1, then that vertex has an incoming edge
                    if self.adjMat[j][i] == 1:
                        no_incoming_edges = False
                        break

                # Add vertex to list of popped vertices
                if no_incoming_edges == True:
                    popped_vertices.append(str(self.Vertices[i]))

            # Sort alphabetically
            popped_vertices.sort()
            # Add to final list
            toposort_vertices += popped_vertices

            # Effectively delete vertex
            for vertex in popped_vertices:
                self.delete_vertex(vertex)

        return toposort_vertices


def main():
    # create the Graph object
    theGraph = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)
    # num vertices to the list of vertices
    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        vertex = line.strip()
        theGraph.add_Vertex(str(vertex))

    # initialize char dictionary with padding constant #
    val_dict = {'#': -1}

    
    # Populate dictionary containing key-value pairs, pairing unique vertex with ordered integer value
    for i in range(num_vertices):
        val_dict[str(theGraph.Vertices[i])] = i

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)
    num_edges = int(line)


    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()

        # Add edges to adjacency matrix, using dictionary values for indices
        start = int(val_dict[edge[0]])
        finish = int(val_dict[edge[1]])

        theGraph.add_directed_edge(start, finish)

    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if (not theGraph.has_cycle()):
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)


if __name__ == "__main__":
    main()
