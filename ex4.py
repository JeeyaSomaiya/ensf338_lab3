import matplotlib.pyplot as plt
import numpy as np
import sys

sys.setrecursionlimit(10**6)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    iterations = 0
    for j in range(low, high):
        iterations += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, iterations

def quicksort(arr, low, high):
    if low < high:
        pi, iterations = partition(arr, low, high)
        iterations += quicksort(arr, low, pi - 1)
        iterations += quicksort(arr, pi + 1, high)
        return iterations
    return 0

def generate_sorted_array(n):
    return list(range(1, n + 1))

sizes = []
iterations = []
for i in range(1, 7):  
    n = 3**i
    sizes.append(n)
    arr = generate_sorted_array(n)
    iter_count = quicksort(arr, 0, len(arr) - 1)
    iterations.append(iter_count)

plt.figure(figsize=(10, 6))
plt.scatter(sizes, iterations, color='blue', label='Number of Iterations')
plt.xlabel('Input Size (n)')
plt.ylabel('Number of Iterations')
plt.title('Number of Iterations in Quicksort')
plt.grid(True)

# Fit a quadratic interpolation function to the data points
popt = np.polyfit(sizes, iterations, 2)
curve_x = np.linspace(min(sizes), max(sizes), 100)
curve_y = popt[0] * curve_x ** 2 + popt[1] * curve_x + popt[2]
plt.plot(curve_x, curve_y, linestyle='--', color='red', label='Quadratic Interpolating Function')

plt.legend()
plt.show()
