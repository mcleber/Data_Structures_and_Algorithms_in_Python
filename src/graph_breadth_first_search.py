#!/usr/bin/env python3

##
# Graph with Breadth-First Search (BFS)
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


class CircularQueue:
    """
    A class to represent a circular queue with a fixed size.
    """
    def __init__(self, capacity):
        """
        Initialize the circular queue with a given capacity.
        
        :param capacity: The capacity of the queue
        """
        self.capacity = capacity
        self.start = 0
        self.end = -1
        self.size = 0

        # Changing the data type to object array for storing vertex objects
        self.values = np.empty(self.capacity, dtype=object)

    def __is_empty(self):
        """
        Check if the queue is empty.
        
        :return: True if the queue is empty, False otherwise
        """
        return self.size == 0

    def __is_full(self):
        """
        Check if the queue is full.
        
        :return: True if the queue is full, False otherwise
        """
        return self.size == self.capacity

    def enqueue(self, value):
        """
        Add an element to the queue.
        
        :param value: The value (vertex) to enqueue
        """
        if self.__is_full():
            print('Queue is full')
            return

        if self.end == self.capacity - 1:
            self.end = -1
        self.end += 1
        self.values[self.end] = value
        self.size += 1

    def dequeue(self):
        """
        Remove and return an element from the queue.
        
        :return: The dequeued value (vertex)
        """
        if self.__is_empty():
            print('Queue is empty')
            return

        temp = self.values[self.start]
        self.start += 1
        if self.start == self.capacity:
            self.start = 0
        self.size -= 1
        return temp

    def first(self):
        """
        Return the first element of the queue without removing it.
        
        :return: The first element (vertex) in the queue
        """
        if self.__is_empty():
            return None
        return self.values[self.start]


# Perform breadth-first search (BFS) for the graph
class BreadthFirstSearch:
    """
    Class to perform a breadth-first search on the graph starting from a vertex.
    """
    def __init__(self, start):
        """
        Initialize the BFS with the starting vertex.
        
        :param start: The starting vertex for BFS
        """
        self.start = start
        self.start.visited = True
        self.queue = CircularQueue(20)
        self.queue.enqueue(start)

    def search(self):
        """
        Perform BFS and print the order of visited vertices.
        """
        first = self.queue.first()
        print('-------')
        print(f'First in the queue: {first.label}')
        temp = self.queue.dequeue()
        print(f'Dequeued: {temp.label}')

        for adjacent in first.adjacent:
            print(f'Was {temp.label} visited? {adjacent.vertex.visited}')
            if not adjacent.vertex.visited:
                adjacent.vertex.visited = True
                self.queue.enqueue(adjacent.vertex)
                print(f'Enqueued: {adjacent.vertex.label}')

        if self.queue.size > 0:
            self.search()


# Run BFS starting from Arad
bfs = BreadthFirstSearch(graph.arad)
bfs.search()
