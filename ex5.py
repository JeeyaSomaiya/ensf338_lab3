import random
import timeit
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

vectorSize = [1000, 2000, 4000, 8000, 16000, 32000]

def log_equation(x, a):
   return a * np.log2(x)

def linearSearch(arr, n):
   """
   Linear Search Implementation
   """
   for i in range(len(arr)):
      if arr[i] == n:
         return True
   return False

def binarySearch(arr, first, last, key):
   """
   Binary Search Implementation
   """
   if(first <= last):
      mid = (first+last)//2
      if (key == arr[mid]):
         return True
      elif (key < arr[mid]):
         return binarySearch(arr, first, mid-1, key)
         # last = mid - 1
      elif (key > arr[mid]):
         return binarySearch(arr, mid+1, last, key)
         # first = mid + 1
      
   return False


def generate_sorted_vector(size):
   """
   Generate a vector of size with random values and sort
   """

   # generate a random vector of size
   numbers = [x for x in range(size)]
   # sort the random vector
   sort_vector = sorted(numbers)
   
   return sort_vector

lineartimes = []
binarytimes = []

for vector in vectorSize:
   # get sorted vector
   sorted_vector = generate_sorted_vector(vector) 

   # get element at target index
   target_element = random.choice(sorted_vector)

   # measure linear search time using 100 itereations
   search_linear = timeit.repeat(lambda: linearSearch(sorted_vector, target_element), number=100)

   # measure binary search time using 100 iterations
   search_binary = timeit.repeat(lambda: binarySearch(sorted_vector, 0, len(sorted_vector)-1, target_element), number=100)

   # get avg times
   linearavg = sum(search_linear) / 100
   binaryavg = sum(search_binary) / 100

   # store values into list
   lineartimes.append(linearavg)
   binarytimes.append(binaryavg)

# print("Linear Search Times:", lineartimes)
# print("Binary Search Times:", binarytimes)
   
# Linear fit
slope, intercept = np.polyfit(vectorSize, lineartimes, 1)
plt.scatter(vectorSize, lineartimes)
linevalues = [slope * x + intercept for x in vectorSize]
plt.plot(vectorSize, linevalues, 'r')
# print("linear model is: t = %.2e * n + %.2e" % (slope, intercept))

# Log fit
log_fit, pcov = curve_fit(log_equation, vectorSize, binarytimes)
plt.scatter(vectorSize, binarytimes)
logvalues = [log_equation(x, *log_fit) for x in vectorSize]
plt.plot(vectorSize, logvalues, 'g')

plt.show()

'''
4. Linear complexity was used with linear search. 
   The function used was y = mx + b, where the parameters of the function is y = average times, x = vector size, m = slope, b = y-intercept.

   For binary search, a log function was used.
   The function used was y = log2(x), where the parameters of the function is x = vector size, y = average times

   The results are what we expected. When the vector size is very small, you can see that the linear search had a faster time complexity but because it is an O(n) and binary search is O(log n), you can see that the binary search time is able to level out at a faster time than the linear search as the vector size gets bigger.
'''