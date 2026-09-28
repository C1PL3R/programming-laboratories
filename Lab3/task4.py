import doctest
import math
import matplotlib.pyplot as plt


def get_sequence_length(N: int) -> int:
    """Обчислює довжину послідовності, утвореної квадратами перших N натуральних чисел.

    Заборонено використовувати str та list.

    >>> get_sequence_length(1)
    1
    >>> get_sequence_length(2)
    2
    >>> get_sequence_length(3)
    3
    >>> get_sequence_length(4)
    5
    >>> get_sequence_length(5)
    7
    >>> get_sequence_length(6)
    9
    >>> get_sequence_length(7)
    11
    >>> get_sequence_length(9)
    15
    >>> get_sequence_length(10)
    18
    >>> get_sequence_length(31)
    81
    """
    length = 0
    for num in range(1, N + 1):
        length += math.floor(math.log10(num**2)) + 1
    return length


def get_sequence_count_block_of_squares(N: int) -> int:
    length = 0
    blocks_of_squares = 0
    for num in range(1, N + 1):
        if length >= N:
            break
        blocks_of_squares += 1
        length += math.floor(math.log10(num**2)) + 1
    return blocks_of_squares


def find_kth_digit_info(target_k: int) -> tuple[int, int]:
    """Знаходить k-ту цифру послідовності та число, чий квадрат містить цю цифру.

    Повертає кортеж: (k_та_цифра, число_чий_квадрат_містить_цифру).
    Заборонено використовувати str та list.

    >>> find_kth_digit_info(1)
    (1, 1)
    >>> find_kth_digit_info(2)
    (4, 2)
    >>> find_kth_digit_info(3)
    (9, 3)
    >>> find_kth_digit_info(4)
    (1, 4)
    >>> find_kth_digit_info(5)
    (6, 4)
    >>> find_kth_digit_info(6)
    (2, 5)
    >>> find_kth_digit_info(7)
    (5, 5)
    >>> find_kth_digit_info(8)
    (3, 6)
    >>> find_kth_digit_info(9)
    (6, 6)
    >>> find_kth_digit_info(10)
    (4, 7)
    >>> find_kth_digit_info(11)
    (9, 7)
    """
    blocks_of_squares = get_sequence_count_block_of_squares(target_k)

    length = 0
    for num in range(1, target_k + 1):
        if length >= target_k:
            break
        length += math.floor(math.log10(num**2)) + 1

    hidden_number = length - target_k
    # це кількість чисел яка не ввійшла в кількість чисел заданої позиції

    k_number = (blocks_of_squares**2 // (10**hidden_number)) % 10

    return (k_number, blocks_of_squares)


def get_digits_statistics(k: int) -> list[int]:
    """Повертає частоту появи цифр (0–9) у послідовності до k-тої цифри включно.

    Повертає список довжиною 10, де i-й елемент відповідає кількості цифр i.

    >>> get_digits_statistics(1)
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> get_digits_statistics(2)
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
    >>> get_digits_statistics(3)
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
    >>> get_digits_statistics(4)
    [0, 2, 0, 0, 1, 0, 0, 0, 0, 1]
    >>> get_digits_statistics(5)
    [0, 2, 0, 0, 1, 0, 1, 0, 0, 1]
    >>> get_digits_statistics(6)
    [0, 2, 1, 0, 1, 0, 1, 0, 0, 1]
    >>> get_digits_statistics(7)
    [0, 2, 1, 0, 1, 1, 1, 0, 0, 1]
    >>> get_digits_statistics(8)
    [0, 2, 1, 1, 1, 1, 1, 0, 0, 1]
    >>> get_digits_statistics(9)
    [0, 2, 1, 1, 1, 1, 2, 0, 0, 1]
    >>> get_digits_statistics(11)
    [0, 2, 1, 1, 2, 1, 2, 0, 0, 2]
    """
    result_list = [0] * 10
    squares_list = []
    digits_list = []

    blocks_of_squares = get_sequence_count_block_of_squares(k)
    hidden_number = blocks_of_squares - k

    for num in range(1, blocks_of_squares + 1):
        squares_list.append(num**2)

    for num in squares_list:
        digit = math.floor(math.log10(num)) + 1
        for i in range(1, digit + 1):
            k_number = (num // (10 ** (digit - i))) % 10
            digits_list.append(k_number)

    digits_list = digits_list[:k]

    for digit in digits_list:
        result_list[digit] += 1


    return result_list


def plot_sequence_analysis(N: int) -> None:
    """Побудувати графік зростання довжини послідовності
    від кількості використаних квадратів чисел (від 1 до N включно).

    Функція має:
    1. Згенерувати значення кількості квадратів n (від 1 до N).
    2. Обчислити довжину послідовності для кожного n
    (за допомогою функції get_sequence_length).
    3. Відобразити лінійний графік залежності довжини від n.
    4. Додати підписи осей, заголовок графіка та сітку для зручності читання.

    :param N: Кількість перших натуральних чисел (квадрати яких беруться до уваги).
    :type N: int
    :return: Функція нічого не повертає (повертає None), а лише демонструє графік.
    :rtype: None
    """
    n_values = list(range(1, N + 1))
    lengths = [get_sequence_length(n) for n in n_values]

    plt.figure(figsize=(8, 5))
    plt.plot(n_values, lengths, marker="o", color="blue", linestyle="-")
    plt.title("Залежність довжини послідовності від кількості квадратів (N)")
    plt.xlabel("Кількість квадратів чисел (n)")
    plt.ylabel("Довжина послідовності (у цифрах)")
    plt.grid(True)
    plt.show()


def plot_digits_statistics(k: int) -> None:
    """Побудувати стовпчикову діаграму (barplot/histogram)
    частоти появи цифр (0–9) у послідовності до k-тої цифри включно.

    Функція має:
    1. Отримати список частот появи кожної цифри (від 0 до 9)
    за допомогою функції get_digits_statistics(k).
    2. Побудувати стовпчикову діаграму, де по осі X розташовані
    цифри від 0 до 9, а по осі Y — їхня частота появи в послідовності.
    3. Додати відповідні підписи осей, заголовок із зазначенням k
    та позначки на осі X для кожної цифри (0..9).

    :param k: Позиція цифри в послідовності, до якої (включно) аналізується статистика.
    :type k: int
    :return: Функція нічого не повертає (повертає None), а лише демонструє графік.
    :rtype: None
    """
    statistics = get_digits_statistics(k)
    digits = list(range(10))

    plt.figure(figsize=(8, 5))
    plt.bar(digits, statistics, color="skyblue", edgecolor="black")
    plt.title(
        f"Частота появи цифр (0–9) у послідовності до {k}-ї цифри включно"
    )
    plt.xlabel("Цифри (0–9)")
    plt.ylabel("Частота появи")
    plt.xticks(digits)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

doctest.testmod(verbose=True)

n = int(input("N = "))

plot_sequence_analysis(n)
plot_digits_statistics(n)
