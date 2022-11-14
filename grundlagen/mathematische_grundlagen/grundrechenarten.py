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


def extract_digits(number) -> list:
    """
    Extract all digits before the comma.

    :param number: Number (int, float)
    :return: Array of digits.
    """

    if isinstance(number, str):
        raise TypeError("Only int, float allowed.")

    if number == 0:
        return [0]

    digits = []
    rem_value = number

    while rem_value > 0:
        rem_value, digit = divmod(rem_value, 10)
        digits.append(digit)

    return digits


def find_proper_divisors_set(number: int) -> set:
    """
    Find all the divisors of a given number without the
    number itself.

    :param number: Integer number.
    :return: Set with all the true divisors.
    """

    result = set()  # save to set (unordered, no duplicates)

    for i in range(1, number):
        if number % i == 0:
            result.add(i)

    return result


def find_proper_divisors_list(number: int) -> list:
    """
    Find all the divisors of a given number without the
    number itself.

    :param number:
    :return:
    """

    return [i for i in range(1, number) if number % i == 0]


def is_prime_number(number: int) -> bool:
    """
    Checks given number for prime status.

    :param number: Integer input.
    :return: True, if prime.
    """

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def get_prime_numbers(number: int) -> list:
    """
    Returns a list with all prime numbers in the range(0, number).

    :param number: Given end number.
    :return: List with all prime numbers.
    """

    return [i for i in range(number) if is_prime_number(i)]
