from algorithms.utils.timer import timer_decorator

@timer_decorator
def linear_search(arr, target):
    """
    线性查找算法
    
    :param arr: 数组
    :param target: 查找目标
    :return: 目标在数组中的索引,如果不存在则返回-1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1