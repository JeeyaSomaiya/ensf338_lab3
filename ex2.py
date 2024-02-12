import sys 
sys.setrecursionlimit(20000)

import timeit
from matplotlib import pyplot as plt
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

def get_avg(func, data):
    '''
    Get average time for 100 runs
    '''
    total_time = 0
    for i in range(100):
        total_time += timeit.timeit(lambda: func(data))
    return total_time / 100

inputSizes = [2, 5, 10, 25, 50, 75, 100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500]

for size in inputSizes:
    quicksort_best = [sortedValue(size)[: size // 2] + sortedValue(size)[::-1][size //2:]]
    quicksort_avg = [randomValue(size)]
    # quicksort_worst = [[max(arr) for i in range(size)]]
    bubblesort_best = [sortedValue(size)]
    bubblesort_avg = [randomValue(size)]
    bubblesort_worst = [reversedValue(size)]

    # get execution time
    bubblesort_best_time = [get_avg(bubble_sort, arr) for arr in bubblesort_best]
    bubblesort_avg_time = [get_avg(bubble_sort, arr) for arr in bubblesort_avg]
    bubblesort_worst_time = [get_avg(bubble_sort, arr) for arr in bubblesort_worst]

    quicksort_best_time = [get_avg(quicksort, arr) for arr in quicksort_best]
    quicksort_avg_time = [get_avg(quicksort, arr) for arr in quicksort_avg]
    # quicksort_worst_time = [get_avg(quicksort, arr) for arr in quicksort_worst]

    plt.figure(figsize=(10, 6))

    plt.plot(inputSizes, bubblesort_best_time, label="Bubble Sort (best)", marker="o")
    plt.plot(inputSizes, bubblesort_avg_time, label="Bubble Sort (avg)", marker="s")
    plt.plot(inputSizes, bubblesort_worst_time, label="Bubble Sort (worst)", marker="^")
    
    plt.plot(inputSizes, quicksort_best_time, label="Quick Sort (best)", marker="o")
    plt.plot(inputSizes, quicksort_avg_time, label="Quick Sort (avg)", marker="s")
    # plt.plot(inputSizes, quicksort_worst_time, label="Quick Sort (worst)", marker="^")

    plt.xlabel("Input size")
    plt.ylabel("Execution time")
    plt.legend()
    plt.grid(True)

    plt.show()