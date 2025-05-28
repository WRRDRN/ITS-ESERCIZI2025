
from my_project.calculator import Calculator
import pytest

@pytest.fixture
def calculation(calculation):
    return Calculator(10,5)

def test_addicition(calculation):
    calculation: Calculator = Calculator (10,5)
    assert calculation.addition() == 13, 'the sum is w'

def test_subtraction(calculation):
    calculation: Calculator = Calculator (10,5)
    assert calculation.subtraction() == 5, 'the sum is w'

def test_multiplication(calculation):
    calculation: Calculator = Calculator (10,5)
    assert calculation.multiplication() == 50, 'the sum is w'


def test_division(calculation):
    calculation: Calculator = Calculator (10,5)
    assert calculation.division() == 2.00, 'the sum is w'