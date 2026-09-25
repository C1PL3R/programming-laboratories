import doctest
import math


def body_moving(H: float, v0: float, alpha: float, t: float) -> str:
    """Finds the coordinates and speed of the body at the time moment t,

    the maximum height and the maximum length of the trajectory.

    The body is thrown from the height H with the initial speed v0
    at the angle alpha to the horizontal.

    >>> body_moving(0.0, 20.0, 90.0, 2.0) == (
    ...     'Coordinates of the body at the time moment 2.00 '
    ...     'are 0.00 and 20.00;\\n'
    ...     'the speed of the body at the time moment 2.00 is 0.00;\\n'
    ...     'the maximum height is 20.00;\\n'
    ...     'the maximum length is 0.00.'
    ... )
    True

    >>> body_moving(45.0, 15.0, 0.0, 1.0) == (
    ...     'Coordinates of the body at the time moment 1.00 '
    ...     'are 15.00 and 40.00;\\n'
    ...     'the speed of the body at the time moment 1.00 is 18.03;\\n'
    ...     'the maximum height is 45.00;\\n'
    ...     'the maximum length is 0.00.'
    ... )
    True

    >>> body_moving(0.0, 10.0, 45.0, 1.0) == (
    ...     'Coordinates of the body at the time moment 1.00 '
    ...     'are 7.07 and 2.07;\\n'
    ...     'the speed of the body at the time moment 1.00 is 7.65;\\n'
    ...     'the maximum height is 2.50;\\n'
    ...     'the maximum length is 10.00.'
    ... )
    True

    >>> body_moving(100.0, 0.0, 45.0, 2.0) == (
    ...     'Coordinates of the body at the time moment 2.00 '
    ...     'are 0.00 and 80.00;\\n'
    ...     'the speed of the body at the time moment 2.00 is 20.00;\\n'
    ...     'the maximum height is 100.00;\\n'
    ...     'the maximum length is 0.00.'
    ... )
    True

    >>> body_moving(34.5, 10.0, 90.0, 0.0) == (
    ...     'Coordinates of the body at the time moment 0.00 '
    ...     'are 0.00 and 34.50;\\n'
    ...     'the speed of the body at the time moment 0.00 is 10.00;\\n'
    ...     'the maximum height is 39.50;\\n'
    ...     'the maximum length is 0.00.'
    ... )
    True

    >>> body_moving(-50, 10.0, 90.0, 0.0)
    'Height H must be positive number'

    >>> body_moving(50, -10.0, 90.0, 0.0)
    'Speed v0 must be positive number'

    >>> body_moving(-50, -10.0, 90.0, 0.0)
    'Height H and speed v0 must be positive numbers'

    >>> body_moving(50, 10.0, 90.0, -1.0)
    'Time moment t must be positive number'

    >>> body_moving(-50, -10.0, 90.0, -1.0)
    'Height H, speed v0 and time moment must be positive numbers'

    >>> body_moving(-50, 10.0, 90.0, -1.0)
    'Height H and time moment must be positive numbers'

    >>> body_moving(50, -10.0, 90.0, -1.0)
    'Speed v0 and time moment must be positive numbers'
    """
    g: float
    x: float
    y: float
    vx: float
    vy: float
    v: float
    Hmax: float
    L: float

    g = 10.0
    if H < 0 and v0 < 0 and t < 0:
        return "Height H, speed v0 and time moment must be positive numbers"
    elif H < 0 and t < 0:
        return "Height H and time moment must be positive numbers"
    elif v0 < 0 and t < 0:
        return "Speed v0 and time moment must be positive numbers"
    elif H < 0 and v0 < 0:
        return "Height H and speed v0 must be positive numbers"
    elif H < 0:
        return "Height H must be positive number"
    elif v0 < 0:
        return "Speed v0 must be positive number"
    elif t < 0:
        return "Time moment t must be positive number"
    else:
        # Converting degrees to radians / Переведення градусів у радіани
        alpha_rad = math.radians(alpha)

        # Equation of motion along the OX axis / Рівняння руху вздовж осі OX
        x = (v0 * math.cos(alpha_rad)) * t

        # Equation of motion along the OY axis / Рівняння руху вздовж осі OY
        y = ((v0 * math.sin(alpha_rad)) * t) - ((g * (t**2)) / 2) + H

        # Velocity projection onto the OX axis / Проєкція швидкості на вісь OX
        vx = v0 * math.cos(alpha_rad)

        # Velocity projection onto the OY axis / Проєкція швидкості на вісь OY
        vy = v0 * math.sin(alpha_rad) - (g * t)

        # Magnitude of the body's velocity / Модуль швидкості тіла
        v = math.sqrt((vx**2) + (vy**2))

        # Maximum lifting height / Максимальна висота підйому
        Hmax = (((v0**2) * (math.sin(alpha_rad) ** 2)) / (2 * g)) + H

        # Horizontal flight range / Дальність польоту по горизонталі
        L = ((v0**2) * math.sin(2 * alpha_rad)) / g

        result_text = (
            f"Coordinates of the body at the time moment {t:.2f} "
            f"are {x:.2f} and {y:.2f};\n"
            f"the speed of the body at the time moment {t:.2f} "
            f"is {v:.2f};\n"
            f"the maximum height is {Hmax:.2f};\n"
            f"the maximum length is {L:.2f}."
        )
        return result_text


doctest.testmod()

H_in: float
H_in = float(input("Enter H: "))

v0_in: float
v0_in = float(input("Enter v0: "))

alpha_in: float
alpha_in = float(input("Enter alpha: "))

t_in: float
t_in = float(input("Enter t: "))

result: str
result = body_moving(H_in, v0_in, alpha_in, t_in)

print(result)
