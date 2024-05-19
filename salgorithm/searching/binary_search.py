from algorithms.utils.timer import timer_decorator

@timer_decorator
def binary_search(arr, target):
    """
    二分查找算法
    
    :param arr: 有序数组
    :param target: 查找目标
    :return: 目标在数组中的索引,如果不存在则返回-1
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1