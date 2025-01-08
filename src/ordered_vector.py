#!/usr/bin/env python3

##
# Ordered  Vectors
##
'''
An Ordered Vector is a data structure where the elements are stored in an 
ordered manner, typically in ascending or descending order.

Operations
- Insertion: Adding elements;
- Search: Finding an element;
- Removal: Removing an element.
'''

import numpy as np

class OrderedVector:

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

    # Insertion - O(n)
    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > value:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1

        self.values[position] = value
        self.last_position += 1

    # Linear Search - O(n)
    def linear_search(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] > value:
                return -1
            if self.values[i] == value:
                return i
            if i == self.last_position:
                return -1

    # Binary Search - O(log n)
    def binary_search(self, value):
        lower_limit = 0
        upper_limit = self.last_position

        while True:
            current_position = int((lower_limit + upper_limit) / 2)
            # Found on the first try
            if self.values[current_position] == value:
                return current_position
            # Not found
            elif lower_limit > upper_limit:
                return -1
            # Divide the limits
            else:
                # Lower limit
                if self.values[current_position] < value:
                    lower_limit = current_position + 1
                # Upper limit
                else:
                    upper_limit = current_position - 1

    # Removal - O(n)
    def delete(self, value):
        position = self.linear_search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]

            self.last_position -= 1


# Test
vector = OrderedVector(10)
vector.insert(8)
vector.insert(9)
vector.insert(4)
vector.insert(1)
vector.insert(5)
vector.insert(7)
vector.insert(11)
vector.insert(13)
vector.insert(2)

vector.print_test()

print(20 * '-' )

vector.binary_search(7)
vector.binary_search(5)
vector.binary_search(13)
vector.binary_search(20)

vector.print_test()
