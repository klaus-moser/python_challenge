
def get_digit_num(number: int) -> int:
    """
    Get the number of digits of a number through using the modulo.
    :param number: Integer number.
    :return: Integer number of digits.
    """
    digits = 0

    while number % 10 != 0:
        number = int(number / 10)
        digits += 1

    return digits
