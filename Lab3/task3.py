import doctest

import matplotlib.pyplot as plt


def is_armstrong(number: int) -> bool:
    """
    Перевіряє, чи є число числом Армстронга.

    >>> is_armstrong(153)
    True
    >>> is_armstrong(370)
    True
    >>> is_armstrong(100)
    False
    """
    result = 0
    for digit in list(str(number)):
        result += int(digit) ** len(list(str(number)))

    return result == number


def get_armstrong_numbers(count: int) -> list[int]:
    """
    Повертає перші count чисел Армстронга.

    >>> get_armstrong_numbers(3)[:3]
    [1, 2, 3]
    """
    armstrong_numbers = []
    num = 1
    while len(armstrong_numbers) != count:
        if is_armstrong(num):
            armstrong_numbers.append(num)
        num += 1
    return armstrong_numbers


def nsd_search(number1: int, number2: int) -> int:
    """
    Знаходить НСД двох чисел за алгоритмом Евкліда.

    >>> nsd_search(153, 370)
    1
    >>> nsd_search(370, 371)
    1
    """
    while number2 != 0:
        number1, number2 = number2, number1 % number2
    return number1


def nsk_search(number1: int, number2: int) -> int:
    """
    Знаходить НСК двох чисел.

    >>> nsk_search(10, 15)
    30
    """
    nsd = nsd_search(number1, number2)
    if nsd == 0:
        return 0
    return (abs(number1 * number2)) // nsd


def common_divisors(number1: int, number2: int) -> list[int]:
    """
    Повертає всі спільні натуральні дільники.

    >>> common_divisors(12, 18)
    [1, 2, 3, 6]
    """
    common_divisors_list = []

    for num in range(1, number2 + 1):
        if number1 % num == 0 and number2 % num == 0:
            common_divisors_list.append(num)
    return common_divisors_list


def plot_armstrong_analysis(
    pair_indices: list[int],
    gcd_values: list[int],
    lcm_values: list[int],
    divisors_counts: list[int],
) -> None:
    """
    Будує графіки залежностей НСД, НСК та кількості
    спільних дільників від номера пари сусідніх чисел Армстронга.
    """
    ax1, ax2, ax3 = plt.subplots(3, 1, figsize=(8, 6))

    ax1.plot(gcd_values, pair_indices, color="red")
    ax1.set_title("Залежність НСД від номера пари сусідніх чисел Армстронга")

    ax2.plot(lcm_values, pair_indices, color="blue")
    ax2.set_title("Залежність НСК від номера пари сусідніх чисел Армстронга ")

    ax3.plot(divisors_counts, pair_indices, color="green")
    ax3.set_title(
        "Залежність кількості спільних дільників"
        + "від номера пари сусідніх чисел Армстронга"
    )

    plt.tight_layout()
    plt.show()


count = int(input("Введіть кількість чисел Армстронга (не менше 2): "))

armstrong_nums = get_armstrong_numbers(count)

pair_indices = []
gcd_values = []
lcm_values = []
divisors_counts = []

print("\n--- Результати аналізу пар послідовних чисел Армстронга ---")
for i in range(len(armstrong_nums) - 1):
    num1 = armstrong_nums[i]
    num2 = armstrong_nums[i + 1]

    nsd = nsd_search(num1, num2)
    nsk = nsk_search(num1, num2)
    divs = common_divisors(num1, num2)

    pair_index = i + 1
    pair_indices.append(pair_index)
    gcd_values.append(nsd)
    lcm_values.append(nsk)
    divisors_counts.append(len(divs))

    print(f"\nПара {pair_index}: ({num1}, {num2})")
    print(f"  НСД({num1}, {num2}) = {nsd}")
    print(f"  НСК({num1}, {num2}) = {nsk}")
    print("  Спільні дільники:", ", ".join(str(d) for d in divs))
    print(f"  Кількість спільних дільників = {len(divs)}")

plot_armstrong_analysis(pair_indices, gcd_values, lcm_values, divisors_counts)

doctest.testmod()
