#!/usr/bin/env python3

##
# Stacks
##

import numpy as np

class Stack:
    """
    A class that represents a stack data structure.

    A stack follows the Last-In-First-Out (LIFO) principle, where elements 
    are added to and removed from the top of the stack.

    Attributes:
    capacity (int): The maximum capacity of the stack.
    top (int): The index of the top element in the stack.
    values (np.chararray): An array that holds the elements of the stack.

    Methods:
    __stack_full(): Checks if the stack is full.
    stack_empty(): Checks if the stack is empty.
    push(value): Adds an element to the top of the stack.
    pop(): Removes and returns the top element from the stack.
    peek(): Returns the top element of the stack without removing it.
    """

    def __init__(self, capacity):
        """
        Initializes a new stack with a given capacity.

        Parameters:
        capacity (int): The maximum capacity of the stack.
        """
        self.capacity = capacity
        self.top = -1
        # Array to hold elements (e.g., '(')
        self.values = np.chararray(self.capacity, unicode=True)

    def __stack_full(self):
        """
        Checks if the stack is full.

        Returns:
        bool: True if the stack is full, otherwise False.
        """
        return self.top == self.capacity - 1

    def stack_empty(self):  
        """
        Checks if the stack is empty.

        Returns:
        bool: True if the stack is empty, otherwise False.
        """
        return self.top == -1

    def push(self, value):
        """
        Pushes an element onto the stack.

        Adds the provided element to the top of the stack if there is space.

        Parameters:
        value (str): The element to be added to the stack.

        Time Complexity: O(1), since insertion occurs at the top of the stack.
        """
        if self.__stack_full():
            print('The stack is full')
        else:
            self.top += 1
            self.values[self.top] = value

    def pop(self):
        """
        Pops an element from the stack.

        Removes and returns the element at the top of the stack.

        Returns:
        str: The popped element if the stack is not empty, otherwise -1.

        Time Complexity: O(1), since the top element is removed directly.
        """
        if self.stack_empty():
            print('The stack is empty')
            return -1
        else:
            value = self.values[self.top]
            self.top -= 1
            return value

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        This allows checking the element at the top of the stack without
        modifying the stack itself.

        Returns:
        str: The top element of the stack if it is not empty, otherwise -1.

        Time Complexity: O(1), since the top element is accessed directly.
        """
        if self.top != -1:
            return self.values[self.top]
        else:
            return -1


# Test

# Example expressions to check for balanced brackets
# c[d]
# a{b[c]d}e
# a{b(c]d}e
# a[b{c}d]e}
# a{b(c)

expression = str(input('Enter an expression: '))
stack = Stack(len(expression))

for i in range(len(expression)):
    char = expression[i]
    if char == '{' or char == '[' or char == '(':
        stack.push(char)
    elif char == '}' or char == ']' or char == ')':
        if not stack.stack_empty():  # Now this works since the method is public
            popped_char = str(stack.pop())
            if (char == '}' and popped_char != '{') or (char == ']' and popped_char != '[') or (char == ')' and popped_char != '('):
                print(f'Error: {char} at position {i}')
                break
        else:
            print(f'Error: {char} at position {i}')
if not stack.stack_empty():  # Also using the public method here
    print('Error!')
