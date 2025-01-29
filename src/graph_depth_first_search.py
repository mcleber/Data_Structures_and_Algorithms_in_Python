#!/usr/bin/env python3

##
# Graph Depth-First Search (DFS) 
#
# Problem: From Arad to Bucharest
# Source: Artificial Intelligence - Stuart Russell and Peter Norvig
##

import numpy as np


class Vertex:
    """
    Class to represent a vertex (city) in the graph.
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
            print(f"{adj.vertex.label} - Cost: {adj.cost}")


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
        # Create vertices
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
print()


# Stack class for DFS
class Stack:
    """
    Class to represent a stack data structure.
    """
    def __init__(self, capacity):
        """
        Initialize the stack with a given capacity.
        
        :param capacity: The maximum size of the stack
        """
        self.__capacity = capacity
        self.__top = -1
        self.__values = np.empty(self.__capacity, dtype=object)

    def __is_full(self):
        """
        Check if the stack is full.
        
        :return: True if the stack is full, otherwise False
        """
        return self.__top == self.__capacity - 1

    def __is_empty(self):
        """
        Check if the stack is empty.
        
        :return: True if the stack is empty, otherwise False
        """
        return self.__top == -1

    def push(self, value):
        """
        Push a value onto the stack.
        
        :param value: The value to be pushed
        """
        if self.__is_full():
            print('The stack is full')
        else:
            self.__top += 1
            self.__values[self.__top] = value

    def pop(self):
        """
        Pop a value from the stack.
        
        :return: The popped value, or None if the stack is empty
        """
        if self.__is_empty():
            print('The stack is empty')
            return None
        else:
            temp = self.__values[self.__top]
            self.__top -= 1
            return temp

    def peek(self):
        """
        Get the top value of the stack without removing it.
        
        :return: The top value of the stack, or -1 if the stack is empty
        """
        if self.__top != -1:
            return self.__values[self.__top]
        else:
            return -1


# Perform Depth-First Search (DFS)
class DepthFirstSearch:
    """
    Class to perform depth-first search on the graph.
    """
    def __init__(self, start):
        """
        Initialize DFS with a starting vertex.
        
        :param start: The starting vertex for DFS
        """
        self.start = start
        self.start.visited = True
        self.stack = Stack(20)
        self.stack.push(start)

    def search(self):
        """
        Perform DFS search and print the traversal path.
        """
        top = self.stack.peek()
        print(f"Top: {top.label}")
        for adjacent in top.adjacent:
            print(f"Top is {top.label}. Has {adjacent.vertex.label} been visited? {adjacent.vertex.visited}")
            if not adjacent.vertex.visited:
                adjacent.vertex.visited = True
                self.stack.push(adjacent.vertex)
                print(f"Pushed {adjacent.vertex.label}")
                self.search()
                
        print(f"Popped: {self.stack.pop().label}")
        print()

# Perform DFS starting from Arad
dfs = DepthFirstSearch(graph.arad)
dfs.search()

# Display the top element of the stack after DFS
top_vertex = dfs.stack.peek()
if top_vertex != -1:
    print(f"Top after DFS: {top_vertex.label}")
else:
    print("Stack is empty")
