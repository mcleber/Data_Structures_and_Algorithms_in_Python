#!/usr/bin/env python3

##
# Ordered Vectors
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
    """
    A class that represents an ordered vector (or array), where the elements
    are stored in sorted order.

    Attributes:
    capacity (int): The maximum number of elements the vector can hold.
    last_position (int): The index of the last element in the vector.
    values (numpy.ndarray): The array that holds the elements of the vector.

    Methods:
    __init__(capacity): Initializes the ordered vector with a given capacity.
    print_test(): Prints all elements in the vector.
    insert(value): Inserts a value into the vector in sorted order.
    linear_search(value): Performs a linear search for a value in the vector.
    binary_search(value): Performs a binary search for a value in the vector.
    delete(value): Removes a value from the vector.
    """

    def __init__(self, capacity):
        """
        Initializes an ordered vector with a given capacity.

        Parameters:
        capacity (int): The maximum capacity of the vector.
        """
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    def print_test(self):
        """
        Prints all the elements in the ordered vector. If the vector is empty,
        it will print a message indicating that.

        Time Complexity: O(n), where n is the number of elements in the vector.
        """
        if self.last_position == -1:
            print("The vector is empty")
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])

    def insert(self, value):
        """
        Inserts a value into the ordered vector, maintaining the sorted order.

        If the vector has reached its capacity, it prints a message and stops.

        Parameters:
        value (int): The value to be inserted into the vector.

        Time Complexity: O(n), where n is the number of elements in the vector.
        """
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

    def linear_search(self, value):
        """
        Performs a linear search to find the given value in the vector.

        Parameters:
        value (int): The value to search for.

        Returns:
        int: The index of the value if found, otherwise -1.

        Time Complexity: O(n), where n is the number of elements in the vector.
        """
        for i in range(self.last_position + 1):
            if self.values[i] > value:
                return -1
            if self.values[i] == value:
                return i
            if i == self.last_position:
                return -1

    def binary_search(self, value):
        """
        Performs a binary search to find the given value in the sorted vector.

        Parameters:
        value (int): The value to search for.

        Returns:
        int: The index of the value if found, otherwise -1.

        Time Complexity: O(log n), where n is the number of elements in the vector.
        """
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

    def delete(self, value):
        """
        Removes a value from the vector, if it exists.

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
