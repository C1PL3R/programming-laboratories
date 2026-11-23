from typing import Callable
import time

def measure_average_time(func: Callable, n: int, x: float, runs:int = 100) -> float:
    """Вимірює середній час виконання функції 'func(n, x)' за
    'runs' запусків.
    Повертає середній час у секундах.
    """
    start_time = time.perf_counter()
    for _ in range(runs):
        func(n, x)
    total_time = time.perf_counter() - start_time

    return total_time / runs


def calculate_power(k, x) -> float:
    result = 1.0
    while k > 0:
        if k % 2 != 0:
            result *= x
        x *= x
        k //= 2

    return result