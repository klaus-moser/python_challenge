import pytest
from grundlagen.mathematische_grundlagen.grundrechenarten import *


@pytest.mark.parametrize("test_input,expected", [(0, 0), (-42, 0), (42, 2)])
def test_grundrechenarten_pass(test_input, expected):
    digits = get_digit_num_of_decimal(number=test_input)
    assert digits == expected


@pytest.mark.parametrize("test_input,expected", [(-0.42, pytest.raises(TypeError)),
                                                 (0.42, pytest.raises(TypeError))])
def test_grundrechenarten_fail(test_input, expected):
    with pytest.raises(Exception):
        assert get_digit_num_of_decimal(number=test_input)
