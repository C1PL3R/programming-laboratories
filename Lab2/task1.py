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
    y_line_bottom = y >= 0.7 * x - 1.4
    y_parallel_x = y <= 5
    y_ellipse = (x**2) / 64 + (y**2) / 25 <= 1
    y_line_top = y >= (7 / 3) * x + (35 / 3)

    return (
        ((y <= 0) and y_line_bottom and y_line_top)  # on picture - color red
        or (
            (x < 0) and (y > 0) and y_line_bottom and y_ellipse
        )  # on picture - color greed
        or ((x >= 0) and y_line_bottom and y_parallel_x)  # on picture - color blue
    )


doctest.testmod()

x = float(input("Enter X coordiantes: "))
y = float(input("Enter Y coordiantes: "))

print(check_point_belonging(x, y))
