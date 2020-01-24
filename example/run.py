# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quicksort, bubblesort, insertionsort

def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)

    #x = np.random.rand(10)
    x = np.array(['b','c','a','d'])
    print("Unsorted input: ", x)
    y = np.array(['b','c','a','d'])
    z = np.array(['b','c','a','d'])
    print("Bubble sort output: ", bubblesort(x))
    print("Quick sort output: ", quicksort(y))
    print("Insertion sort output: ", insertionsort(z))
