import time

class TimedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()  # 开始时间
        result = self.func(*args, **kwargs)  # 执行函数
        end_time = time.time()  # 结束时间
        print(f"{self.func.__name__} took {end_time - start_time:.6f} seconds.")
        return result

    def time(self, *args, **kwargs):
        return self(*args, **kwargs)
