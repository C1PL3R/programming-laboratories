import doctest
import math

import matplotlib.pyplot as plt


def is_prime(number: int) -> bool:
    """
    Перевіряє, чи є число простим.

    >>> is_prime(1)
    False

    >>> is_prime(2)
    True

    >>> is_prime(17)
    True

    >>> is_prime(25)
    False
    """
    if number < 2:
        return False
    for d in range(2, math.isqrt(number) + 1):
        if number % d == 0:
            return False
    return True


def digit_sum(number: int) -> int:
    """
    Обчислює суму цифр числа.

    >>> digit_sum(0)
    0

    >>> digit_sum(123)
    6

    >>> digit_sum(1001)
    2
    """
    result = 0
    for digit in list(str(number)):
        result += int(digit)

    return result


def find_double_primes(N: int) -> tuple[list[int], list[int]]:
    """
    Знаходить прості числа, сума цифр яких є простою.

    >>> find_double_primes(1)
    ([], [])

    >>> find_double_primes(10)
    ([2, 3, 5, 7], [2, 3, 5, 7])

    >>> find_double_primes(20)
    ([2, 3, 5, 7, 11], [2, 3, 5, 7, 2])
    """
    primes = []
    digit_sums = []

    for num in list(range(1, N + 1)):
        if is_prime(num) and is_prime(digit_sum(num)):
            primes.append(num)
            digit_sums.append(digit_sum(num))

    return primes, digit_sums


def plot_double_primes(numbers: list[int], digit_sums: list[int]) -> None:
    """
    Будує гістограму сум цифр.
    """
    if not numbers:
        return

    plt.figure(figsize=(8, 5))
    plt.bar(
        [str(n) for n in numbers],
        digit_sums,
        color="green",
        edgecolor="black",
    )
    plt.title("Сума цифр простих чисел (сума цифр яких також є простою)")
    plt.xlabel("Прості числа")
    plt.ylabel("Сума цифр")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


N = int(input("N = "))

numbers, digit_sums = find_double_primes(N)

if numbers:
    for number, digit_sum_value in zip(numbers, digit_sums):
        print(f"{number}: сума цифр = {digit_sum_value}")
else:
    print("Таких чисел немає.")

plot_double_primes(numbers, digit_sums)

doctest.testmod()
