# def calculate_a(k):
#     numerator = 1.0
#     x = 2
#
#     if k % 2 == 0:
#         power = int(k / 2)
#     else:
#         power = int((k + 1) / 2)
#     print(k)
#
#     for i in range(1, power + 1):
#         numerator *= x * x
#
#     if k % 2 != 0:
#         numerator /= 2
#
#     return numerator


import time
from typing import Callable

# 1. Твоя функція (без print)
def power_even_split(k: int, x: float = 2.0) -> float:
    numerator = 1.0
    if k % 2 == 0:
        power = k // 2
    else:
        power = (k + 1) // 2

    for _ in range(1, power + 1):
        numerator *= x * x

    if k % 2 != 0:
        numerator /= x

    return numerator

# 2. Швидке піднесення до степеня O(log N)
def power_binary(k: int, x: float = 2.0) -> float:
    res = 1.0
    base = x
    p = k
    while p > 0:
        if p % 2 == 1:
            res *= base
        base *= base
        p //= 2
    return res

# 3. Звичайний цикл O(N)
def power_linear(k: int, x: float = 2.0) -> float:
    res = 1.0
    for _ in range(k):
        res *= x
    return res


def measure_average_time(func: Callable, k: int, runs: int = 1000) -> float:
    start_time = time.perf_counter()
    for _ in range(runs):
        func(k)
    total_time = time.perf_counter() - start_time
    return total_time / runs


# Порівняємо на великому степені, наприклад N = 10 000
N = 1000000

t1 = measure_average_time(power_even_split, k=N)
t2 = measure_average_time(power_binary, k=N)
t3 = measure_average_time(power_linear, k=N)

print(f"Степінь N = {N}:")
print(f"1. Поділ навпіл (твій підхід): {t1:.8f} сек")
print(f"2. Binary Exponentiation O(log N): {t2:.8f} сек")
print(f"3. Звичайний цикл O(N): {t3:.8f} сек")