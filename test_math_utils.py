import pytest
from math_utils import MathUtils


@pytest.fixture
def math_utils():
    return MathUtils()


def test_add(math_utils):
    assert math_utils.add(5, 3) == 8
    assert math_utils.add(-2, 2) == 0


def test_subtract(math_utils):
    assert math_utils.subtract(10, 4) == 6
    assert math_utils.subtract(3, 7) == -4


def test_multiply(math_utils):
    assert math_utils.multiply(4, 5) == 20
    assert math_utils.multiply(0, 10) == 0


def test_divide(math_utils):
    assert math_utils.divide(10, 2) == 5.0
    assert math_utils.divide(5, 0) == -1.0