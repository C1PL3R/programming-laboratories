import doctest
import math

import matplotlib.pyplot as plt


def get_number_by_pos(number, pos, total_digits):
    shift = total_digits - pos
    digit = (number // (10**shift)) % 10
    return digit


def is_palindrome(number: int) -> bool:
    """
    Перевіряє, чи є число паліндромом.

    >>> is_palindrome(1)
    True

    >>> is_palindrome(11)
    True

    >>> is_palindrome(121)
    True

    >>> is_palindrome(123)
    False
    """
    if number < 0:
        return False
    elif number == 0:
        return True

    total_digits = math.floor(math.log10(number)) + 1

    step = total_digits

    for i in range(1, (total_digits // 2) + 1):
        if get_number_by_pos(number, i, total_digits) != get_number_by_pos(
            number, step, total_digits
        ):
            return False

        step -= 1
    return True


def find_palindrom_squares(N: int) -> tuple[list[int], list[int]]:
    """
    Знаходить числа, квадрати яких є паліндромами.

    >>> find_palindrom_squares(1)
    ([1], [1])

    >>> find_palindrom_squares(5)
    ([1, 2, 3], [1, 4, 9])

    >>> find_palindrom_squares(12)
    ([1, 2, 3, 11], [1, 4, 9, 121])

    >>> find_palindrom_squares(0)
    ([], [])
    """
    numbers = []
    squares = []
    for num in list(range(1, N + 1)):
        if is_palindrome(num**2):
            numbers.append(num)
            squares.append(num**2)

    return numbers, squares


def plot_palindrom_squares(numbers: list[int], squares: list[int]) -> None:
    """
    Будує графік та гістограму квадратів чисел.
    Функція нічого не повертає.
    """
    if not numbers:
        return

    counts = list(range(1, len(numbers) + 1))

    plt.figure(figsize=(8, 5))
    plt.plot(numbers, counts, marker="o", linestyle="-", color="purple")
    plt.title("Залежність кількості чисел з квадратами-паліндромами від N")
    plt.xlabel("Число N")
    plt.ylabel("Кількість знайдених чисел")
    plt.grid(True)
    plt.show()


doctest.testmod()

N = int(input("N = "))

numbers, squares = find_palindrom_squares(N)

if numbers:
    for number, square in zip(numbers, squares):
        print(f"{number}^2 = {square}")
else:
    print("Таких чисел немає.")

plot_palindrom_squares(numbers, squares)
