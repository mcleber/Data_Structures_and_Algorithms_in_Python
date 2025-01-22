#!/usr/bin/env python3

##
# Shell Sort
##

import numpy as np

def shell_sort(array):
    """
    Sorts an array using the Shell Sort algorithm.

    Shell Sort is an in-place comparison-based sorting algorithm
    that generalizes insertion sort to allow the exchange of items 
    that are far apart. The idea is to arrange the list of elements 
    so that, starting anywhere, taking every `gap`-th element produces 
    a sorted list. The algorithm gradually reduces the gap between 
    elements to be compared.

    Parameters:
    array (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.
    """
    
    # Start with a gap size of half the length of the array
    gap = len(array) // 2

    # Continue reducing the gap until it becomes zero
    while gap > 0:
        # Perform a modified insertion sort for each gap
        for i in range(gap, len(array)):
            temp = array[i]  # Store the current element
            j = i  # Initialize index j to the current index i

            # Shift elements that are greater than temp to the right
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            # Place the temp element in the correct position
            array[j] = temp
        
        # Reduce the gap for the next iteration
        gap //= 2

    return array

# Example usage
sorted_array = shell_sort(np.array([8, 5, 1, 4, 2, 3]))
print(sorted_array)
