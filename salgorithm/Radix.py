def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 统计每个数字出现的次数
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # 计算累计次数
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 根据次数将元素放入正确的位置
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # 将排序后的结果复制回原数组
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # 找到数组中的最大值，确定迭代次数
    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr