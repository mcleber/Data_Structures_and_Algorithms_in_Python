#!/usr/bin/env python3

##
# Singly Linked List
##

import numpy as np

class Node:
    """
    A class representing a node in a linked list.

    Attributes:
    value (int): The value stored in the node.
    next (Node): A reference to the next node in the list.
    """
    def __init__(self, value):
        """
        Initializes the node with a given value and sets the next reference to None.

        Args:
        value (int): The value to be stored in the node.
        """
        self.value = value
        self.next = None

    def show_node(self):
        """
        Prints the value of the node.
        """
        print(self.value)


class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
    first (Node): The first node in the linked list.
    """
    def __init__(self):
        """
        Initializes an empty linked list with no nodes.
        """
        self.first = None

    def insert_start(self, value):
        """
        Inserts a new node with the given value at the start of the list.

        Args:
        value (int): The value to be inserted at the start of the list.
        """
        new_node = Node(value)
        new_node.next = self.first
        self.first = new_node

    def display(self):
        """
        Displays the values of all nodes in the list.
        If the list is empty, it prints a message indicating so.
        """
        if self.first is None:
            print('The list is empty')
            return None

        current = self.first
        while current is not None:
            current.show_node()
            current = current.next

    def search(self, value):
        """
        Searches for a node with the given value in the list.

        Args:
        value (int): The value to search for.

        Returns:
        Node: The node containing the value, or None if not found.
        """
        if self.first is None:
            print('The list is empty')
            return None

        current = self.first
        while current.value != value:
            if current.next is None:
                return None
            else:
                current = current.next
        return current

    def delete_start(self):
        """
        Deletes the first node from the list.

        Returns:
        Node: The node that was deleted, or None if the list is empty.
        """
        if self.first is None:
            print('The list is empty')
            return None

        temp = self.first
        self.first = self.first.next
        return temp

    def delete_position(self, value):
        """
        Deletes a node with the given value from the list.

        Args:
        value (int): The value of the node to delete.

        Returns:
        Node: The node that was deleted, or None if not found.
        """
        if self.first is None:
            print('The list is empty')
            return None

        current = self.first
        previous = self.first
        while current.value != value:
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next

        return current


# Tests
linked_list = LinkedList()
linked_list.insert_start(1)
linked_list.insert_start(2)
linked_list.insert_start(3)
linked_list.insert_start(4)
linked_list.insert_start(5)

linked_list.display()

print(20 * '-')

search_result = linked_list.search(3)

linked_list.delete_start()
linked_list.delete_position(4)
linked_list.delete_position(2)

linked_list.display()





