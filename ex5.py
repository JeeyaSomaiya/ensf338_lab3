import matplotlib.pyplot as plt
import numpy as np
import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def binary_search(arr, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i - 1)
        arr = arr[:j] + [key] + arr[j:i] + arr[i + 1:]
    return arr

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(algorithm, input_size):
    arr = generate_random_array(input_size)
    start_time = timeit.default_timer()
    if algorithm == 'insertion':
        insertion_sort(arr)
    elif algorithm == 'binary':
        binary_insertion_sort(arr)
    end_time = timeit.default_timer()
    return end_time - start_time


sizes = [100, 500, 1000, 2000, 5000]  
for size in sizes:
    insertion_time = measure_time('insertion', size)
    binary_time = measure_time('binary', size)
    print(f"Input size: {size}\tInsertion Sort Time: {insertion_time:.6f} seconds\tBinary Insertion Sort Time: {binary_time:.6f} seconds")

insertion_times = []
binary_times = []
for size in sizes:
    insertion_time = measure_time('insertion', size)
    binary_time = measure_time('binary', size)
    insertion_times.append(insertion_time)
    binary_times.append(binary_time)

plt.figure(figsize=(10, 6))

plt.scatter(sizes, insertion_times, color='blue', label='Insertion Sort')
plt.scatter(sizes, binary_times, color='red', label='Binary Insertion Sort')

# Interpolating functions
x_vals = np.linspace(min(sizes), max(sizes), 100)
insertion_fit = np.polyfit(sizes, insertion_times, 2)
insertion_fit_fn = np.poly1d(insertion_fit)
plt.plot(x_vals, insertion_fit_fn(x_vals), linestyle='--', color='blue', label='Insertion Sort Interpolating Function')

binary_fit = np.polyfit(sizes, binary_times, 2)
binary_fit_fn = np.poly1d(binary_fit)
plt.plot(x_vals, binary_fit_fn(x_vals), linestyle='--', color='red', label='Binary Insertion Sort Interpolating Function')

insertion_eq = f'Insertion Sort: {insertion_fit_fn}'
binary_eq = f'Binary Insertion Sort: {binary_fit_fn}'
plt.text(0.5, 0.95, insertion_eq, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', color='blue')
plt.text(0.5, 0.90, binary_eq, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', color='red')

plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Insertion Sort and Binary Insertion Sort')
plt.legend()
plt.grid(True)
plt.show()

""" Question 4: 
As the size of the array increases, it is seen on the graph that binary insertion sort performs better than 
insertion sort. This is because binary insertion sort uses binary search initially to find the correct position for 
each of the elements, thus reducing the number of comparisons required for the algorithm to fully sort the data; and 
this is why this difference is more clearly seen as the datasets get larger."""