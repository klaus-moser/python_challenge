import pytest
from grundlagen.mathematische_grundlagen.grundrechenarten import *


@pytest.mark.parametrize("test_input,expected", [(-1, 0), (1234, 4)])
def test_grundrechenarten(test_input, expected):

    digits = get_digit_num_of_decimal(number=test_input)
    assert digits == expected
