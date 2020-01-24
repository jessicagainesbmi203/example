# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quicksort, bubblesort, insertionsort
import pandas as pd
import matplotlib.pyplot as plt

def run_stuff():
    """
    This function is called in `__main__.py`
    """
    plt.clf()
    print("This is `run()` from ", __file__)

    x = np.random.rand(10)
    print("Unsorted input: ", x)
    print("Bubble sort output: ", bubblesort(x)['sorted'])
    print(x)
    print("Quick sort output: ", quicksort(x)['sorted'])
    print(x)
    print("Insertion sort output: ", insertionsort(x)['sorted'])
    print(x)
    
    
    
    
    
    
    
    
    
