#!/usr/bin/env python3

##
# Unordered  Vectors
##
'''
Unordered Vectors are a type of data structure that stores elements without 
any specific order or sorting.

Operations
- Insertion: Adding elements;
- Search: Finding an element;
- Removal: Removing an element.
'''


import numpy as np

class UnorderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # Print - O(n)
    def print_test(self):
        if (self.last_position == -1):
            print("The vector is empty")
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])

    # Insertion - O(2)
    def insert(self, value):
        if (self.last_position == self.capacity -1):
            print("Maximum capacity reached")
        else:
            self.last_position += 1
            self.values[self.last_position] = value

    # Search - O(n)
    def linear_search(self, value):
        for i in range(self.last_position + 1):
            if (value == self.values[i]):
                return i
        return -1

    # Removal - O(n)
    def remove(self, value):
        position = self.linear_search(value)
        if (position == -1):
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]

            self.last_position -= 1


# Tests
vector = UnorderedVector(10)

#insertion
vector.insert(2)
vector.insert(8)
vector.insert(5)
vector.insert(1)
vector.insert(6)
vector.insert(4)

vector.print_test()

print(20 * '-' )

#search - shows the position of the element 8
print(vector.linear_search(8)) # 

print(20 * '-' )

#remove the 8
vector.remove(8)
vector.print_test()
