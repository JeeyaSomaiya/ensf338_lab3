import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1  
            if arr[j] > arr[j + 1]:
                swaps += 1  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return comparisons, swaps

sizes = [100, 500, 1000, 5000, 10000]
comparison_counts = []
swap_counts = []

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    comparisons, swaps = bubble_sort(arr)
    comparison_counts.append(comparisons)
    swap_counts.append(swaps)

theoretical_comparisons = [(size*(size-1))/2 for size in sizes]
theoretical_swaps = [(size*(size-1))/4 for size in sizes]

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(sizes, comparison_counts, marker='o', label='Actual Comparisons', color='blue')
plt.plot(sizes, theoretical_comparisons, label='Theoretical Comparisons', color='red', linestyle='--')
plt.title('Number of Comparisons in Bubble Sort')
plt.xlabel('Input Size')
plt.ylabel('Number of Comparisons')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(sizes, swap_counts, marker='o', label='Actual Swaps', color='green')
plt.plot(sizes, theoretical_swaps, label='Theoretical Swaps', color='orange', linestyle='--')
plt.title('Number of Swaps in Bubble Sort')
plt.xlabel('Input Size')
plt.ylabel('Number of Swaps')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
