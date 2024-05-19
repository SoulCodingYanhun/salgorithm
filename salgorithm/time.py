
import time

def timeit(func):
    """装饰器，用于计算函数运行时间"""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 开始时间
        result = func(*args, **kwargs)  # 执行函数
        end_time = time.time()  # 结束时间
        print(f"{func.__name__} took {:.6f} seconds.".format(end_time - start_time))
        return result
    return wrapper
