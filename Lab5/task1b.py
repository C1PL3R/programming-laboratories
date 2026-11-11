import math
import doctest
import matplotlib.pyplot as plt
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


def calculate_b(n: int, x: float) -> str:
    """Обчислює суму:

    S_n = sum_{k=1}^n ((-2x)^(k^2) / k!)

    >>> calculate_b(1, 1.0)
    '-2.0'
    >>> calculate_b(2, 0.5)
    '-0.5'
    >>> calculate_b(3, 0.5)
    '-0.66667'
    >>> calculate_b(1, -1.0)
    '2.0'
    >>> calculate_b(2, -0.5)
    '1.5'
    >>> calculate_b(3, -0.5)
    '1.6667'
    >>> calculate_b(10, 0.2)
    '-0.38724'
    >>> calculate_b(10, 0.5)
    '-0.63212'
    >>> calculate_b(100, 0.54)
    '1.8516e+176'
    >>> calculate_b(15, 12.5)
    '-2.6303e+302'
    >>> calculate_b(1000, 0.503795)
    '-0.63211'
    >>> calculate_b(500, -0.5)
    '1.7183'
    """
    if x == 0.0:
        return "0.0"

    # total_sum = 0
    # a_prev = 1.0
    # power = -2 * x
    #
    # for k in range(1, n + 1):
    #     numerator = 1.0
    #
    #     for _ in range(1, 2 * k):
    #         numerator *= power
    #
    #     qk = numerator / k
    #     ak = a_prev * qk
    #
    #     total_sum = total_sum + ak
    #     a_prev = ak
    total_sum = 0
    a_prev = 1.0
    base = -2 * x
    base_sq = base * base

    for k in range(1, n + 1):
        if k * k % 2 == 0:
            exponent = k * k // 2
        else:
            exponent = (k * k + 1) // 2

        numerator = 1.0

        for _ in range(exponent):
            numerator *= base_sq

        if k % 2 != 0:
            numerator = base

        qk = numerator / k
        ak = a_prev * qk
        print(k, ak)
        total_sum = total_sum + ak
        a_prev = ak

    res = f"{total_sum:.5g}"
    if "inf" in res.lower():
        res = "0.0"
    else:
        if "." not in res and "e" not in res:
            res += ".0"

    return res


n = int(input("n = "))
x = float(input("x = "))

print(calculate_b(n, x))


# def calculate_b_naive(n: int, x: float) -> float:
#     """Обчислення S_n без оптимізації."""
#     total = 0.0
#
#     for k in range(1, n + 1):
#         try:
#             term = ((-2 * x) ** (k ** 2)) / math.factorial(k)
#             total += term
#         except (OverflowError, ValueError):
#             try:
#                 base_int = int(-2 * x)
#                 num = base_int ** (k ** 2)
#                 den = math.factorial(k)
#                 total += float(num / den)
#             except (OverflowError, ValueError, ZeroDivisionError):
#                 break
#
#     res = f"{total:.5g}"
#     if "inf" in res.lower():
#         res = "0.0"
#     elif "." not in res and "e" not in res:
#         res += ".0"
#
#     return res
#
# b_n_list = [i for i in range(1, 31)]
# b_x_list = [30] * len(b_n_list)
#
# tasks = [
#     ("b", b_n_list, b_x_list, calculate_b, calculate_b_naive)
# ]
#
# for name, n_list, x_list, func_opt, func_naive in tasks:
#     t_opt_list = []
#     t_naive_list = []
#
#     for n, x in zip(n_list, x_list):
#         t_opt_list.append(measure_average_time(func_opt, n, x))
#         t_naive_list.append(measure_average_time(func_naive, n, x))
#
#     ratios = [tn / to if to > 0 else 1.0 for tn, to in zip(t_naive_list, t_opt_list)]
#
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
#
#     ax1.plot(
#         n_list,
#         t_naive_list,
#         label="Наївна реалізація",
#         color="red",
#         marker="o",
#     )
#     ax1.plot(
#         n_list, t_opt_list, label="Моя реалізація", color="green", marker="s"
#     )
#     ax1.set_title(f"Порівняння часу роботи (Завдання {name})")
#     ax1.set_xlabel("N")
#     ax1.set_ylabel("Час (секунди)")
#     ax1.grid(True)
#     ax1.legend()
#
#     ax2.plot(
#         n_list,
#         ratios,
#         label="Прискорення (T_naive / T_my)",
#         color="blue",
#         marker="^",
#     )
#
#     ax2.set_title(f"Коефіцієнт прискорення (Завдання {name})")
#     ax2.set_xlabel("N")
#     ax2.set_ylabel("Коефіцієнт (разів)")
#     ax2.grid(True)
#     ax2.legend()
#
#     plt.tight_layout()
#     plt.show()
#
# doctest.testmod(verbose=True)


