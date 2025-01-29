#!/usr/bin/env python3

##
# Graph 
#
# Problem: From Arad to Bucharest
# Source: Artificial Intelligence - Stuart Russell and Peter Norvig
##

class Vertex:
    """
    Class to represent a vertex in the graph.
    """
    def __init__(self, label):
        """
        Initialize a vertex with a given label.
        
        :param label: The label for the vertex (e.g., city name)
        """
        self.label = label
        self.visited = False  # Flag to mark whether the vertex has been visited
        self.adjacent = []  # List of adjacent vertices

    def add_adjacent(self, adjacent):
        """
        Add an adjacent vertex to the current vertex.
        
        :param adjacent: The adjacent vertex object
        """
        self.adjacent.append(adjacent)

    def show_adjacent(self):
        """
        Print the adjacent vertices and their costs.
        """
        for adj in self.adjacent:
            print(adj.vertex.label, adj.cost)


class Adjacent:
    """
    Class to represent an edge between two vertices with a cost.
    """
    def __init__(self, vertex, cost):
        """
        Initialize an edge between a vertex and its adjacent with a cost.
        
        :param vertex: The adjacent vertex
        :param cost: The cost to reach the adjacent vertex
        """
        self.vertex = vertex
        self.cost = cost


class Graph:
    """
    Class to represent the entire graph with all its vertices and edges.
    """
    def __init__(self):
        """
        Initialize the graph with predefined vertices and edges.
        """
        self.arad = Vertex('Arad')
        self.zerind = Vertex('Zerind')
        self.oradea = Vertex('Oradea')
        self.sibiu = Vertex('Sibiu')
        self.timisoara = Vertex('Timisoara')
        self.lugoj = Vertex('Lugoj')
        self.mehadia = Vertex('Mehadia')
        self.dobreta = Vertex('Dobreta')
        self.craiova = Vertex('Craiova')
        self.rimnicu = Vertex('Rimnicu')
        self.fagaras = Vertex('Fagaras')
        self.pitesti = Vertex('Pitesti')
        self.bucharest = Vertex('Bucharest')
        self.giurgiu = Vertex('Giurgiu')

        # Adding edges to the graph
        self.arad.add_adjacent(Adjacent(self.zerind, 75))
        self.arad.add_adjacent(Adjacent(self.sibiu, 140))
        self.arad.add_adjacent(Adjacent(self.timisoara, 118))

        self.zerind.add_adjacent(Adjacent(self.arad, 75))
        self.zerind.add_adjacent(Adjacent(self.oradea, 71))

        self.oradea.add_adjacent(Adjacent(self.zerind, 71))
        self.oradea.add_adjacent(Adjacent(self.sibiu, 151))

        self.sibiu.add_adjacent(Adjacent(self.oradea, 151))
        self.sibiu.add_adjacent(Adjacent(self.arad, 140))
        self.sibiu.add_adjacent(Adjacent(self.fagaras, 99))
        self.sibiu.add_adjacent(Adjacent(self.rimnicu, 80))

        self.timisoara.add_adjacent(Adjacent(self.arad, 118))
        self.timisoara.add_adjacent(Adjacent(self.lugoj, 111))

        self.lugoj.add_adjacent(Adjacent(self.timisoara, 111))
        self.lugoj.add_adjacent(Adjacent(self.mehadia, 70))

        self.mehadia.add_adjacent(Adjacent(self.lugoj, 70))
        self.mehadia.add_adjacent(Adjacent(self.dobreta, 75))

        self.dobreta.add_adjacent(Adjacent(self.mehadia, 75))
        self.dobreta.add_adjacent(Adjacent(self.craiova, 120))

        self.craiova.add_adjacent(Adjacent(self.dobreta, 120))
        self.craiova.add_adjacent(Adjacent(self.pitesti, 138))
        self.craiova.add_adjacent(Adjacent(self.rimnicu, 146))

        self.rimnicu.add_adjacent(Adjacent(self.craiova, 146))
        self.rimnicu.add_adjacent(Adjacent(self.sibiu, 80))
        self.rimnicu.add_adjacent(Adjacent(self.pitesti, 97))

        self.fagaras.add_adjacent(Adjacent(self.sibiu, 99))
        self.fagaras.add_adjacent(Adjacent(self.bucharest, 211))

        self.pitesti.add_adjacent(Adjacent(self.rimnicu, 97))
        self.pitesti.add_adjacent(Adjacent(self.craiova, 138))
        self.pitesti.add_adjacent(Adjacent(self.bucharest, 101))

        self.bucharest.add_adjacent(Adjacent(self.fagaras, 211))
        self.bucharest.add_adjacent(Adjacent(self.pitesti, 101))
        self.bucharest.add_adjacent(Adjacent(self.giurgiu, 90))


# Create the graph and display the adjacent vertices for Arad and Bucharest
graph = Graph()

# Show adjacent vertices of Arad
print("Adjacent cities from Arad:")
graph.arad.show_adjacent()

# Show adjacent vertices of Bucharest
print("\nAdjacent cities from Bucharest:")
graph.bucharest.show_adjacent()
