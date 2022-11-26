#  File: Graph.py

#  Description: Create and test methods for the Graph Data Structure

#  Student Name: Sai Chandrasekar

#  Student UT EID: svc439

#  Partner Name: Reece Mathew

#  Partner's UT EID: rtm 2244

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 11/16

#  Date Last Modified: 11/17

import sys

class Stack (object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return number of elements in the stack
    def size(self):
        return len(self.stack)
# ---------------------------------------------------------------------------------------------------------------
class Queue (object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the number of elements in the queue
    def size(self):
        return len(self.queue)
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
    def has_Vertex (self, label):
        nVert = len (self.Vertices)

        #check every vertex for matching label
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False
    # ===========================================================================================
    # given the label, get the index of a vertex
    def get_index (self, label):
        nVert = len (self.Vertices)
        # return index of vertex with matching label
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1
    # ===========================================================================================
    # Add a Vertex with a given label to the graph
    def add_Vertex (self, label):
        # checks for redundancy
        if (self.has_Vertex (label)):
            return
        
        # add Vertex to list of vertices
        self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert-1):
            (self.adjMat[i]).append(0)  # add a zero to end of each row
        
        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row) # add a row of zeroes to adjMatrix
    # ===========================================================================================
    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
    # ===========================================================================================
    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adMat[start][finish] = weight
        self.adMat[finish][start] = weight
    # ===========================================================================================
    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)

        # return first vertex that is adjacent to vertex 'v' and has not been visited
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i].was_visited())):
                return i
        return -1
    # ===========================================================================================
    # do a depth first search in a graph from vertex v (index)
    def dfs (self, v):
        # create a Stack
        theStack = Stack()

        # mark starting vertex v as visited and push it on the stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])    # print visited vertex
        theStack.push (v)

        # visit all other vertices acording to depth
        while ( not theStack.is_empty() ):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u== -1):
                u = theStack.pop()
            else:
                # mark vertex visited and push it on the stack
                (self.Vertices[u]).visited = True
                print (self.Vertices[u]) # print visited vertex
                theStack.push (u)

        # the stack is emprty, let us reset the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False
    # ===========================================================================================
    # do a breadth first search in a graph starting at vertex v (index)

    def bfs(self, v):
        # create the Queue
        theQueue = Queue()

        # mark the vertex v as visited and put in in the Queue
        (self.Vertices[v]).visited = True
        theQueue.enqueue(v)

        # visit all the other vertices according to breadth
        while (not theQueue.is_empty()):

            u = theQueue.dequeue()
            print(self.Vertices[u]) # print current visited Vertex

            # go through all adjacent unvisited vertices of current vertex
            while (self.get_adj_unvisited_vertex(u) != -1):
                x = self.get_adj_unvisited_vertex(u)
                (self.Vertices[x]).visited = True   # mark Vertex as visited
                theQueue.enqueue(x) # enqueue current vertex

        # the Queue is emprty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False
    # ===========================================================================================
        
    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        # retrieve indices of vertices on the edge
        start = self.get_index(fromVertexLabel) 
        finish = self.get_index(toVertexLabel)
        # delete the edge in the adjacency matrix
        self.adjMat[start][finish] = 0
        self.adjMat[finish][start] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        # get index of vertex and delete it from Vertices using index
        v = self.get_index (vertexLabel)
        del self.Vertices[v]

        del self.adjMat[v]  # delete the row containing the vertex's adjEdges
        for i in range ( len(self.Vertices) ):  # delete column containing adjEdges
            del self.adjMat[i][v]
        

    def printadJ (self):    # helper function to handle printing Adj Matrix
        n = len(self.Vertices)
        for i in range(n):  # print every value in adjacency matrix, left to right, top to bottom
            for j in range(n):
                if (j == n-1): # handles extra space at end of each line
                    print( self.adjMat[i][j], end = '')
                else:
                    print( self.adjMat[i][j], end = ' ' )
            print()
    
    def printVertices (self):   # helper function to handle printing list of graph Vertices
        for vertex in self.Vertices:
            print(vertex)

# ---------------------------------------------------------------------------------------------------------------
def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        cities.add_Vertex(city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # do the depth first search
    print("Depth First Search")
    cities.dfs(start_index)
    print()

    # do the breadth first search
    print("Breadth First Search")
    cities.bfs(start_index)
    print()

    # read the vertices whose edge is to be deleted
    line = sys.stdin.readline()
    vertexEdgedelete = line.strip().split()
    vertex1 = vertexEdgedelete[0]
    vertex2 = vertexEdgedelete[1]
    # delete the edge
    print('Deletion of an edge')
    cities.delete_edge (vertex1, vertex2)
    # print the adj matrix
    print()
    print('Adjacency Matrix')
    cities.printadJ()
    print()

    # read the vertex to be deleted
    line = sys.stdin.readline()
    vertextoDel = line.strip()
    # delete the Vertex
    print('Deletion of a vertex\n')
    cities.delete_vertex(vertextoDel)
    print('List of Vertices')
    cities.printVertices()
    
    # print the adj matrix
    print()
    print('Adjacency Matrix')
    cities.printadJ()

if __name__ == "__main__":
    main()
