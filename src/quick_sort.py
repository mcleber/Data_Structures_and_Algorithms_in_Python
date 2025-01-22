#!/usr/bin/env python3

##
# Quick Sort
##


import numpy as np

def partition(array, start, end):
    """
    Partitions the array into two subarrays based on a pivot element.

    This function rearranges the elements of the array such that elements
    smaller than or equal to the pivot are placed before the pivot, and elements
    greater than the pivot are placed after it. The pivot is then placed at its
    correct position in the sorted array.

    Parameters:
    array (numpy.ndarray): The array to be partitioned.
    start (int): The starting index of the array segment.
    end (int): The ending index of the array segment.

    Returns:
    int: The index of the pivot element after partitioning.
    """
    pivot = array[end]  # Choose the pivot element (last element)
    i = start - 1  # Initialize the index for smaller elements

    # Traverse through the array and partition based on the pivot
    for j in range(start, end):
        if array[j] <= pivot:  # If current element is smaller than or equal to pivot
            i += 1
            array[i], array[j] = array[j], array[i]  # Swap elements
    
    # Place the pivot in the correct position
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1

def quick_sort(array, start, end):
    """
    Sorts the array using the Quick Sort algorithm.

    Quick Sort is a divide-and-conquer algorithm that works by partitioning the
    array around a pivot element. The algorithm recursively sorts the subarrays
    before and after the pivot.

    Parameters:
    array (numpy.ndarray): The array to be sorted.
    start (int): The starting index of the array segment.
    end (int): The ending index of the array segment.

    Returns:
    numpy.ndarray: The sorted array.
    """
    if start < end:
        # Partition the array and get the pivot position
        pivot_position = partition(array, start, end)

        # Recursively sort the left and right subarrays
        quick_sort(array, start, pivot_position - 1)  # Left subarray
        quick_sort(array, pivot_position + 1, end)    # Right subarray

    return array

# Example usage
array = np.array([38, 27, 43, 3, 9, 82, 10])
sorted_array = quick_sort(array, 0, len(array) - 1)
print(sorted_array)
