import time
from dataclasses import dataclass, field
from typing import Any, Callable

@dataclass
class AlgorithmResult:
    result: Any
    time: float

def timer_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> AlgorithmResult:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return AlgorithmResult(result=result, time=execution_time)
    return wrapper