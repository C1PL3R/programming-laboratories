# import time
# import doctest
# from typing import Callable
#
#
#
#
# def measure_average_time(func: Callable,
#                          n: int,
#                          x: float,
#                          runs:int = 100) -> float:
#     """Вимірює середній час виконання функції 'func(n, x)' за
#     'runs' запусків.
#     Повертає середній час у секундах.
#     """
#     start_time = time.perf_counter()
#     for _ in range(runs):
#         func(n, x)
#         total_time = time.perf_counter() - start_time
#         avg_time = total_time / runs
#         return avg_time
#
#
# def calculate_a(n: int, x: float) -> str:
#     """Обчислює значення виразу:
#
#     a_n = ((-1)^n * x^(2 * n^2)) / (n^2 + n)!
#
#     Базові тести:
#     >>> calculate_a(1, 2.0)
#     '-2.0'
#     >>> calculate_a(2, 1.5)
#     '0.035596'
#     >>> calculate_a(1, -2.0)
#     '-2.0'
#     >>> calculate_a(2, -1.5)
#     '0.035596'
#     >>> calculate_a(3, 1.0)
#     '-2.0877e-09'
#     >>> calculate_a(3, 10.0)
#     '-2.0877e+09'
#     >>> calculate_a(2, 50.0)
#     '5.4253e+10'
#     >>> calculate_a(2, -100.0)
#     '1.3889e+13'
#     >>> calculate_a(10, 8.0)
#     '261.26'
#     >>> calculate_a(15, 10.5)
#     '-8.4298e-10'
#     >>> calculate_a(15, 20.0)
#     '-7.1471e+116'
#     >>> calculate_a(100, 200.0)
#     '0.0'
#     """
#     a0 = - (x ** 2) / 2.0
#     a = 1.0
#
#     fact1 = 1.0
#     for n in range(1, (n * n - n) + 1):
#         fact1 *= n
#
#     fact2 = 1.0
#     for n in range(1, (n * n + n) + 1):
#         fact2 *= n
#
#     c = 1.0
#     for i in range(1, (4 * n - 2) + 1):
#         c *= x
#
#     for _ in range(1, n + 1):
#         a *= -(a0 * c * fact1 / fact2)
#         a0 = a
#
#     return f"{a:.5}"
#
# def calculate_b(n: int, x: float) -> str:
#     """Обчислює суму:
#
#     S_n = sum_{k=1}^n ((-2x)^(k^2) / k!)
#
#     >>> calculate_b(1, 1.0)
#     '-2.0'
#     >>> calculate_b(2, 0.5)
#     '-0.5'
#     >>> calculate_b(3, 0.5)
#     '-0.66667'
#     >>> calculate_b(1, -1.0)
#     '2.0'
#     >>> calculate_b(2, -0.5)
#     '1.5'
#     >>> calculate_b(3, -0.5)
#     '1.6667'
#     >>> calculate_b(10, 0.2)
#     '-0.38724'
#     >>> calculate_b(10, 0.5)
#     '-0.63212'
#     >>> calculate_b(100, 0.54)
#     '1.8516e+176'
#     >>> calculate_b(15, 12.5)
#     '-2.6303e+302'
#     >>> calculate_b(1000, 0.503795)
#     '-0.63211'
#     >>> calculate_b(500, -0.5)
#     '1.7183'
#     """
#     # Тут має бути Ваш код
#     # return f"{total_sum:.5}"
#
#
# def calculate_c(n: int, x: float) -> float:
#     """Обчислює добуток:
#
#     P_n = prod_{k=1}^n (1 + |x|^(100*k) / k!)^(-1)
#
#     Базові тести:
#     >>> calculate_c(1, 1.0)
#     '0.5'
#     >>> calculate_c(2, 0.5)
#     '1.0'
#     >>> calculate_c(3, 0.5)
#     '1.0'
#
#     Тести для x < 1 при великих n:
#     >>> calculate_c(180, 0.99)
#     '0.67998'
#     >>> calculate_c(500, 0.99)
#     '0.67998'
#     >>> calculate_c(1000, 0.98)
#     '0.87486'
#
#     Великі n та x, близьке до одиниці:
#     >>> calculate_c(100, 1.00001)
#     '0.27109'
#     >>> calculate_c(500, -1.00005)
#     '0.26913'
#     >>> calculate_c(1000, 1.0001)
#     '0.26668'
#     >>> calculate_c(1000, -1.0005)
#     '0.24713'
#     """
#     # Тут має бути Ваш код
#
#     # return f"{result:.5}"
#
#
# def calculate_d(n: int, x: float) -> float:
#     """Обчислює суму:
#
#     S_n = sum_{k=1}^n (x^(k^2) / ((a_k + b_k) * k!))
#
#     де:
#     a_1 = 1,  a_2 = 1,
#     a_k = a_{k-1}/k + a_{k-2}*b_k
#
#     b_1 = 0,  b_2 = 1,
#     b_k = b_{k-1} + a_{k-1}
#
#
#     >>> calculate_d(1, 1.0)
#     '1.0'
#     >>> calculate_d(2, 1.0)
#     '1.25'
#     >>> calculate_d(3, 1.0)
#     '1.2885'
#     >>> calculate_d(1, 2.0)
#     '2.0'
#     >>> calculate_d(2, 2.0)
#     '6.0'
#     >>> calculate_d(3, 2.0)
#     '25.692'
#     >>> calculate_d(2, -0.5)
#     '-0.48438'
#     >>> calculate_d(1, 10.5)
#     '10.5'
#     >>> calculate_d(2, 10.5)
#     '3049.3'
#     >>> calculate_d(3, 10.5)
#     '5.967e+07'
#     >>> calculate_d(20, 1.01)
#     '1.3178'
#     >>> calculate_d(100, 1.05)
#     '1.4243'
#     >>> calculate_d(500, 1.1)
#     '1.5805'
#     >>> calculate_d(500, 1.2)
#     '2.0306'
#     """
#     # Тут має бути Ваш код
#     # return f"{result:.5}"
#
#
# #doctest.testmod(verbose=True)
#
# n = int(input("n = "))
# x = float(input("x = "))
#
# print(calculate_a(n, x))
# # calculate_b(n, x)
# # calculate_c(n, x)
# # calculate_d(n, x)

m1_list = [i for i in range(2, 100, 5)]
m2_list = [i for i in range(4, 100, 5)]

v1_list = [i for i in range(100, 1100, 50)]
v2_list = [0] * 20

print(
    len(m1_list),
    len(m2_list),
    len(v1_list),
    len(v2_list),

    f"{m1_list}\n", f"{m2_list}\n", f"{v1_list}\n", f'{v2_list}\n'
)