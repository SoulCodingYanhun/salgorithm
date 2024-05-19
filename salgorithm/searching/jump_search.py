import math
from algorithms.utils.timer import timer_decorator

@timer_decorator
def jump_search(arr, target):
    """
    跳跃查找算法
    
    :param arr: 有序数组
    :param target: 查找目标
    :return: 目标在数组中的索引,如果不存在则返回-1
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1