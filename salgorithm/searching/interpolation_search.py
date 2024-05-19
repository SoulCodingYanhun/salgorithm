from algorithms.utils.timer import timer_decorator

@timer_decorator
def interpolation_search(arr, target):
    """
    插值查找算法
    
    :param arr: 有序数组
    :param target: 查找目标
    :return: 目标在数组中的索引,如果不存在则返回-1
    """
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1