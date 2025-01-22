#!/usr/bin/env python3

##
# Merge Sort
##
import numpy as np

def merge_sort(array):
    """
    Sorts an array using the Merge Sort algorithm.

    Merge Sort is a divide-and-conquer algorithm that splits the array
    into smaller subarrays, sorts them recursively, and then merges 
    the sorted subarrays back together.

    Parameters:
    array (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.
    """
    
    # If the array has more than one element, split and recursively sort
    if len(array) > 1:
        mid = len(array) // 2  # Find the middle index
        left = array[:mid].copy()  # Left half of the array
        right = array[mid:].copy()  # Right half of the array

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0  # Initialize indices for left, right, and the original array

        # Merge the left and right subarrays into the original array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Add remaining elements from left, if any
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # Add remaining elements from right, if any
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array

# Example usage
sorted_array = merge_sort(np.array([38, 27, 43, 3, 9, 82, 10]))
print(sorted_array)
