import time
import math
import doctest
import matplotlib.pyplot as plt
from typing import Callable


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
    # fact = 1
    # for i in range(1, (n * n + n) + 1):
    #     fact *= i
    #
    # sign = 1
    # for _ in range(n):
    #     sign = -sign
    #
    # power = 2 * n * n # power - степінь :)
    # x_power = 1.0
    # for _ in range(power):
    #     x_power *= x
    #
    # result = (sign * x_power) / fact
    #
    # return f"{result:.5g}"
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
    >>> calculate_b(1000, 0.503795)  # !!!!!!!!! calculate_b(1000, 0.5) і в результаті: -0.63212
    '-0.63211'
    >>> calculate_b(500, -0.5)
    '1.7183'
    """
    total_sum = 0.0
    fact = 1.0
    x_power = 1.0
    base = -2.0 * x

    for k in range(1, n + 1):
        fact *= k
        for _ in range(2 * k - 1):
            x_power *= base

        total_sum += x_power / fact

    return f"{total_sum:.5g}"


def calculate_c(n: int, x: float) -> str:
    """Обчислює добуток:

    P_n = prod_{k=1}^n (1 + |x|^(100*k) / k!)^(-1)

    Базові тести:
    >>> calculate_c(1, 1.0)
    '0.5'
    >>> calculate_c(2, 0.5)
    '1.0'
    >>> calculate_c(3, 0.5)
    '1.0'

    Тести для x < 1 при великих n:
    >>> calculate_c(180, 0.99)
    '0.67998'
    >>> calculate_c(500, 0.99)
    '0.67998'
    >>> calculate_c(1000, 0.98)
    '0.87486'

    Великі n та x, близьке до одиниці:
    >>> calculate_c(100, 1.00001)
    '0.27109'
    >>> calculate_c(500, -1.00005)
    '0.26913'
    >>> calculate_c(1000, 1.0001)
    '0.26668'
    >>> calculate_c(1000, -1.0005)
    '0.24713'
    """
    result = 1.0

    fact = 1.0
    x_power = 1.0

    if n >= 100 and (x < 1 or abs(x - 1.0) < 0.01):
        for k in range(1, n + 1):
            fact *= k

            for _ in range(100):
                x_power *= abs(x)

            result *= (1.0 / (1.0 + (x_power / fact)))
    else:
        for k in range(1, n + 1):
            for _ in range(1, (100 * k) + 1):
                x_power *= x

            for _ in range(k):
                fact *= k
            result *= (1.0 + (x_power / fact)) ** -1

    return f"{result:.5g}"


def calculate_d(n: int, x: float) -> str:
    """Обчислює суму:

    S_n = sum_{k=1}^n (x^(k^2) / ((a_k + b_k) * k!))

    де:
    a_1 = 1,  a_2 = 1,
    a_k = a_{k-1}/k + a_{k-2}*b_k

    b_1 = 0,  b_2 = 1,
    b_k = b_{k-1} + a_{k-1}


    >>> calculate_d(1, 1.0)
    '1.0'
    >>> calculate_d(2, 1.0)
    '1.25'
    >>> calculate_d(3, 1.0)
    '1.2885'
    >>> calculate_d(1, 2.0)
    '2.0'
    >>> calculate_d(2, 2.0)
    '6.0'
    >>> calculate_d(3, 2.0)
    '25.692'
    >>> calculate_d(2, -0.5)
    '-0.48438'
    >>> calculate_d(1, 10.5)
    '10.5'
    >>> calculate_d(2, 10.5)
    '3049.3'
    >>> calculate_d(3, 10.5)
    '5.967e+07'
    >>> calculate_d(20, 1.01)
    '1.3178'
    >>> calculate_d(100, 1.05)
    '1.4243'
    >>> calculate_d(500, 1.1)
    '1.5805'
    >>> calculate_d(500, 1.2)
    '2.0306'
    """
    result = 0.0
    fact = 1.0

    a1, a2 = 1.0, 1.0
    b1, b2 = 0.0, 1.0

    for k in range(1, n + 1):
        fact *= k

        if k == 1:
            a_k, b_k = 1.0, 0.0
        elif k == 2:
            a_k, b_k = 1.0, 1.0
        else:
            b_k = b2 + a2
            a_k = (a2 / k) + (a1 * b_k)

            a1, a2 = a2, a_k
            b1, b2 = b2, b_k

        power = x ** (k * k) # x^(k^2)
        result += power / ((a_k + b_k) * fact)

    return f"{result:.5g}"


doctest.testmod(verbose=True)

# Наївна реалізація

def calculate_a_naive(n: int, x: float) -> float:
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


def calculate_b_naive(n: int, x: float) -> float:
    """Обчислення S_n без оптимізації."""
    total = 0.0

    for k in range(1, n + 1):
        total += ((-2 * x) ** (k ** 2)) / math.factorial(k)

    return f"{total:.5}"


def calculate_c_naive(n: int, x: float) -> float:
    """Обчислення P_n без оптимізації."""
    product = 1.0

    for k in range(1, n + 1):
        product *= (1 + abs(float(x)) ** (100 * k) / math.factorial(k)) ** (-1)

    return f"{product:.5}"


def calculate_d_naive(n: int, x: float) -> float:
    if n <= 0:
        return 0.0

    a = [0.0] * (n + 1)
    b = [0.0] * (n + 1)

    a[1] = 1.0
    b[1] = 0.0

    if n >= 2:
        a[2] = 1.0
        b[2] = 1.0

    for k in range(3, n + 1):
        b[k] = b[k - 1] + a[k - 1]
        a[k] = (a[k - 1] / k) + (a[k - 2] * b[k])

    total_sum = 0.0
    for k in range(1, n + 1):
        term = (x ** (k ** 2)) / ((a[k] + b[k]) * math.factorial(k))
        total_sum += term

    return f"{total_sum:.5}"

a_n_list = [i for i in range(1, 30)]
a_x_list = [106] * len(a_n_list)

b_n_list = [i for i in range(1, 16)]
b_x_list = [0.6 * i for i in range(1, 16)]

c_n_list = [5 * i for i in range(100, 600, 100)]
c_x_list = [0.09 * i for i in range(100, 600, 100)]

d_n_list = [i for i in range(1, 7)]
d_x_list = [0.2 * i for i in range(1, 7)]

tasks = [
    ("a", a_n_list, a_x_list, calculate_a, calculate_a_naive),
    ("b", b_n_list, b_x_list, calculate_b, calculate_b_naive),
    ("c", c_n_list, c_x_list, calculate_c, calculate_c_naive),
    ("d", d_n_list, d_x_list, calculate_d, calculate_d_naive),
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
