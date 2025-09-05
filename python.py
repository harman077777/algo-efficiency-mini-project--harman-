# 1. Fibonacci
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# 3. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        result.append(left[i] if left[i] < right[j] else right[j])
        i += left[i] < right[j]
        j += left[i] >= right[j]
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 4. quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# 5. insertion sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# 6. bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 7. selection sort 

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 8. binary search 

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Time Profiling

import time
start = time.time()
merge_sort([5, 2, 9, 1])
end = time.time()
print("Execution Time:", end - start)

# Memory Profiling

from memory_profiler import profile
@profile
def run_sort():
    merge_sort([5, 2, 9, 1])

# Visualization with Matplotlib

import matplotlib.pyplot as plt
input_sizes = [10, 100, 500, 1000]
times = [0.001, 0.01, 0.05, 0.2]  # Example values
plt.plot(input_sizes, times, marker='o')
plt.title("Execution Time vs Input Size")
plt.xlabel("Input Size")
plt.ylabel("Time (s)")
plt.grid(True)
plt.show()