import doctest


def calculate_payment(
    price: int,
    banknotes_500: int,
    banknotes_100: int,
    banknotes_50: int,
    banknotes_20: int,
    banknotes_10: int,
    banknotes_5: int,
    banknotes_1: int,
) -> str:
    """Calculates the number of banknotes of each denomination used to pay for a purchase.

    >>> calculate_payment(534, 1, 3, 2, 3, 5, 2, 10)
    '500: 1 banknotes;\\n100: 0 banknotes;\\n50: 0 banknotes;\\n20: 1 banknotes;\\n10: 1 banknotes;\\n5: 0 banknotes;\\n1: 4 banknotes;\\nRemaining amount: 0 UAH.'

    >>> calculate_payment(1245, 2, 3, 1, 2, 5, 2, 10)
    '500: 2 banknotes;\\n100: 2 banknotes;\\n50: 0 banknotes;\\n20: 2 banknotes;\\n10: 0 banknotes;\\n5: 1 banknotes;\\n1: 0 banknotes;\\nRemaining amount: 0 UAH.'

    >>> calculate_payment(137, 1, 0, 2, 1, 1, 0, 2)
    '500: 0 banknotes;\\n100: 0 banknotes;\\n50: 2 banknotes;\\n20: 1 banknotes;\\n10: 1 banknotes;\\n5: 0 banknotes;\\n1: 2 banknotes;\\nRemaining amount: 5 UAH.'

    >>> calculate_payment(68, 0, 0, 1, 0, 1, 0, 3)
    '500: 0 banknotes;\\n100: 0 banknotes;\\n50: 1 banknotes;\\n20: 0 banknotes;\\n10: 1 banknotes;\\n5: 0 banknotes;\\n1: 3 banknotes;\\nRemaining amount: 5 UAH.'
    """

    count_of_500 = min(banknotes_500, price // 500)
    price -= count_of_500 * 500

    count_of_100 = min(banknotes_100, price // 100)
    price -= count_of_100 * 100

    count_of_50 = min(banknotes_50, price // 50)
    price -= count_of_50 * 50

    count_of_20 = min(banknotes_20, price // 20)
    price -= count_of_20 * 20

    count_of_10 = min(banknotes_10, price // 10)
    price -= count_of_10 * 10

    count_of_5 = min(banknotes_5, price // 5)
    price -= count_of_5 * 5

    count_of_1 = min(banknotes_1, price // 1)
    price -= count_of_1 * 1

    return (
        f"500: {count_of_500} banknotes;\n"
        f"100: {count_of_100} banknotes;\n"
        f"50: {count_of_50} banknotes;\n"
        f"20: {count_of_20} banknotes;\n"
        f"10: {count_of_10} banknotes;\n"
        f"5: {count_of_5} banknotes;\n"
        f"1: {count_of_1} banknotes;\n"
        f"Remaining amount: {price} UAH."
    )


doctest.testmod()

price = int(input("Enter price: "))
banknotes_500 = int(input("Enter banknotes 500: "))
banknotes_100 = int(input("Enter banknotes 100: "))
banknotes_50 = int(input("Enter banknotes 50: "))
banknotes_20 = int(input("Enter banknotes 20: "))
banknotes_10 = int(input("Enter banknotes 10: "))
banknotes_5 = int(input("Enter banknotes 5: "))
banknotes_1 = int(input("Enter banknotes 1: "))

print(
    calculate_payment(
        price,
        banknotes_500,
        banknotes_100,
        banknotes_50,
        banknotes_20,
        banknotes_10,
        banknotes_5,
        banknotes_1,
    )
)
