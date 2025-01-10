#!/usr/bin/env python3

##
# Unordered Vectors
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
    """
    A class that represents an unordered vector (or array), where elements 
    are stored without any particular order or sorting.

    Attributes:
    capacity (int): The maximum number of elements the vector can hold.
    last_position (int): The index of the last element in the vector.
    values (numpy.ndarray): The array that holds the elements of the vector.

    Methods:
    __init__(capacity): Initializes the unordered vector with a given capacity.
    print_test(): Prints all elements in the unordered vector.
    insert(value): Adds a new value to the unordered vector.
    linear_search(value): Performs a linear search to find the position of a value.
    remove(value): Removes a value from the unordered vector.
    """

    def __init__(self, capacity):
        """
        Initializes an unordered vector with a given capacity.

        Parameters:
        capacity (int): The maximum capacity of the vector.
        """
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    def print_test(self):
        """
        Prints all the elements in the unordered vector. If the vector is empty,
        it prints a message indicating that.

        Time Complexity: O(n), where n is the number of elements in the vector.
        """
        if self.last_position == -1:
            print("The vector is empty")
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])

    def insert(self, value):
        """
        Inserts a value into the unordered vector.

        If the vector has reached its maximum capacity, it prints a message 
        indicating that no more elements can be inserted.

        Parameters:
        value (int): The value to be inserted into the vector.

        Time Complexity: O(1), since insertion happens at the end of the vector.
        """
        if self.last_position == self.capacity - 1:
            print("Maximum capacity reached")
        else:
            self.last_position += 1
            self.values[self.last_position] = value

    def linear_search(self, value):
        """
        Performs a linear search to find the given value in the unordered vector.

        Parameters:
        value (int): The value to search for.

        Returns:
        int: The index of the value if found, otherwise -1.

        Time Complexity: O(n), where n is the number of elements in the vector.
        """
        for i in range(self.last_position + 1):
            if value == self.values[i]:
                return i
        return -1

    def remove(self, value):
        """
        Removes the specified value from the unordered vector if it exists.

        Parameters:
        value (int): The value to be removed from the vector.

        Returns:
        int: -1 if the value is not found, otherwise the vector is updated.

        Time Complexity: O(n), where n is the number of elements in the vector.
        """
        position = self.linear_search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]

            self.last_position -= 1


# Tests
vector = UnorderedVector(10)

# Insertion
vector.insert(2)
vector.insert(8)
vector.insert(5)
vector.insert(1)
vector.insert(6)
vector.insert(4)

vector.print_test()

print(20 * '-' )

# Search - shows the position of the element 8
print(vector.linear_search(8)) # Should return the index of 8

print(20 * '-' )

# Remove the element 8
vector.remove(8)
vector.print_test()
