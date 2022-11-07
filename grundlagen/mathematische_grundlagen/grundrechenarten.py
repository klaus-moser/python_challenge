def get_digit_num_of_decimal(number: int) -> int:
    """
    Get the number of digits of a number through using the modulo.
    :param number: Integer number.
    :return: Integer number of digits.
    """

    if not isinstance(number, int):  # check type
        raise TypeError("Number is not integer/decimal")

    digits = 0

    while number > 0:
        number = number // 10  # division without rest
        digits += 1

    return digits


def get_digit_num(number) -> int:
    """
    Returns the number of whole digits (before the
    comma) of any number (int, float, etc.).
    :param number: Any number.
    :return: Integer number.
    """

    if isinstance(number, str):
        raise TypeError("Only int, float allowed.")

    digits = 0
    rem_value = number

    while rem_value >= 1:
        rem_value, _ = divmod(rem_value, 10)
        digits += 1

    return digits
