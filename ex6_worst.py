import random
from matplotlib import pyplot as plt
import timeit

def binary_search(arr, key):
   first = 0
   last = len(arr) -1
   if(first >= last):
      mid = (first + last)/2
      if(key == arr[mid]):
         return mid
      elif(key < arr[mid]):
         return binary_search(arr, first, mid-1, key)
      elif(key > arr[mid]):
         return binary_search(arr, mid+1, last, key)
   return -1

def linear_search(n, l):
   for i in range(len(n)):
      if n[i] == l:
         return i
   return -1

def quicksort(arr):
   '''
   quicksort in worst case
   '''
   if len(arr) <= 1:
      return arr
   pivot = arr[0]
   left = [x for x in arr[1:] if x <= pivot]
   right = [x for x in arr[1:] if x > pivot]
   return quicksort(left) + [pivot] + quicksort(right)

def quicksort_binary(arr, x):
   sorted_arr = quicksort(arr)
   index = binary_search(sorted_arr, x)
   if index != -1:
      return True
   else:
      return False
   

def q3(size, algorithm):
   arr = random.sample(range(size * 10), size)
   target = random.choice(arr)

   time_taken = timeit.timeit(lambda: algorithm(arr, target), number=100)

   time_avg = time_taken / 100

   return time_avg

inputSize = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

time_linear = []
time_algo = []

for size in inputSize:
   linear_avg = q3(size, linear_search)
   time_linear.append(linear_avg)

   algo_avg = q3(size, quicksort_binary)
   time_algo.append(algo_avg)

plt.figure(figsize=(10, 6))
plt.plot(inputSize, time_algo, label="Quicksort and binary search")
plt.plot(inputSize, time_linear, label="Linear search")
plt.xlabel("input size")
plt.ylabel("avg time(s)")
plt.legend()
plt.grid(True)

plt.show()

