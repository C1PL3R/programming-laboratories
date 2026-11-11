import math
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

def calculate_a(n: int, x: float) -> str:
    """Обчислює значення виразу:

    a_n = ((-1)^n * x^(2 * n^2)) / (n^2 + n)!

    Базові тести:
    >>> calculate_a(1, 2.0)
    '-2.0'
    >>> calculate_a(2, 1.5)
    '0.035596'
    >>> calculate_a(1, -2.0)
    '-2.0'
    >>> calculate_a(2, -1.5)
    '0.035596'
    >>> calculate_a(3, 1.0)
    '-2.0877e-09'
    >>> calculate_a(3, 10.0)
    '-2.0877e+09'
    >>> calculate_a(2, 50.0)
    '5.4253e+10'
    >>> calculate_a(2, -100.0)
    '1.3889e+13'
    >>> calculate_a(10, 8.0)
    '261.26'
    >>> calculate_a(15, 10.5)
    '-8.4298e-10'
    >>> calculate_a(15, 20.0)
    '-7.1471e+116'
    >>> calculate_a(100, 200.0)
    '0.0'
    """
    a_prev = 1
    an = 0.0
    x2 = x * x

    for k in range(1, n + 1):
        qk = -1.0
        for i in range(k * k - k + 1, k * k + k + 1):
            qk = (qk * x2) / i

        qk = qk / x2
        an = a_prev * qk

        a_prev = an

    res = f"{an:.5g}"
    if "inf" in res.lower():
        res = "0.0"
    else:
        if "." not in res and "e" not in res:
            res += ".0"

    return res


def calculate_a_naive(n: int, x: float) -> str:
    """Обчислення a_n без оптимізації з перехопленням переповнення."""
    try:
        result = ((-1) ** n * x ** (2 * n ** 2)) / math.factorial(n ** 2 + n)
        return f"{result:.5g}"
    except (OverflowError, ValueError):
        try:
            num = ((-1) ** n) * (int(x) ** (2 * n ** 2))
            den = math.factorial(n ** 2 + n)
            # Примусове ділення точних int через Decimal або float з перехопленням
            res_val = float(num / den)
            return f"{res_val:.5g}"
        except (OverflowError, ValueError, ZeroDivisionError):
            return "inf"


a_n_list = [i for i in range(1, 30)]
a_x_list = [106] * len(a_n_list)

tasks = [
    ("a", a_n_list, a_x_list, calculate_a, calculate_a_naive)
]

for name, n_list, x_list, func_opt, func_naive in tasks:
    t_opt_list = []
    t_naive_list = []

    for n, x in zip(n_list, x_list):
        t_opt_list.append(measure_average_time(func_opt, n, x))
        t_naive_list.append(measure_average_time(func_naive, n, x))

    ratios = [tn / to if to > 0 else 1.0 for tn, to in zip(t_naive_list, t_opt_list)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.plot(
        n_list,
        t_naive_list,
        label="Наївна реалізація",
        color="red",
        marker="o",
    )
    ax1.plot(
        n_list, t_opt_list, label="Моя реалізація", color="green", marker="s"
    )
    ax1.set_title(f"Порівняння часу роботи (Завдання {name})")
    ax1.set_xlabel("N")
    ax1.set_ylabel("Час (секунди)")
    ax1.grid(True)
    ax1.legend()

    ax2.plot(
        n_list,
        ratios,
        label="Прискорення (T_naive / T_my)",
        color="blue",
        marker="^",
    )
    ax2.set_title(f"Коефіцієнт прискорення (Завдання {name})")
    ax2.set_xlabel("N")
    ax2.set_ylabel("Коефіцієнт (разів)")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.show()

# n = int(input("n = "))
# x = float(input("x = "))
#
# print(calculate_a(n, x))
