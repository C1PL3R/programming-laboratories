def calculate_power(k, x) -> float:
    result = 1.0
    while k > 0:
        if k % 2 != 0:
            result *= x
        x *= x
        k //= 2

    return result

print(calculate_power(k=3, x=2))
