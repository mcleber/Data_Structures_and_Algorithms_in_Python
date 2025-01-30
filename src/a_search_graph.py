#!/usr/bin/env python3

##
# A* Search Graph
#
# Problem: From Arad to Bucharest
# Source: Artificial Intelligence - Stuart Russell and Peter Norvig
##

import numpy as np

class Vertex:
    """
    A class representing a vertex (node) in the graph.
    
    Attributes:
    label (str): The label of the vertex.
    visited (bool): Whether the vertex has been visited in the search.
    distance_to_goal (int): Estimated distance from this vertex to the goal (heuristic).
    adjacencies (list): List of adjacent vertices and their corresponding costs.
    g_cost (int): The actual cost from the start node to this vertex.
    parent (Vertex): The parent vertex for path reconstruction.
    """
    
    def __init__(self, label, distance_to_goal):
        self.label = label
        self.visited = False
        self.distance_to_goal = distance_to_goal  # Heuristic (h(n))
        self.adjacencies = []
        self.g_cost = float('inf')  # Actual cost from the start node (g(n))
        self.parent = None  # Parent vertex for path reconstruction

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
            print(f'{adj.vertex.label} - Cost: {adj.cost}')

class Adjacent:
    """
    A class representing an edge between two vertices.
    
    Attributes:
    vertex (Vertex): The adjacent vertex.
    cost (int): The cost to move from the current vertex to the adjacent vertex.
    total_cost (int): The sum of the edge cost and the heuristic for the adjacent vertex (A*).
    """
    
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost
        self.total_cost = vertex.distance_to_goal + self.cost  # A* heuristic + cost

class Graph:
    """
    A class representing the entire graph with vertices and their adjacencies.
    """
    
    # Define vertices
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

    # Add adjacencies
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

# Create the graph object
graph = Graph()

class OrderedList:
    """
    A class representing a sorted list of adjacent vertices for A* search.

    Attributes:
    capacity (int): Maximum capacity of the list.
    values (list): A list of adjacent vertices sorted by total cost.
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=object)

    def insert(self, adjacent):
        """
        Inserts an adjacent vertex into the sorted list based on its total A* cost.

        Args:
        adjacent (Adjacent): The adjacent vertex to insert.
        """
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
            return
        
        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i].total_cost > adjacent.total_cost:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1
        self.values[position] = adjacent
        self.last_position += 1

    def print_list(self):
        """
        Prints the list of adjacent vertices with their associated costs.
        """
        if self.last_position == -1:
            print('The list is empty')
        else:
            for i in range(self.last_position + 1):
                print(f'{i} - {self.values[i].vertex.label} - Cost: {self.values[i].cost} - '
                      f'Heuristic: {self.values[i].vertex.distance_to_goal} - Total: {self.values[i].total_cost}')

class AStarSearch:
    """
    A* Search Algorithm to find the path from the start node to the goal node.
    
    Attributes:
    goal (Vertex): The goal vertex.
    found (bool): Whether the goal has been found.
    """
    
    def __init__(self, goal):
        self.goal = goal
        self.found = False

    def search(self, current):
        """
        Perform the A* search to find the goal.

        Args:
        current (Vertex): The current vertex in the search.
        """
        print('----------')
        print(f'Current: {current.label}')
        current.visited = True

        if current == self.goal:
            self.found = True
            print('Goal found!')
        else:
            ordered_list = OrderedList(len(current.adjacencies))
            for adjacent in current.adjacencies:
                if not adjacent.vertex.visited:
                    adjacent.vertex.visited = True
                    ordered_list.insert(adjacent)
            ordered_list.print_list()

            if ordered_list.values[0] is not None:
                self.search(ordered_list.values[0].vertex)

# Create the A* search object and start the search
astar_search = AStarSearch(graph.bucharest)
astar_search.search(graph.arad)
