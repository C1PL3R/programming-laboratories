import doctest


def pi_gregory(n_digits: int) -> str:
    """Calculates pi using the Gregory-Leibniz formula up to n_digits after the decimal point.

    >>> pi_gregory(1)
    'The Gregory formula gives value 3.3 with the accuracy 1 digits after the decimal point by using 5 members of series.'

    >>> pi_gregory(2)
    'The Gregory formula gives value 3.12 with the accuracy 2 digits after the decimal point by using 50 members of series.'

    >>> pi_gregory(3)
    'The Gregory formula gives value 3.140 with the accuracy 3 digits after the decimal point by using 500 members of series.'

    >>> pi_gregory(4)
    'The Gregory formula gives value 3.1414 with the accuracy 4 digits after the decimal point by using 5000 members of series.'

    >>> pi_gregory(5)
    'The Gregory formula gives value 3.14157 with the accuracy 5 digits after the decimal point by using 50000 members of series.'

    >>> pi_gregory(6)
    'The Gregory formula gives value 3.141591 with the accuracy 6 digits after the decimal point by using 500000 members of series.'

    >>> pi_gregory(7)
    'The Gregory formula gives value 3.1415925 with the accuracy 7 digits after the decimal point by using 5000000 members of series.'

    >>> pi_gregory(8)
    'The Gregory formula gives value 3.14159263 with the accuracy 8 digits after the decimal point by using 50000000 members of series.'

    # >>> pi_gregory(9)
    # 'The Gregory formula gives value 3.141592652 with the accuracy 9 digits after the decimal point by using 500000000 members of series.'
    #
    # >>> pi_gregory(10)
    # 'The Gregory formula gives value 3.1415926534 with the accuracy 10 digits after the decimal point by using 5000000000 members of series.'
    # """
    eps = 4.0 * (10 ** (-n_digits))
    k = 1
    a_prev = 4
    value = 4

    while True:
        an = -a_prev * (2*k - 1) / (2*k + 1)
        a_prev = an
        if abs(an) < eps:
            break
        value += + an
        k += 1

    formatted_value = f"{value:.{n_digits}f}"

    return (
        f"The Gregory formula gives value {formatted_value} "
        f"with the accuracy {n_digits} digits after the decimal point by using {k} members of series."
    )


def pi_wallis(n_digits: int) -> str:
    """Calculates pi using the Wallis product up to n_digits after the decimal point.

    >>> pi_wallis(1)
    'The Vallis formula gives value 3.1 with the accuracy 1 digits after the decimal point by using 15 members of series.'

    >>> pi_wallis(2)
    'The Vallis formula gives value 3.14 with the accuracy 2 digits after the decimal point by using 157 members of series.'

    >>> pi_wallis(3)
    'The Vallis formula gives value 3.142 with the accuracy 3 digits after the decimal point by using 1571 members of series.'

    >>> pi_wallis(4)
    'The Vallis formula gives value 3.1416 with the accuracy 4 digits after the decimal point by using 15708 members of series.'

    >>> pi_wallis(5)
    'The Vallis formula gives value 3.14159 with the accuracy 5 digits after the decimal point by using 157079 members of series.'

    >>> pi_wallis(6)
    'The Vallis formula gives value 3.141593 with the accuracy 6 digits after the decimal point by using 1570796 members of series.'

    >>> pi_wallis(7)
    'The Vallis formula gives value 3.1415927 with the accuracy 7 digits after the decimal point by using 15707963 members of series.'

    >>> pi_wallis(8)
    'The Vallis formula gives value 3.14159265 with the accuracy 8 digits after the decimal point by using 157079632 members of series.'

    # >>> pi_wallis(9)
    # 'The Vallis formula gives value 3.141592653 with the accuracy 9 digits after the decimal point by using 1570796326 members of series.'
    #
    # >>> pi_wallis(10)
    # 'The Vallis formula gives value 3.1415926536 with the accuracy 10 digits after the decimal point by using 15707963267 members of series.'
    # """
    eps = 10 ** (-n_digits)
    dn = 1 / 3  # це (a_1 - 1) = 4/3 - 1
    value = 2 * (1 + dn)
    n = 1
    cond = 1.0

    while cond >= eps:
        n += 1
        dn = dn * (2 * n - 3) / (2 * n + 1)
        value *= (1 + dn)
        cond = (2 * n - 1) * value * dn

    pi_with_error = value + cond / 2

    return (
        f"The Vallis formula gives value {round(pi_with_error, n_digits)} "
        f"with the accuracy {n_digits} digits after the decimal point by using {n} members of series."
    )


doctest.testmod(verbose=True)

print(pi_wallis(4))