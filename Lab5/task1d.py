import math
import doctest
import matplotlib.pyplot as plt
from my_func import measure_average_time, calculate_power


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

    a_prev_1, a_prev_2 = 1.0, 1.0
    b_prev_2 = 1.0
    u_prev = 1.0
    prev_sum = 1.0  # a_1 + b_1 = 1.0 + 0.0

    for k in range(1, n + 1):
        if k == 1:
            a_k, b_k = 1.0, 0.0
        elif k == 2:
            a_k, b_k = 1.0, 1.0
        else:
            b_k = b_prev_2 + a_prev_2
            a_k = (a_prev_2 / k) + (a_prev_1 * b_k)

            a_prev_1, a_prev_2 = a_prev_2, a_k
            b_prev_2 = b_k

        curr_sum = a_k + b_k
        power = calculate_power(2 * k - 1, x)

        qk = (power * prev_sum) / (k * curr_sum)
        an = u_prev * qk

        result += an

        if k > 2 and an != 0.0 and abs(an) < abs(result) * 1e-16:
            break

        u_prev = an
        prev_sum = curr_sum

    res = f"{result:.5g}"
    if "inf" in res.lower() or "nan" in res.lower():
        return "0.0"
    if "." not in res and "e" not in res:
        res += ".0"

    return res

#
# n = int(input("n = "))
# x = float(input("x = "))
#
# print(calculate_d(n, x))


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


d_n_list = [11 * i for i in range(1, 11)]
d_x_list = [1.0 + 0.005 * i for i in range(1, 11)]


tasks = [
    ("d", d_n_list, d_x_list, calculate_d, calculate_d_naive)
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

doctest.testmod(verbose=True)
