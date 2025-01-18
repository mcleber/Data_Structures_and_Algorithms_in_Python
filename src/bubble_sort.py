#!/usr/bin/env python3

##
# Bubble Sort
##


import numpy as np

def bubble_sort(array):
    """
    Sorts an array using the bubble sort algorithm.
    
    Bubble sort repeatedly steps through the list, compares adjacent elements, 
    and swaps them if they are in the wrong order. The pass through the list 
    is repeated until the list is sorted.

    Parameters:
    array (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.
    """
    n = len(array)  # Get the length of the array

    # Loop over each element in the array
    for i in range(n):
        # Traverse the array from the start to the unsorted part
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if array[j] > array[j + 1]:
                # Swap if the element is greater than the next element
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array  # Return the sorted array

# Example usage of the bubble_sort function
sorted_array = bubble_sort(np.array([15, 34, 8, 3]))
print(sorted_array)  # Output: [ 3  8 15 34]
