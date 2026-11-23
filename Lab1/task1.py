import doctest


def number_operations(number: int) -> str:
    """Finds the sum of digits of the number,

    the absolute value of the difference of the number
    and the reversed number,
    and the fraction of the number and the sum of its digits.

    :param number: int

    >>> number_operations(124)
    'The sum of digits of the number 124 is 7;\\n'
    'the absolute value of the difference of the number and reversed number is 297;\\n'
    'the fraction of the number 124 and the sum of its digits is 17.714.'

    >>> number_operations(792)
    'The sum of digits of the number 792 is 18;\\n'
    'the absolute value of the difference of the number and reversed number is 495;\\n'
    'the fraction of the number 792 and the sum of its digits is 44.000.'

    >>> number_operations(55)
    'Number of digits must be 3'

    >>> number_operations(-124)
    'Number must be positive'

    >>> number_operations(100)
    'The sum of digits of the number 100 is 1;\\n'
    'the absolute value of the difference of the number and reversed number is 99;\\n'
    'the fraction of the number 100 and the sum of its digits is 100.000.'
    """

    is_negative = int(number < 0)
    is_not_three_digit = int(not (100 <= number <= 999)) * (1 - is_negative)
    is_valid = 1 - is_negative - is_not_three_digit

    safe_number = number * is_valid + 100 * (1 - is_valid)

    first_digit = safe_number // 100
    second_digit = (safe_number % 100) // 10
    third_digit = safe_number % 10

    sum_of_digit = first_digit + second_digit + third_digit
    reverse_number = third_digit * 100 + second_digit * 10 + first_digit
    absolute_value = abs(safe_number - reverse_number)
    fraction = safe_number / sum_of_digit

    error_negative = "Number must be positive"
    error_digits = "Number of digits must be 3"

    valid_result = (
        f"The sum of digits of the number {number} is {sum_of_digit};\n"
        f"the absolute value of the difference of the number and reversed number is {absolute_value};\n"
        f"the fraction of the number {number} and the sum of its digits is {fraction:.3f}."
    )

    return (
        error_negative * is_negative
        + error_digits * is_not_three_digit
        + valid_result * is_valid
    )


doctest.testmod()

entered_number = int(input("Enter a three-digit number: "))

result = number_operations(number=entered_number)
print(result)
