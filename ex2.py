
import timeit
from matplotlib import pyplot as plt
import numpy as np
import random

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

def quicksort(arr):
   '''
    Quick Sort analysis
    worst: largest/smallest element chosen for pivot O(n^2)
    best: pivots always create equal sized subarrays O(nlog(n))
    avg: O(nlog(n))
    '''
   if len(arr) <= 1:
      return arr
   pivot = arr[len(arr) // 2]
   left = [x for x in arr if x < pivot]
   middle = [x for x in arr if x == pivot]
   right = [x for x in arr if x > pivot]
   return quicksort(left) + middle + quicksort(right)

def quicksort_worst_func(arr):
   '''
   quicksort in worst case
   '''
   if len(arr) <= 1:
      return arr
   pivot = arr[0]
   left = [x for x in arr[1:] if x <= pivot]
   right = [x for x in arr[1:] if x > pivot]
   return quicksort(left) + [pivot] + quicksort(right)

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
    
    total_time = timeit.timeit(lambda: func(data), number=100)

    time_avg = total_time / 100
    return time_avg

inputSizes = [2, 5, 7, 10, 15, 20, 25, 30, 40, 50, 75, 100, 110, 120, 135, 150, 175, 200, 225, 250]

qs_best_times = []
qs_worst_times = []
qs_avg_times = []

bs_best_times = []
bs_worst_times = []
bs_avg_times = []

for size in inputSizes:
    quicksort_best = randomValue(size)
    quicksort_avg = randomValue(size)
    quicksort_worst = randomValue(size)
    bubblesort_best = sortedValue(size)
    bubblesort_avg = randomValue(size)
    bubblesort_worst = reversedValue(size)

    # get execution time
    bubblesort_best_time = get_avg(bubble_sort, bubblesort_best)
    bubblesort_avg_time = get_avg(bubble_sort, bubblesort_avg)
    bubblesort_worst_time = get_avg(bubble_sort, bubblesort_worst)

    quicksort_best_time = get_avg(quicksort, quicksort_best)
    quicksort_avg_time = get_avg(quicksort, quicksort_avg)
    quicksort_worst_time = get_avg(quicksort_worst_func, quicksort_worst)

    qs_avg_times.append(quicksort_avg_time)
    qs_best_times.append(quicksort_best_time)
    qs_worst_times.append(quicksort_worst_time)
    bs_avg_times.append(bubblesort_avg_time)
    bs_best_times.append(bubblesort_best_time)
    bs_worst_times.append(bubblesort_worst_time)

# plotting and analyzing performnace
figure, axis = plt.subplots(nrows=1, ncols=3, figsize=[15, 5])

# best case
axis[0].plot(inputSizes, qs_best_times, label="quicksort")
axis[0].plot(inputSizes, bs_best_times, label="bubble sort")
axis[0].set_title("Best case")
axis[0].legend()

# average case
axis[1].plot(inputSizes, qs_avg_times, label="quicksort")
axis[1].plot(inputSizes, bs_avg_times, label="bubble sort")
axis[1].set_title("Average case")
axis[1].legend()

# worst case
axis[2].plot(inputSizes, qs_worst_times, label="quicksort")
axis[2].plot(inputSizes, bs_worst_times, label="bubble sort")
axis[2].set_title("Worst case")
axis[2].legend()

plt.show()