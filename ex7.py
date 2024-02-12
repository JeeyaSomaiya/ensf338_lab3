import timeit
import json
import random
from matplotlib import pyplot as plt

def binary_search(arr, key, midpoint=None):
   '''
   Binary search, midpoint for first iteration must be configurable(all successive iterations will split the array in the middle)
   '''
   low = 0
   high = len(arr) - 1
   if midpoint is None:
      # if no midpoint indicated, split array in the middle
      mid = (low + high) // 2
   else:
      mid = midpoint

   while low <= high:
      if arr[mid] == key:
         return mid
      elif arr[mid] < key:
         low = mid + 1
      else:
         high = mid -1
      mid = (low + high) // 2
   return -1
   
# import json files
with open('ex7data.json', 'r') as data_file:
   data = json.load(data_file)

with open('ex7tasks.json', 'r') as tasks_file:
   tasks = json.load(tasks_file)

best_midpoints = {}

for task in tasks:
   random_midpoints = [random.randint(0, len(data) - 1) for i in range(100)]
   results = []

   for random_midpoint in random_midpoints:
      time_taken = timeit.timeit(lambda: binary_search(data, task, random_midpoint), number=100)
      avg_time = time_taken/100
      results.append((random_midpoint, avg_time))

   # find best midpoint with one with smallest avg time
   best_midpoint, fastest = min(results, key=lambda x: x[1])
   best_midpoints[task] = best_midpoint

# produce scatter plot with results
tasks_sorted, best_midpoints_sorted = zip(*sorted(best_midpoints.items()))

plt.figure(figsize=(10, 6))
plt.scatter(tasks_sorted, best_midpoints_sorted)
plt.xlabel("tasks")
plt.ylabel("best midpoint")
plt.grid(True)
plt.show()

# Q4. Looking at the graph, it looks like the closer the midpoint is to the target value, it will take faster to search the data. This is because the graph seems to have a linear line as the line of best fit, meaning that the best midpoint is close to the actual task value needed to find. Seeing this, the further away the midpoint is to the task value for the first iteration, the less values it will be able to divide for the first iteration, leading it to take a longer time.