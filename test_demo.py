import pytest
from pytest import mark


@pytest.fixture
def input_value():
    input = 15
    return input


def test_div_3(input_value):
    input_value % 3 == 0


def test_div_5(input_value):
    input_value % 5 == 0


@mark.parametrize("num1, num2 ,expected",
                  [(2, 5, 7),
                   (3, 7, 10)])
@pytest.mark.regression
def test_addition(num1, num2, expected):
    assert num1 + num2 == expected


@pytest.mark.skip
def test_skip():
    pass
