def bucket_sort(arr):
    # 确定桶的数量，这里假设为10
    num_buckets = 10

    # 创建一个空的桶列表
    buckets = [[] for _ in range(num_buckets)]

    # 将元素分配到桶中
    for num in arr:
        if isinstance(num, int):
            index = min(num // num_buckets, num_buckets - 1)
        else:
            index = min(int(num * num_buckets), num_buckets - 1)
        buckets[index].append(num)

    # 对每个桶中的元素进行排序
    for bucket in buckets:
        bucket.sort()

    # 将排序后的元素合并到一个新的列表中
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

