import sys 
sys.setrecursionlimit(20000)

import timeit
from matplotlib import pyplot as pyplot
import numpy as np
from numpy import random

def bubble_sort(arr):
    '''
    Bubble sort analysis
    O(n^2) in all cases
    Worst case: reverse order
    Best: already sort
    Avg: random order
    '''
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high 
    done = False 
    while not done: 
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left: 
            right = right - 1
        if right < left:
            done = True 
        else: 
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quicksort(arr, low, high):
    '''
    Quick Sort analysis
    worst: largest/smallest element chosen for pivot O(n^2)
    best: pivots always create equal sized subarrays O(nlog(n))
    avg: O(nlog(n))
    '''
    if low < high: 
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

def randomValue(size):
    '''
    Generate an array of certain size with random values
    '''
    arr = []
    for i in range(size):
        arr.append(random.randint(0, size))

    return arr

def sortedValue(size):
    '''
    Generate an array of certain size with sorted values
    '''
    arr = [i for i in range(size)]

    return arr

def reversedValue(size):
    '''
    Generate an array of certain size with reverse sorted values
    '''
    arr = sorted([i for i in range(size)], reverse=True)

    return arr

inputSizes = [2, 5, 10, 25, 50, 75, 100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]

quicksortTimes = []
bubblesortTimes = []

for sizes in inputSizes:
    # best case scenario testing
    bubblearr = sortedValue(sizes)
    bubbleBest = timeit.timeit(bubble_sort(bubblearr))

    bubblesortTimes.append(bubbleBest)