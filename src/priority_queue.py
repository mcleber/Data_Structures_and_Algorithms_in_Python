#!/usr/bin/env python3

##
# Priority Queue
##

import numpy as np

class PriorityQueue:
    """
    A Priority Queue implementation using an array where elements are inserted 
    in descending order of priority (highest priority first).
    """

    def __init__(self, capacity):
        """
        Initializes the priority queue with a given capacity.

        Args:
            capacity (int): Maximum number of elements the queue can hold.
        """
        self.capacity = capacity
        self.number_of_elements = 0
        self.values = np.empty(self.capacity, dtype=int)

    def __is_empty(self):
        """
        Checks if the priority queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.number_of_elements == 0

    def __is_full(self):
        """
        Checks if the priority queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return self.number_of_elements == self.capacity

    def enqueue(self, value):
        """
        Adds an element to the priority queue while maintaining order by priority.

        Args:
            value (int): The value to be added to the queue.

        If the queue is full, a message is printed.
        """
        if self.__is_full():
            print('The queue is full')
            return

        if self.number_of_elements == 0:
            self.values[self.number_of_elements] = value
            self.number_of_elements += 1
        else:
            x = self.number_of_elements - 1
            while x >= 0:
                if value > self.values[x]:
                    self.values[x + 1] = self.values[x]
                else:
                    break
                x -= 1
            self.values[x + 1] = value
            self.number_of_elements += 1

        self.display_queue()


    def dequeue(self):
        """
        Removes and returns the element with the highest priority (last in the array).

        Returns:
            int: The element with the highest priority.

        If the queue is empty, a message is printed.
        """
        if self.__is_empty():
            print('The queue is empty')
            return

        value = self.values[self.number_of_elements - 1]
        self.number_of_elements -= 1
        print(f'Dequeued: {value}')
        self.display_queue()
        return value

    def first(self):
        """
        Returns the element with the highest priority without removing it.

        Returns:
            int: The element with the highest priority, or -1 if the queue is empty.
        """
        if self.__is_empty():
            return -1
        return self.values[self.number_of_elements - 1]

    def display_queue(self):
        """
        Prints the current state of the priority queue.
        """
        if self.__is_empty():
            print("Queue is empty")
        else:
            print("Queue:", self.values[:self.number_of_elements])


# Tests
queue = PriorityQueue(5)
queue.enqueue(30)
queue.enqueue(50)
queue.enqueue(10)
queue.enqueue(40)
queue.enqueue(20)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(5)

# Display the current state of the queue
queue.display_queue()
