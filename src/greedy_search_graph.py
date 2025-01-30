#!/usr/bin/env python3

##
# Greedy Search Graph
#
# Problem: From Arad to Bucharest
# Source: Artificial Intelligence - Stuart Russell and Peter Norvig
##


import numpy as np

class Vertex:
    """
    A class representing a vertex (node) in the graph.
    
    Attributes:
    rotulo (str): The label of the vertex.
    visited (bool): Whether the vertex has been visited in the search.
    distance_to_goal (int): Estimated distance from this vertex to the goal.
    adjacencies (list): List of adjacent vertices and their corresponding costs.
    """
    
    def __init__(self, label, distance_to_goal):
        self.label = label
        self.visited = False
        self.distance_to_goal = distance_to_goal
        self.adjacencies = []

    def add_adjacent(self, adjacent):
        """
        Adds an adjacent vertex to the current vertex.

        Args:
        adjacent (Adjacent): The adjacent vertex and its cost.
        """
        self.adjacencies.append(adjacent)

    def show_adjacencies(self):
        """
        Displays all adjacent vertices with their associated costs.
        """
        for adj in self.adjacencies:
            print(adj.vertex.label, adj.cost)


class Adjacent:
    """
    A class representing an edge between two vertices.
    
    Attributes:
    vertex (Vertex): The adjacent vertex.
    cost (int): The cost to move from the current vertex to the adjacent vertex.
    """
    
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost


class Graph:
    """
    A class representing the entire graph.
    It initializes the vertices and their adjacencies as per the problem scenario.
    """
    
    arad = Vertex('Arad', 366)
    zerind = Vertex('Zerind', 374)
    oradea = Vertex('Oradea', 380)
    sibiu = Vertex('Sibiu', 253)
    timisoara = Vertex('Timisoara', 329)
    lugoj = Vertex('Lugoj', 244)
    mehadia = Vertex('Mehadia', 241)
    dobreta = Vertex('Dobreta', 242)
    craiova = Vertex('Craiova', 160)
    rimnicu = Vertex('Rimnicu', 193)
    fagaras = Vertex('Fagaras', 178)
    pitesti = Vertex('Pitesti', 98)
    bucharest = Vertex('Bucharest', 0)
    giurgiu = Vertex('Giurgiu', 77)

    # Adding adjacencies (edges with costs)
    arad.add_adjacent(Adjacent(zerind, 75))
    arad.add_adjacent(Adjacent(sibiu, 140))
    arad.add_adjacent(Adjacent(timisoara, 118))

    zerind.add_adjacent(Adjacent(arad, 75))
    zerind.add_adjacent(Adjacent(oradea, 71))

    oradea.add_adjacent(Adjacent(zerind, 71))
    oradea.add_adjacent(Adjacent(sibiu, 151))

    sibiu.add_adjacent(Adjacent(oradea, 151))
    sibiu.add_adjacent(Adjacent(arad, 140))
    sibiu.add_adjacent(Adjacent(fagaras, 99))
    sibiu.add_adjacent(Adjacent(rimnicu, 80))

    timisoara.add_adjacent(Adjacent(arad, 118))
    timisoara.add_adjacent(Adjacent(lugoj, 111))

    lugoj.add_adjacent(Adjacent(timisoara, 111))
    lugoj.add_adjacent(Adjacent(mehadia, 70))

    mehadia.add_adjacent(Adjacent(lugoj, 70))
    mehadia.add_adjacent(Adjacent(dobreta, 75))

    dobreta.add_adjacent(Adjacent(mehadia, 75))
    dobreta.add_adjacent(Adjacent(craiova, 120))

    craiova.add_adjacent(Adjacent(dobreta, 120))
    craiova.add_adjacent(Adjacent(pitesti, 138))
    craiova.add_adjacent(Adjacent(rimnicu, 146))

    rimnicu.add_adjacent(Adjacent(craiova, 146))
    rimnicu.add_adjacent(Adjacent(sibiu, 80))
    rimnicu.add_adjacent(Adjacent(pitesti, 97))

    fagaras.add_adjacent(Adjacent(sibiu, 99))
    fagaras.add_adjacent(Adjacent(bucharest, 211))

    pitesti.add_adjacent(Adjacent(rimnicu, 97))
    pitesti.add_adjacent(Adjacent(craiova, 138))
    pitesti.add_adjacent(Adjacent(bucharest, 101))

    bucharest.add_adjacent(Adjacent(fagaras, 211))
    bucharest.add_adjacent(Adjacent(pitesti, 101))
    bucharest.add_adjacent(Adjacent(giurgiu, 90))


class SortedVector:
    """
    A class representing a sorted vector for ordering vertices by their distance to the goal.
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=object)

    def insert(self, vertex):
        """
        Inserts a vertex into the sorted vector based on its distance to the goal.

        Args:
        vertex (Vertex): The vertex to be inserted.
        """
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
            return
        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i].distance_to_goal > vertex.distance_to_goal:
                break
            if i == self.last_position:
                position = i + 1
        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1
        self.values[position] = vertex
        self.last_position += 1

    def print(self):
        """
        Prints the contents of the sorted vector.
        """
        if self.last_position == -1:
            print('The vector is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i].label, ' - ', self.values[i].distance_to_goal)


class GreedySearch:
    """
    A class implementing the Greedy Search algorithm.
    """
    
    def __init__(self, goal):
        """
        Initializes the search with the goal vertex.

        Args:
        goal (Vertex): The goal vertex to reach.
        """
        self.goal = goal
        self.found = False

    def search(self, current):
        """
        Performs the greedy search starting from the current vertex.
        
        Args:
        current (Vertex): The current vertex in the search.
        """
        print('-------')
        print('Current: {}'.format(current.label))
        current.visited = True

        if current == self.goal:
            self.found = True
        else:
            sorted_vector = SortedVector(len(current.adjacencies))
            for adjacent in current.adjacencies:
                if not adjacent.vertex.visited:
                    adjacent.vertex.visited = True
                    sorted_vector.insert(adjacent.vertex)
            sorted_vector.print()

            if sorted_vector.values[0] is not None:
                self.search(sorted_vector.values[0])


# Initialize graph and run greedy search
graph = Graph()

sorted_vector = SortedVector(5)
sorted_vector.insert(graph.arad)
sorted_vector.insert(graph.craiova)
sorted_vector.insert(graph.bucharest)
sorted_vector.insert(graph.dobreta)

sorted_vector.print()
print()

sorted_vector.insert(graph.lugoj)
sorted_vector.print()
print()

# Start greedy search from 'Arad' to 'Bucharest'
greedy_search = GreedySearch(graph.bucharest)
greedy_search.search(graph.arad)
