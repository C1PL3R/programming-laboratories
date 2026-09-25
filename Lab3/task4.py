import doctest
import math

def sequence_k(k: int) -> int:
    result = 0
    for num in range(1, k + 1):
        count = math.floor(math.log10(num ** 2)) + 1
        result = result * 10**count + num ** 2
    return result


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
    result = sequence_k(N)

    length = math.floor(math.log10(result)) + 1
    return length


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
    count = get_sequence_length(target_k)

    print(sequence_k(target_k))

    shift = count - target_k
    digit = int((sequence_k(target_k) // (10 ** shift)) % 10)

    target_number = 0
    for num in range(1, count + 1):
        pos_previous = (target_k - num)
        shift = count - pos_previous
        digit_previous = int((sequence_k(target_k) // (10 ** shift)) % 10)
        result = (digit * 10 ** (num * -1) + digit_previous) * 10 ** num
        print(result)

        target_number = math.sqrt(result)

        if not target_number.is_integer():
            pos_next = (target_k + num)
            shift = count - pos_next
            digit_next = int((sequence_k(target_k) // (10 ** shift)) % 10)
            result = digit * 10 ** num + digit_next
            print(result)

            target_number = math.sqrt(result)
            if target_number.is_integer():
                break
        else:
            break

    return (digit, int(target_number))


# def get_digits_statistics(k: int) -> list[int]:
#     """Повертає частоту появи цифр (0–9) у послідовності до k-тої цифри включно.

#     Повертає список довжиною 10, де i-й елемент відповідає кількості цифр i.

#     >>> get_digits_statistics(1)
#     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
#     >>> get_digits_statistics(2)
#     [0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
#     >>> get_digits_statistics(3)
#     [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
#     >>> get_digits_statistics(4)
#     [0, 2, 0, 0, 1, 0, 0, 0, 0, 1]
#     >>> get_digits_statistics(5)
#     [0, 2, 0, 0, 1, 0, 1, 0, 0, 1]
#     >>> get_digits_statistics(6)
#     [0, 2, 1, 0, 1, 0, 1, 0, 0, 1]
#     >>> get_digits_statistics(7)
#     [0, 2, 1, 0, 1, 1, 1, 0, 0, 1]
#     >>> get_digits_statistics(8)
#     [0, 2, 1, 1, 1, 1, 1, 0, 0, 1]
#     >>> get_digits_statistics(9)
#     [0, 2, 1, 1, 1, 1, 2, 0, 0, 1]
#     >>> get_digits_statistics(11)
#     [0, 2, 1, 1, 2, 1, 2, 0, 0, 2]
#     """
#     pass

# def plot_sequence_analysis(N: int) -> None:
#     """Побудувати графік зростання довжини послідовності 
#     від кількості використаних квадратів чисел (від 1 до N включно).

#     Функція має:
#     1. Згенерувати значення кількості квадратів n (від 1 до N).
#     2. Обчислити довжину послідовності для кожного n 
#     (за допомогою функції get_sequence_length).
#     3. Відобразити лінійний графік залежності довжини від n.
#     4. Додати підписи осей, заголовок графіка та сітку для зручності читання.

#     :param N: Кількість перших натуральних чисел (квадрати яких беруться до уваги).
#     :type N: int
#     :return: Функція нічого не повертає (повертає None), а лише демонструє графік.
#     :rtype: None
#     """
#     pass


# def plot_digits_statistics(k: int) -> None:
#     """Побудувати стовпчикову діаграму (barplot/histogram) 
#     частоти появи цифр (0–9) у послідовності до k-тої цифри включно.

#     Функція має:
#     1. Отримати список частот появи кожної цифри (від 0 до 9) 
#     за допомогою функції get_digits_statistics(k).
#     2. Побудувати стовпчикову діаграму, де по осі X розташовані 
#     цифри від 0 до 9, а по осі Y — їхня частота появи в послідовності.
#     3. Додати відповідні підписи осей, заголовок із зазначенням k 
#     та позначки на осі X для кожної цифри (0..9).

#     :param k: Позиція цифри в послідовності, до якої (включно) аналізується статистика.
#     :type k: int
#     :return: Функція нічого не повертає (повертає None), а лише демонструє графік.
#     :rtype: None
#     """
#     pass

n = int(input("N = "))
print(find_kth_digit_info(n))

# doctest.testmod(verbose=True)