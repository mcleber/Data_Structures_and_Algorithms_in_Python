#!/usr/bin/env python3

##
# Insertion Sort
##


import numpy as np

def insertion_sort(array):
    """
    Sorts an array using the insertion sort algorithm.
    
    The insertion sort algorithm builds the final sorted array one item at a time.
    It repeatedly picks the next element and inserts it into its correct position 
    among the already sorted elements.

    Parameters:
    array (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.
    """
    n = len(array)  # Get the length of the array

    # Loop through each element starting from the second one
    for i in range(1, n):
        marked = array[i]  # Store the element to be inserted

        j = i - 1  # Start comparing with the previous element
        # Shift elements to the right to make space for the marked element
        while j >= 0 and marked < array[j]:
            array[j + 1] = array[j]  # Shift the element to the right
            j -= 1  # Move to the previous element

        # Insert the marked element at its correct position
        array[j + 1] = marked

    return array  # Return the sorted array

# Example usage of the insertion_sort function
sorted_array = insertion_sort(np.array([15, 34, 8, 3]))
print("Sorted array:", sorted_array)  # Output: [ 3  8 15 34]
