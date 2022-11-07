import pytest
from grundlagen.mathematische_grundlagen.grundrechenarten import *

num = 1000

print(num)
digits = get_digit_num(number=num)
assert digits == 4

