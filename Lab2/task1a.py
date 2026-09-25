import doctest


def check_point_belonging(x: float, y: float) -> bool:
    """
    Checks whether a point belongs to the given area.

    :param x: float
    :param y: float
    :return: bool

    >>> check_point_belonging(0, 0)
    True

    >>> check_point_belonging(6, 5)
    True

    >>> check_point_belonging(7, 5)
    True

    >>> check_point_belonging(-5, -5)
    False

    >>> check_point_belonging(5, -5)
    False

    >>> check_point_belonging(-4, 5)
    False

    >>> check_point_belonging(5, 0)
    False

    >>> check_point_belonging(0, 5)
    True

    >>> check_point_belonging(-5, 0)
    True

    >>> check_point_belonging(0, -5)
    False

    >>> check_point_belonging(10, 10)
    False

    >>> check_point_belonging(-10, 10)
    False

    >>> check_point_belonging(10, -10)
    False

    >>> check_point_belonging(-10, -10)
    False

    >>> check_point_belonging(2.5, 3.5)
    True

    >>> check_point_belonging(6.5, 4.5)
    True
    """

    cond_1st = (x >= 0) and (y >= 0) and (y <= 5) and (y >= 0.7 * x - 1.4)
    cond_2nd = (x < 0) and (y > 0) and ((x**2) + (y**2) <= 25)
    cond_3rd = (
        (x <= 0)
        and (y <= 0)
        and ((x**2) + (y**2) <= 25)
        and (y >= (7 / 3) * x + (35 / 3))
        and (y >= 0.7 * x - 1.4)
    )
    cond_4th = (x > 0) and (y < 0) and (y >= 0.7 * x - 1.4)

    return cond_1st or cond_2nd or cond_3rd or cond_4th


doctest.testmod()

x = float(input("Enter X coordiantes: "))
y = float(input("Enter Y coordiantes: "))

print(check_point_belonging(x, y))
