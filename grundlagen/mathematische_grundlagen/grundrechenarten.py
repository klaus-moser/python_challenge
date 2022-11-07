
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
