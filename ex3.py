from numpy.random import randint

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr [j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    
    swaps = n * (n - 1) / 4
    comparisons = n * (n - 1) / 2

    return comparisons, swaps

arr = [8,42,25,3,3,2,27,3]

def rand_arr():
    for i in range(0, 200):
        arr = randint(0, 50, i)
        print(f'\n{arr}')
        print(f'{bubblesort(arr)}, \n{arr} \n')

rand_arr()
