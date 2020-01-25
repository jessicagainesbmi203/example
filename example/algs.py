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
    conditionals = 0
    assignments = 0
    copy = np.copy(x)
    sorted = False
    while not sorted:
        swap_this_round = False
        for i in range(0,len(copy)-1,1):
            assignments = assignments + 1 # assign counter
            conditionals = conditionals + 1
            if (copy[i] > copy[i+1]):
                assignments = assignments + 1
                temp = copy[i+1]
                assignments = assignments + 1
                copy[i+1] = copy[i]
                assignments = assignments + 1
                copy[i] = temp
                swap_this_round = True
        if not swap_this_round:
            sorted = True
    assert len(copy) == len(x)
    assert set(copy) == set(x)
    assert is_sorted(copy)
    return {'sorted':copy, 'c':conditionals, 'a':assignments}
    

def quicksort(x):
    """
    Pick a pivot element from the copy and move all elements less than the pivot
    element to a left partition, and all elements greater than the pivot element
    to a right partition. Recursively quicksort the left and right sub arrays. 
    Then concatenate the left partition, pivot, and right partition in that order.
    """
    conditionals = 0
    assignments = 0
    if x.size <= 1:
        return {'sorted' : x, 'c':0, 'a':0}
    copy = np.copy(x)
    pivot = copy[0]
    left = np.array([])
    right = np.array([])
    equal = np.array([])
    for item in copy[1:]:
        conditionals = conditionals + 1
        if item > pivot:
            assignments = assignments + 1
            right = np.append(right,item)
        conditionals = conditionals + 1
        else if item < pivot:
            assignments = assignments + 1
            left = np.append(left,item)
        conditionals = conditionals + 1
        else if item == pivot:
            assignments = assignments + 1
            equal = np.append(equal,item)
    assignments = assignments + 1
    equal = np.append(equal,pivot)
    assignments = assignments + x.size
    left_data = quicksort(left)
    conditionals = conditionals + left_data['c']
    assignments = assignments + left_data['a']
    temp = np.append(left_data['sorted'],pivot)
    right_data = quicksort(right)
    conditionals = conditionals + right_data['c']
    assignments = assignments + right_data['a']
    sorted = np.append(temp,right_data['sorted'])
    assert len(sorted) == len(x)
    assert set(sorted) == set(x)
    assert is_sorted(sorted)
    return {'sorted' : sorted, 'c' : conditionals, 'a' : assignments}
    
def insertionsort(x):
    """
    Iterate through the elements of x. Add the first element to an empty array. 
    Then add each subsequent element of x to its sorted place in the new array 
    by iterating through the sorted array until reaching the first element
    greater than the x element. Place the x element just before this element in the 
    new array. If an element greater than the x element is not found, place the x 
    element at the end of the new array. Repeat for all elements of x.
    """
    conditionals = 0
    assignments = 0
    if x.size <= 1:
        return {'sorted':x, 'c':0, 'a':0}
    copy = np.copy(x)
    sorted = np.array([])
    sorted = np.append(sorted,copy[0])
    for item in copy[1:]:
        item_placed = False
        for j in range(0,len(sorted),1):
            conditionals = conditionals + 1
            if sorted[j] > item:
                assignments = assignments + 1
                sorted = np.insert(sorted,j,item)
                item_placed = True
                break
        if not item_placed:
            assignments = assignments + 1
            sorted = np.insert(sorted,len(sorted),item)
    assert len(sorted) == len(x)
    assert set(sorted) == set(x)
    assert is_sorted(sorted)
    return {'sorted':sorted, 'c':conditionals, 'a':assignments}
    
    
    
    