import time
import math


def calculate_sum_of_digit(n):
    length = int(math.log10(n) + 1)
    result = 0
    for i in range(1, length + 1):
        last_digit = n % 10
        n = n // 10
        result += last_digit**2
    return result

def is_happy(n, k):
    """
    Перевіряє, чи є число n k-щасливим.

    --- Базові випадки (k = 2) ---
    >>> is_happy(1, 2)
    True
    >>> is_happy(7, 2)
    True
    >>> is_happy(19, 2)
    True
    >>> is_happy(4, 2)
    False
    >>> is_happy(2, 2)
    False

    --- Інші значення степеня k ---
    >>> # Для k = 1 будь-яке число зводиться до 1 лише якщо воно саме 1
    >>> is_happy(1, 1)
    True
    >>> is_happy(5, 1)
    False

    >>> # Для k = 3 (кубічно-щасливі числа): 10, 55, 136 є 3-щасливими
    >>> is_happy(10, 3)
    True
    >>> is_happy(55, 3)
    True
    >>> is_happy(136, 3)
    True
    >>> is_happy(2, 3)
    False

    --- Перевірка великих чисел ---
    >>> is_happy(999, 2)
    False
    >>> is_happy(1000, 2)
    True
    """
    bunny = n
    for _ in range(999):
        turtle = calculate_sum_of_digit(n)
        n = turtle
        bunny = calculate_sum_of_digit(turtle)
        bunny = n
        print(turtle, bunny)

        if turtle == bunny:
            return False
        elif turtle == bunny == 1:
            return True



n = int(input("n = "))
k = int(input("k = "))
print(is_happy(n, k))


def is_abundant(n, alpha):
    """
    Перевіряє, чи є число n alpha-досконалим (sigma(n) == alpha * n).

    --- Граничні значення та некоректні вхідні дані ---
    >>> is_abundant(0, 2)
    False
    >>> is_abundant(-5, 2)
    False

    --- alpha = 1 (число має дорівнювати сумі дільників, що неможливо для n >= 1) ---
    >>> is_abundant(1, 1)
    True
    >>> is_abundant(6, 1)
    False

    --- alpha = 2 (традиційні досконалі числа) ---
    >>> is_abundant(6, 2)
    True
    >>> is_abundant(28, 2)
    True
    >>> is_abundant(496, 2)
    True
    >>> is_abundant(8128, 2)
    True
    >>> is_abundant(12, 2)
    False

    --- alpha = 3 (3-досконалі / мультидосконалі числа) ---
    >>> is_abundant(120, 3)
    True
    >>> is_abundant(672, 3)
    True
    >>> is_abundant(523776, 3)
    True
    >>> is_abundant(100, 3)
    False

    --- alpha = 4 (4-досконалі числа) ---
    >>> is_abundant(30240, 4)
    True
    >>> is_abundant(32760, 4)
    True
    """
    #Тут має бути Ваш код


def print_formatted_numbers(M, N, mode, alpha=2, k=2):
    """
    Форматовано виводить числа з проміжку [M, N].

    --- Тест 1: Точно 1 число у виводі (закінчується крапкою без крапки з комою) ---
    >>> print_formatted_numbers(6, 6, mode=2, alpha=2)
    6.

    --- Тест 2: Точно 5 чисел у виводі (останній рядок має 5 чисел і закривається крапкою) ---
    >>> print_formatted_numbers(1, 19, mode=1, k=2)
    1, 7, 10, 13, 19.

    --- Тест 3: Рівно 10 чисел у виводі (перший рядок з 5 закривається ';', другий з 5 закривається '.') ---
    >>> print_formatted_numbers(1, 44, mode=1, k=2)
    1, 7, 10, 13, 19;
    23, 28, 31, 32, 44.

    --- Тест 4: Більше ніж 5 чисел, де в останньому рядку < 5 чисел ---
    >>> print_formatted_numbers(1, 23, mode=1, k=2)
    1, 7, 10, 13, 19;
    23.

    --- Тест 5: Порожній проміжок (жодне число не підходить) ---
    >>> print_formatted_numbers(2, 5, mode=2, alpha=2)
    <BLANKLINE>

    --- Тест 6: Пнкт в) суміщені умови (k-щасливі ТА alpha-досконалі) ---
    >>> # 28 є і 2-щасливим (2^2+8^2=68 -> 100 -> 1) і 2-досконалим (1+2+4+7+14+28 = 56 = 2*28)
    >>> print_formatted_numbers(1, 100, mode=3, alpha=2, k=2)
    28.

    --- Тест 7: Коли M = N ---
    >>> print_formatted_numbers(7, 7, mode=1, k=2)
    7.
    >>> print_formatted_numbers(8, 8, mode=1, k=2)
    <BLANKLINE>
    """
    #Тут має бути Ваш код
