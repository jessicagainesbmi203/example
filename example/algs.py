import numpy as np
import collections

def is_sorted(x):
    for i in range(0,x.size-1,1):
        if x[i] > x[i+1]:
            return False
    return True

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    Make a copy of x. Iterate through the elements of x, comparing each element
    to the element ahead of it. If the first element is greater than the second,
    swap the elements. Repeat the iteration until no swaps occur in an iteration.`
    """
    copy = x
    sorted = False
    while not sorted:
        swap_this_round = False
        for i in range(0,len(copy)-1,1):
            if (copy[i] > copy[i+1]):
                temp = copy[i+1]
                copy[i+1] = copy[i]
                copy[i] = temp
                swap_this_round = True
        if not swap_this_round:
            sorted = True
    assert len(copy) == len(x)
    assert set(copy) == set(x)
    assert is_sorted(copy)
    return copy
    

def quicksort(x):
    """
    Pick a pivot element from the copy and move all elements less than the pivot
    element to a left partition, and all elements greater than the pivot element
    to a right partition. Recursively quicksort the left and right sub arrays. 
    Then concatenate the left partition, pivot, and right partition in that order.
    """
    pivot = list()
    pivot.append(x[0])
    left = list()
    right = list()
    for item in x[1:]:
        if item > pivot[0]:
            right.append(item)
        if item < pivot[0]:
            left.append(item)
        if item == pivot[0]:
            pivot.append(item)
    left.extend(pivot)
    left.extend(right)
    sorted = np.array(left)
    assert len(sorted) == len(x)
    assert set(sorted) == set(x)
    assert is_sorted(sorted)
    return sorted
    
def insertionsort(x):
    """
    Iterate through the elements of x. Add the first element to an empty array. 
    Then add each subsequent element of x to its sorted place in the new array 
    by iterating through the sorted array until reaching the first element
    greater than the x element. Place the x element just before this element in the 
    new array. Repeat for all elements of x.
    """
    sorted = np.array(x[0])
    for item in x[1:]:
        for j in range(0,sorted.size,1):
    assert len(sorted) == len(x)
    assert set(sorted) == set(x)
    assert is_sorted(sorted)
    return x
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
