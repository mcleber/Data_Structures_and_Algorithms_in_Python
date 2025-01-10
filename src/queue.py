#!/usr/bin/env python3

##
# Circular Queue
##

import numpy as np

class CircularQueue:
    """
    A class representing a Circular Queue (FIFO structure with wrapping capability).
    
    A Circular Queue allows enqueueing and dequeueing elements in a circular manner,
    where after reaching the end of the array, it wraps around to the beginning.

    Attributes:
    capacity (int): The maximum capacity of the queue.
    start (int): The index of the first element in the queue.
    end (int): The index of the last element in the queue.
    num_elements (int): The number of elements currently in the queue.
    values (np.ndarray): An array to hold the elements of the queue.

    Methods:
    __is_empty(): Checks if the queue is empty.
    __is_full(): Checks if the queue is full.
    enqueue(value): Adds an element to the end of the queue.
    dequeue(): Removes and returns the element from the front of the queue.
    first(): Returns the element at the front of the queue without removing it.
    """

    def __init__(self, capacity):
        """
        Initializes the circular queue with a given capacity.

        Parameters:
        capacity (int): The maximum capacity of the queue.
        """
        self.capacity = capacity
        self.start = 0
        self.end = -1
        self.num_elements = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
        bool: True if the queue is empty, otherwise False.
        """
        return self.num_elements == 0

    def __is_full(self):
        """
        Checks if the queue is full.

        Returns:
        bool: True if the queue is full, otherwise False.
        """
        return self.num_elements == self.capacity

    def enqueue(self, value):
        """
        Adds an element to the end of the queue.

        If the queue is full, the element will not be added.

        Parameters:
        value (int): The value to be added to the queue.

        Time Complexity: O(1)
        """
        if self.__is_full():
            print('The queue is full')
            return

        if self.end == self.capacity - 1:
            self.end = -1  # Wrap around
        self.end += 1
        self.values[self.end] = value
        self.num_elements += 1

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        If the queue is empty, it returns None.

        Returns:
        int: The element that was dequeued, or None if the queue is empty.

        Time Complexity: O(1)
        """
        if self.__is_empty():
            print('The queue is empty')
            return None

        temp = self.values[self.start]
        self.start += 1
        if self.start == self.capacity - 1:
            self.start = 0  # Wrap around
        self.num_elements -= 1
        return temp

    def first(self):
        """
        Returns the element at the front of the queue without removing it.

        If the queue is empty, it returns -1.

        Returns:
        int: The first element of the queue, or -1 if the queue is empty.

        Time Complexity: O(1)
        """
        if self.__is_empty():
            return -1
        return self.values[self.start]

    def display(self):
            """
            Displays the elements of the queue from start to end in the correct order,
            accounting for wraparound.
            """
            if self.__is_empty():
                print("The queue is empty")
                return

            elements = []
            index = self.start
            for _ in range(self.num_elements):
                elements.append(self.values[index])
                index = (index + 1) % self.capacity  # Wrap around using modulo
            
            print("Queue elements: ", elements)


# Test

queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()  # Removes 1
queue.dequeue()  # Removes 2
queue.enqueue(6)
queue.enqueue(7)

# Display the current state of the queue
queue.display()