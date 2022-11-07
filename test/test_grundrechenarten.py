import pytest
from grundlagen.mathematische_grundlagen.grundrechenarten import *


class TestGrundrechenarten:
    @pytest.mark.parametrize("test_input,expected", [(0, 0), (-42, 0), (42, 2)])
    def test_get_digit_num_of_decimal_pass(self, test_input, expected):
        digits = get_digit_num_of_decimal(number=test_input)
        assert digits == expected

    @pytest.mark.parametrize("test_input,expected", [(0.0, pytest.raises(TypeError)),
                                                     (-0.42, pytest.raises(TypeError)),
                                                     (0.42, pytest.raises(TypeError)),
                                                     ("foobar", pytest.raises(TypeError))])
    def test_get_digit_num_of_decimal_fail(self, test_input, expected):
        with pytest.raises(Exception):
            assert get_digit_num_of_decimal(number=test_input)

    @pytest.mark.parametrize("test_input,expected", [(0.0, 0), (1, 1), (-0.42, 0),
                                                     (0.42, 0), (42.42, 2)])
    def test_get_digit_num_pass(self, test_input, expected):
        assert get_digit_num(number=test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [("foobar", pytest.raises(TypeError))])
    def test_get_digit_num_fail(self, test_input, expected):
        with pytest.raises(Exception):
            assert get_digit_num(number=test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [(0, [0]), (1, [1]), (42, [2, 4])])
    def test_extract_digits_pass(self, test_input, expected):
        assert extract_digits(number=test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [("foobar", pytest.raises(TypeError))])
    def test_extract_digits_fail(self, test_input, expected):
        with pytest.raises(Exception):
            assert extract_digits(number=test_input) == expected
