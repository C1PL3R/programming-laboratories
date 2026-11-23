import doctest


def time_operations(seconds: int) -> str:
    """
    Calculates the number of days, hours, minutes and seconds
    in the given duration and creates a formatted representation.

    :param seconds: int

    >>> time_operations(93784)
    'The duration of the mission is 1 days, 2 hours, 3 minutes and 4 seconds;\\nthe formatted duration is 1 days, 02:03:04.'

    >>> time_operations(90061)
    'The duration of the mission is 1 days, 1 hours, 1 minutes and 1 seconds;\\nthe formatted duration is 1 days, 01:01:01.'

    >>> time_operations(172865)
    'The duration of the mission is 2 days, 0 hours, 1 minutes and 5 seconds;\\nthe formatted duration is 2 days, 00:01:05.'

    >>> time_operations(1000000)
    'The duration of the mission is 11 days, 13 hours, 46 minutes and 40 seconds;\\nthe formatted duration is 11 days, 13:46:40.'

    >>> time_operations(59)
    'The duration of the mission is 0 days, 0 hours, 0 minutes and 59 seconds;\\nthe formatted duration is 0 days, 00:00:59.'

    >>> time_operations(-100)
    'Number of seconds must be non-negative'
    """

    is_valid = int(seconds >= 0)
    is_negative = 1 - is_valid

    count_of_days = seconds // 86400
    seconds = seconds % 86400

    count_of_hours = seconds // 3600
    seconds = seconds % 3600

    count_of_minutes = seconds // 60
    count_of_seconds = seconds % 60

    result = (
        f"The duration of the mission is {count_of_days} days, {count_of_hours} hours, {count_of_minutes} minutes and {count_of_seconds} seconds;\n"
        f"the formatted duration is {count_of_days} days, {count_of_hours:02d}:{count_of_minutes:02d}:{count_of_seconds:02d}."
    )

    error = "Number of seconds must be non-negative"

    return (error * is_negative) + (result * is_valid)


doctest.testmod()

entered_seconds = int(input("Enter duration in seconds: "))
print(time_operations(entered_seconds))
