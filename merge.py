import threading
import random
import time

# Normal Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def normal_merge_sort(arr):
    merge_sort(arr)

# Multithreaded Merge Sort
def merge(left, right, arr):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def threaded_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_thread = threading.Thread(target=threaded_merge_sort, args=(left_half,))
    right_thread = threading.Thread(target=threaded_merge_sort, args=(right_half,))

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    merge(left_half, right_half, arr)


    # Generate a random list of numbers
data = [random.randint(1, 1) for _ in range(1000)]

# Measure the time for normal merge sort
start_time = time.time()
normal_merge_sort(data.copy())
normal_sort_time = time.time() - start_time

# Measure the time for multithreaded merge sort
start_time = time.time()
threaded_merge_sort(data.copy())
threaded_sort_time = time.time() - start_time
threaded_sort_time /= 1000

print(f"Normal Merge Sort Time: {normal_sort_time} seconds")
print(f"Multithreaded Merge Sort Time: {threaded_sort_time} seconds")
