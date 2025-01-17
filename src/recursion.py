#!/usr/bin/env python3

##
# Recursion
##

def recursion(i):
    """
    This function demonstrates a simple recursive process. It prints the word "recursion" each time it is called,
    and increments the value of the parameter `i`. The recursion stops when `i` reaches 5.

    Parameters:
    i (int): The current value that is incremented in each recursive call.

    Returns:
    None: This function does not return any value, it only prints output to the console.
    """
    print("recursion")
    i += 1
    if i == 5:
        return
    else:
        recursion(i)

# Initial call with value of i
recursion(0)

# Sum values
def sum1(n):
    """
    This function calculates the sum of values from 0 to n using an iterative approach.
    It prints the sum and returns the final result.

    Parameters:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of values from 0 to n.
    """
    total = 0
    for i in range(n + 1):
        total += i

    print("Sum1 result:", total)
    return total
    
sum1(5)

def sum2(n):
    """
    This function calculates the sum of numbers from 1 to n recursively.
    It prints the final result once the recursion is complete.

    Parameters:
    n (int): The number up to which the sum is calculated.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    if n == 0:
        return 0
    else:
        return n + sum2(n - 1)

# Call the function and print the final result
result = sum2(5)
print("Sum2 result:", result)
