from algorithms.utils.timer import timer_decorator

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_helper(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_helper(arr, low, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, high)

@timer_decorator
def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr