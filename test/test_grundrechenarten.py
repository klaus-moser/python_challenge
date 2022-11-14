import pytest
from grundlagen.mathematische_grundlagen.grundrechenarten import *


class TestGrundrechenarten:
    """
    Test class for all tests.
    """

    @pytest.mark.parametrize("test_input,expected", [(0, 0), (-42, 0), (42, 2)])
    def test_get_digit_num_of_decimal_pass(self, test_input, expected) -> None:
        """
        Method: get_digit_num_of_decimal. Pass.

        :param test_input: Input.
        :param expected: Expected result.
        :return:
        """

        # act
        digits = get_digit_num_of_decimal(number=test_input)
        # assert
        assert digits == expected

    @pytest.mark.parametrize("test_input,expected", [(0.0, pytest.raises(TypeError)),
                                                     (-0.42, pytest.raises(TypeError)),
                                                     (0.42, pytest.raises(TypeError)),
                                                     ("foobar", pytest.raises(TypeError))])
    def test_get_digit_num_of_decimal_fail(self, test_input, expected) -> None:
        """
        Method: get_digit_num_of_decimal. Fail.

        :param test_input: Input.
        :param expected: Expected result.
        :return:
        """

        # assert
        with pytest.raises(TypeError):
            assert get_digit_num_of_decimal(number=test_input)

    @pytest.mark.parametrize("test_input,expected", [(0.0, 0), (1, 1), (-0.42, 0),
                                                     (0.42, 0), (42.42, 2)])
    def test_get_digit_num_pass(self, test_input, expected) -> None:
        """
        Method: get_digit_num_pass. Pass.

        :param test_input: Input.
        :param expected: Expected result.
        :return:
        """

        # assert
        assert get_digit_num(number=test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [("foobar", pytest.raises(TypeError))])
    def test_get_digit_num_fail(self, test_input, expected) -> None:
        """
        Method: get_digit_num. Fail.

        :param test_input: Input.
        :param expected: Expected result.
        :return:
        """

        # assert
        with pytest.raises(Exception):
            assert get_digit_num(number=test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [(0, [0]), (1, [1]), (42, [2, 4])])
    def test_extract_digits_pass(self, test_input, expected) -> None:
        """
        Method: extract_digits. Pass.

        :param test_input: Input.
        :param expected: Expected result.
        :return:
        """

        # assert
        assert extract_digits(number=test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [("foobar", pytest.raises(TypeError))])
    def test_extract_digits_fail(self, test_input, expected) -> None:
        """
        Method: extract_digits. Fail.

        :param test_input: Test Input.
        :param expected: Expected result.
        :return:
        """

        # assert
        with pytest.raises(Exception):
            assert extract_digits(number=test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [(42, {1, 2, 3, 6, 7, 14, 21}), (0, set()), (-42, set())])
    def test_find_proper_divisors_set(self, test_input, expected) -> None:
        """
        Method: find_proper_divisors_set.

        :param test_input: Test Input.
        :param expected: Expected result.
        :return:
        """

        # act / assert
        assert expected == find_proper_divisors_set(number=test_input)

    @pytest.mark.parametrize("test_input,expected", [(24, [1, 2, 3, 4, 6, 8, 12]), (0, []), (-42, [])])
    def test_find_proper_divisors_list(self, test_input, expected) -> None:
        """
        Method: find_proper_divisors_list.

        :param test_input: Test Input.
        :param expected: Expected result.
        :return:
        """

        # act / assert
        assert expected == find_proper_divisors_list(number=test_input)

    @pytest.mark.parametrize("test_input,expected", [([3, 5, 7, 11, 13, 17, 19, 23], True)])
    def test_is_prime_numbers(self, test_input, expected) -> None:
        """
        Method: is_prime_number.

        :param test_input:  Test Input.
        :param expected:  Expected result.
        :return:
        """

        for i in test_input:
            # act / assert
            assert is_prime_number(number=i) is True

    @pytest.mark.parametrize("test_input,expected", [(25, [3, 5, 7, 11, 13, 17, 19, 23])])
    def test_get_prime_numbers(self, test_input, expected) -> None:
        """
        Method: get_prime_numbers.

        :param test_input:  Test Input.
        :param expected:  Expected result.
        :return:
        """

        # act / assert
        assert get_prime_numbers(number=test_input)
