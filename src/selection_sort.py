#!/usr/bin/env python3

##
# Selection Sort
##

import numpy as np

def selection_sort(array):
    """
    Sorts an array using the selection sort algorithm.
    
    The selection sort algorithm repeatedly selects the smallest element 
    from the unsorted portion of the list and swaps it with the element 
    at the current position. This process continues until the entire array is sorted.

    Parameters:
    array (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.
    """
    n = len(array)  # Get the length of the array

    # Loop over each element in the array
    for i in range(n):
        id_minimum = i  # Assume the current element is the minimum

        # Traverse the unsorted portion of the array
        for j in range(i + 1, n):
            # Find the minimum element in the unsorted portion
            if array[id_minimum] > array[j]:
                id_minimum = j  # Update the index of the minimum element

        # Swap the found minimum element with the element at position i
        temp = array[i]
        array[i] = array[id_minimum]
        array[id_minimum] = temp

    return array  # Return the sorted array

# Example usage of the selection_sort function
sorted_array = selection_sort(np.array([15, 34, 8, 3]))
print("Sorted array:", sorted_array)  # Output: [ 3  8 15 34]
