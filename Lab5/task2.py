import math
import doctest


def taylor_sin(x_deg: float, eps: float) -> str:
    """Обчислює sin(x) за допомогою розкладу у ряд Тейлора з точністю eps
    без використання періодичності (без редукції кута за 2*pi).

    Аргументи:
        x_deg (float): Кут у градусах.
        eps (float): Задана точність (eps > 0).

    Повертає:
        str: Рядок у форматі "sin({x}) = {value} with accuracy {eps}; N = {N}"

    Examples:
        >>> taylor_sin(5.7, 0.001)
        'sin(5.7) = 0.099 with accuracy 0.001; N = 1'

        >>> taylor_sin(180, 1e-5)
        'sin(180) = 0.00000 with accuracy 1e-05; N = 8'

        >>> taylor_sin(540, 1e-5)
        'sin(540) = -0.00000 with accuracy 1e-05; N = 17'

        >>> taylor_sin(630, 1e-4)
        'sin(630) = -1.0000 with accuracy 0.0001; N = 18'

        >>> taylor_sin(-720, 1e-5)
        'sin(-720) = 0.00000 with accuracy 1e-05; N = 21'

        >>> taylor_sin(-987.65, 1e-4)
        'sin(-987.65) = 0.9992 with accuracy 0.0001; N = 26'

        >>> taylor_sin(1234.5, 1e-4)
        'sin(1234.5) = 0.4305 with accuracy 0.0001; N = 32'
    """
    x_rad = math.radians(x_deg)
    a_prev = x_rad
    n = 1
    value = x_rad


    while True:
        an = -a_prev * x_rad * x_rad / ((2 * n) * (2 * n + 1))

        value = value + an
        a_prev = an

        n += 1
        q =  (x_rad * x_rad) / (2 * n * (2 * n + 1))

        if q < 1 and (abs(an) / (1 - q)) < eps:
            break

    digits = round(-math.log10(eps))
    formatted_value = f"{value:.{digits}f}"

    return f"sin({x_deg}) = {formatted_value} with accuracy {eps}; N = {n - 1}"


doctest.testmod(verbose=True)

# x_deg: float | int = float(input("x_deg = "))
# eps: float = float(input("eps = "))
# print(taylor_sin(x_deg, eps))
