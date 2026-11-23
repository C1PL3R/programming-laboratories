import math
import doctest
import matplotlib.pyplot as plt
from my_func import measure_average_time, calculate_power


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
    power = calculate_power(100, abs(x))
    a_prev = 1.0
    result = 1.0

    for k in range(1, n + 1):
        an = a_prev * (power / k)

        if math.isinf(an):
            return "0.0"

        result *= 1.0 / (1.0 + an)
        a_prev = an

        if an < 1e-16:
            break

    res = f"{result:.5g}"
    if "inf" in res.lower():
        res = "0.0"
    elif "." not in res and "e" not in res:
        res += ".0"

    return res


# n = int(input("n = "))
# x = float(input("x = "))
#
# print(calculate_c(n, x))

def calculate_c_naive(n: int, x: float) -> float:
    """Обчислення P_n без оптимізації."""
    product = 1.0

    for k in range(1, n + 1):
        product *= (1 + abs(float(x)) ** (100 * k) / math.factorial(k)) ** (-1)

    return f"{product:.5}"

c_n_list = [17 * i for i in range(1, 11)]
c_x_list = [1.001 + 0.0005 * i for i in range(1, 11)]

tasks = [
    ("c", c_n_list, c_x_list, calculate_c, calculate_c_naive)
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