import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    # test odd length
    x = np.array([1,2,4,0,1])
    assert np.array_equal(algs.bubblesort(x)['sorted'],np.array([0,1,1,2,4]))
    # test even length
    x = np.array([1,2,4,0])
    assert np.array_equal(algs.bubblesort(x)['sorted'], np.array([0,1,2,4]))
    # test empty vector
    x = np.array([])
    assert np.array_equal(algs.bubblesort(x)['sorted'],np.array([]))
    # test single element vector
    x = np.array([7])
    assert np.array_equal(algs.bubblesort(x)['sorted'],np.array([7]))
    # test duplicated elements
    x = np.array([1,1,1,1])
    assert np.array_equal(algs.bubblesort(x)['sorted'],np.array([1,1,1,1]))
    # test characters
    x = np.array(['b','d','a','c'])
    assert np.array_equal(algs.bubblesort(x)['sorted'],np.array(['a','b','c','d']))
    
def test_quicksort():    
    # test odd length
    x = np.array([1,2,4,0,3])
    assert np.array_equal(algs.quicksort(x)['sorted'],np.array([0,1,2,3,4]))
    # test even length
    x = np.array([1,2,4,0])
    assert np.array_equal(algs.quicksort(x)['sorted'], np.array([0,1,2,4]))
    # test empty vector
    x = np.array([])
    assert np.array_equal(algs.quicksort(x)['sorted'],np.array([]))
    # test single element vector
    x = np.array([7])
    assert np.array_equal(algs.quicksort(x)['sorted'],np.array([7]))
    # test duplicated elements
    x = np.array([1,1,1,1])
    #assert np.array_equal(algs.quicksort(x)['sorted'],np.array([1,1,1,1]))
    # test characters
    x = np.array(['b','d','a','c'])
    assert np.array_equal(algs.quicksort(x)['sorted'],np.array(['a','b','c','d']))
    
def test_insertionsort():    
    # test odd length
    x = np.array([1,2,4,0,3])
    assert np.array_equal(algs.insertionsort(x)['sorted'],np.array([0,1,2,3,4]))
    # test even length
    x = np.array([1,2,4,0])
    assert np.array_equal(algs.insertionsort(x)['sorted'], np.array([0,1,2,4]))
    # test empty vector
    x = np.array([])
    assert np.array_equal(algs.insertionsort(x)['sorted'],np.array([]))
    # test single element vector
    x = np.array([7])
    assert np.array_equal(algs.insertionsort(x)['sorted'],np.array([7]))
    # test duplicated elements
    x = np.array([1,1,1,1])
    assert np.array_equal(algs.insertionsort(x)['sorted'],np.array([1,1,1,1]))
    # test characters
    x = np.array(['b','d','a','c'])
    assert np.array_equal(algs.insertionsort(x)['sorted'],np.array(['a','b','c','d']))    