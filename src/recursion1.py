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



