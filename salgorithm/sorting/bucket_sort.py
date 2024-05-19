from algorithms.utils.timer import timer_decorator

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

@timer_decorator
def bucket_sort(arr):
    max_value = max(arr)
    size = max_value / len(arr)
    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])
    for i in range(len(arr)):
        insertion_sort(buckets[i])
    result = []
    for i in range(len(arr)):
        result = result + buckets[i]
    return result