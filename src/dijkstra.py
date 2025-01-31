#!/usr/bin/env python3

##
# Dijkstra's Algorithm
#
# Shortest path using Dijkstra's algorithm
#
# Problem: From Arad to Bucharest
# Source: Artificial Intelligence - Stuart Russell and Peter Norvig
##

import numpy as np
import sys

# Graph structure - adjacency matrix
vertices = {'arad': 0, 'zerind': 1, 'oradea': 2, 'sibiu': 3, 'timisoara': 4,
            'lugoj': 5, 'mehadia': 6, 'dobreta': 7, 'craiova': 8, 'rimnicu': 9,
            'fagaras': 10, 'pitesti': 11, 'bucharest': 12, 'giurgiu': 13}

# Reverse lookup for cities
cities = {0: 'arad', 1: 'zerind', 2: 'oradea', 3: 'sibiu', 4: 'timisoara',
           5: 'lugoj', 6: 'mehadia', 7: 'dobreta', 8: 'craiova', 9: 'rimnicu',
           10: 'fagaras', 11: 'pitesti', 12: 'bucharest', 13: 'giurgiu'}

# Initialize adjacency matrix for the graph
edges = np.zeros([len(cities), len(cities)], dtype=int)

# Set edge weights for the graph
edges[vertices['arad'], [vertices['zerind']]] = 75
edges[vertices['arad'], [vertices['sibiu']]] = 140
edges[vertices['arad'], [vertices['timisoara']]] = 118

edges[vertices['zerind'], [vertices['arad']]] = 75
edges[vertices['zerind'], [vertices['oradea']]] = 71

edges[vertices['oradea'], [vertices['zerind']]] = 71
edges[vertices['oradea'], [vertices['sibiu']]] = 151

edges[vertices['sibiu'], [vertices['oradea']]] = 151
edges[vertices['sibiu'], [vertices['arad']]] = 140
edges[vertices['sibiu'], [vertices['fagaras']]] = 99
edges[vertices['sibiu'], [vertices['rimnicu']]] = 80

edges[vertices['timisoara'], [vertices['arad']]] = 118
edges[vertices['timisoara'], [vertices['lugoj']]] = 111

edges[vertices['lugoj'], [vertices['timisoara']]] = 111
edges[vertices['lugoj'], [vertices['mehadia']]] = 70

edges[vertices['mehadia'], [vertices['lugoj']]] = 70
edges[vertices['mehadia'], [vertices['dobreta']]] = 75

edges[vertices['dobreta'], [vertices['mehadia']]] = 75
edges[vertices['dobreta'], [vertices['craiova']]] = 120

edges[vertices['craiova'], [vertices['dobreta']]] = 120
edges[vertices['craiova'], [vertices['pitesti']]] = 138
edges[vertices['craiova'], [vertices['rimnicu']]] = 146

edges[vertices['rimnicu'], [vertices['craiova']]] = 146
edges[vertices['rimnicu'], [vertices['sibiu']]] = 80
edges[vertices['rimnicu'], [vertices['pitesti']]] = 97

edges[vertices['fagaras'], [vertices['sibiu']]] = 99
edges[vertices['fagaras'], [vertices['bucharest']]] = 211

edges[vertices['pitesti'], [vertices['rimnicu']]] = 97
edges[vertices['pitesti'], [vertices['craiova']]] = 138
edges[vertices['pitesti'], [vertices['bucharest']]] = 101

edges[vertices['bucharest'], [vertices['fagaras']]] = 211
edges[vertices['bucharest'], [vertices['pitesti']]] = 101
edges[vertices['bucharest'], [vertices['giurgiu']]] = 90


# Dijkstra's Algorithm class
class Dijkstra:
    """
    Dijkstra's algorithm to find the shortest path in a graph.

    Attributes:
    - vertices: List of graph vertices
    - edges: Adjacency matrix representing the graph
    - start: Starting vertex for the algorithm
    """

    def __init__(self, vertices, edges, start):
        """
        Initializes the Dijkstra object with the graph and starting vertex.

        :param vertices: List of vertices in the graph
        :param edges: Adjacency matrix representing the edges of the graph
        :param start: The starting vertex for the algorithm
        """
        self.size = len(vertices)
        self.vertices = vertices
        self.graph = edges
        self.start = start

    def display_solution(self, distances):
        """
        Displays the shortest distances from the start vertex to all other vertices.

        :param distances: List of shortest distances
        """
        print(f'Shortest distances from {self.vertices[self.start]} to all other vertices:')
        for vertex in range(self.size):
            print(f'{self.vertices[vertex]}: {distances[vertex]}')

    def find_min_distance(self, distance, visited):
        """
        Finds the vertex with the minimum distance that has not been visited.

        :param distance: List of current distances
        :param visited: List of visited vertices
        :return: Index of the vertex with the minimum distance
        """
        min_distance = sys.maxsize
        for vertex in range(self.size):
            if distance[vertex] < min_distance and not visited[vertex]:
                min_distance = distance[vertex]
                min_index = vertex
        return min_index

    def run_dijkstra(self):
        """
        Runs Dijkstra's algorithm to find the shortest path from the start vertex.
        """
        distance = [sys.maxsize] * self.size
        distance[self.start] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_index = self.find_min_distance(distance, visited)
            visited[min_index] = True

            for vertex in range(self.size):
                if self.graph[min_index][vertex] > 0 and not visited[vertex] \
                        and distance[vertex] > distance[min_index] + self.graph[min_index][vertex]:
                    distance[vertex] = distance[min_index] + self.graph[min_index][vertex]

        self.display_solution(distance)


# Example with the first graph
dijkstra = Dijkstra(cities, edges, vertices['arad'])
dijkstra.run_dijkstra()

# Test with another graph
vertices2 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
vertices2_inv = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

edges2 = np.zeros([len(vertices2), len(vertices2)], dtype=int)
edges2[vertices2['A'], [vertices2['B']]] = 2
edges2[vertices2['A'], [vertices2['C']]] = 1
edges2[vertices2['B'], [vertices2['D']]] = 1
edges2[vertices2['C'], [vertices2['D']]] = 3
edges2[vertices2['C'], [vertices2['E']]] = 4
edges2[vertices2['D'], [vertices2['F']]] = 2
edges2[vertices2['E'], [vertices2['F']]] = 2

# Running Dijkstra on the second graph
dijkstra = Dijkstra(vertices2_inv, edges2, vertices2['A'])
dijkstra.run_dijkstra()
