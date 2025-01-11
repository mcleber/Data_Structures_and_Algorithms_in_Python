#!/usr/bin/env python3

##
# Deque - Double-ended Queue
##

import numpy as np

class Deque:
    """
    A double-ended queue (Deque) implementation where elements can be 
    added or removed from both ends.
    """

    def __init__(self, capacity):
        """
        Initializes the deque with a given capacity.

        Args:
            capacity (int): Maximum number of elements the deque can hold.
        """
        self.capacity = capacity
        self.start = -1
        self.end = 0
        self.number_of_elements = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __is_full(self):
        """
        Checks if the deque is full.

        Returns:
            bool: True if the deque is full, False otherwise.
        """
        return (self.start == 0 and self.end == self.capacity - 1) or (self.start == self.end + 1)

    def __is_empty(self):
        """
        Checks if the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise.
        """
        return self.start == -1

    def insert_start(self, value):
        """
        Adds an element to the front of the deque.

        Args:
            value (int): The value to be added to the front of the deque.

        If the deque is full, a message is printed.
        """
        if self.__is_full():
            print('The deque is full')
            return

        # If deque is empty
        if self.start == -1:
            self.start = 0
            self.end = 0
        # If start is at the first position
        elif self.start == 0:
            self.start = self.capacity - 1
        else:
            self.start -= 1

        self.values[self.start] = value
        self.display_deque()

    def insert_end(self, value):
        """
        Adds an element to the end of the deque.

        Args:
            value (int): The value to be added to the end of the deque.

        If the deque is full, a message is printed.
        """
        if self.__is_full():
            print('The deque is full')
            return

        # If deque is empty
        if self.start == -1:
            self.start = 0
            self.end = 0
        # If end is at the last position
        elif self.end == self.capacity - 1:
            self.end = 0
        else:
            self.end += 1

        self.values[self.end] = value
        self.display_deque()

    def remove_start(self):
        """
        Removes and returns the element from the front of the deque.

        If the deque is empty, a message is printed.
        """
        if self.__is_empty():
            print('The deque is already empty')
            return

        # If there is only one element
        if self.start == self.end:
            self.start = -1
            self.end = -1
        else:
            # Move the start pointer to the next position
            if self.start == self.capacity - 1:
                self.start = 0
            else:
                self.start += 1
        self.display_deque()

    def remove_end(self):
        """
        Removes and returns the element from the end of the deque.

        If the deque is empty, a message is printed.
        """
        if self.__is_empty():
            print('The deque is already empty')
            return

        if self.start == self.end:
            self.start = -1
            self.end = -1
        elif self.start == 0:
            self.end = self.capacity - 1
        else:
            self.end -= 1
        self.display_deque()

    def get_start(self):
        """
        Returns the element from the front of the deque without removing it.

        Returns:
            int: The front element, or None if the deque is empty.
        """
        if self.__is_empty():
            print('The deque is already empty')
            return None

        return self.values[self.start]

    def get_end(self):
        """
        Returns the element from the end of the deque without removing it.

        Returns:
            int: The end element, or None if the deque is empty.
        """
        if self.__is_empty() or self.end < 0:
            print('The deque is already empty')
            return None

        return self.values[self.end]

    def display_deque(self):
        """
        Prints the current state of the deque.
        """
        if self.__is_empty():
            print("Deque is empty")
        else:
            # Print elements from start to end
            if self.end >= self.start:
                print("Deque:", self.values[self.start:self.end + 1])
            else:
                print("Deque:", np.concatenate((self.values[self.start:], 
                self.values[:self.end + 1])))


# Tests
deque = Deque(5)
deque.insert_end(5)
deque.insert_end(10)
deque.insert_start(3)
deque.insert_start(2)
deque.insert_end(11)

# Attempt to insert when the deque is full
deque.insert_start(43)  # Should show that the deque is full

deque.remove_start()
deque.remove_end()

deque.display_deque()