#!/usr/bin/env python3

##
# Doubly Linked List
##

import numpy as np

class Node:
    """
    Represents a node in a doubly linked list.
    Each node contains a value, a reference to the next node,
    and a reference to the previous node in the list.
    """
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.next = None    # Pointer to the next node
        self.prev = None    # Pointer to the previous node

    def show_node(self):
        """Prints the value of the node."""
        print(self.value)

class DoublyLinkedList:
    """
    Represents a doubly linked list. It supports operations to insert,
    delete nodes, and traverse the list in both directions.
    """
    def __init__(self):
        self.first = None  # Pointer to the first node in the list
        self.last = None   # Pointer to the last node in the list

    def __is_empty(self):
        """Checks if the list is empty."""
        return self.first is None

    def insert_at_start(self, value):
        """
        Inserts a new node with the given value at the start of the list.
        """
        new_node = Node(value)
        if self.__is_empty():
            self.last = new_node
        else:
            self.first.prev = new_node
        new_node.next = self.first
        self.first = new_node

    def insert_at_end(self, value):
        """
        Inserts a new node with the given value at the end of the list.
        """
        new_node = Node(value)
        if self.__is_empty():
            self.first = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
        self.last = new_node

    def remove_from_start(self):
        """
        Removes and returns the node at the start of the list.
        """
        temp = self.first
        if self.first.next is None:
            self.last = None
        else:
            self.first.next.prev = None
        self.first = self.first.next
        return temp

    def remove_from_end(self):
        """
        Removes and returns the node at the end of the list.
        """
        temp = self.last
        if self.first.next is None:
            self.first = None
        else:
            self.last.prev.next = None
        self.last = self.last.prev
        return temp

    def remove_at_position(self, value):
        """
        Removes the node with the given value from the list.
        """
        current = self.first
        while current.value != value:
            current = current.next
            if current is None:
                return None
        if current == self.first:
            self.first = current.next
        else:
            current.prev.next = current.next

        if current == self.last:
            self.last = current.prev
        else:
            current.next.prev = current.prev
        return current

    def show_forward(self):
        """
        Displays the list from the first node to the last.
        """
        current = self.first
        while current is not None:
            current.show_node()
            current = current.next

    def show_backward(self):
        """
        Displays the list from the last node to the first.
        """
        current = self.last
        while current is not None:
            current.show_node()
            current = current.prev


# Tests

dll = DoublyLinkedList()
dll.insert_at_start(1)
dll.insert_at_start(2)
dll.insert_at_end(3)
dll.insert_at_end(4)

dll.show_forward()
print(20 * '-')

dll.remove_from_start()
dll.remove_from_end()
dll.remove_at_position(3)

dll.show_forward()
print(20 * '-')
