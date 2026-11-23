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

num1 = int(input("N1 = "))

print(is_armstrong(num1))