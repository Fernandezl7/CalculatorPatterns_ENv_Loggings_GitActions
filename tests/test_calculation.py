'''Test Calculation'''
from decimal import Decimal
import pytest
from app.calculator.calculation import Calculation
from app.calculator.operations import add,divide
# pylint: disable=unnecessary-dunder-call, invalid-name

def test_calculation_operations(a, b, operation, expected):
    '''Test Calculation Operation'''
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"
def test_calculation_repr():
    '''Test the string representation (__repr__) of Calculation class'''
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation (10, 5, add)"
    assert calc.__repr__() == expected_repr, "The __repr__ output does not match"
def test_divide_by_zero():
    '''Test division by zero to ensure it raises ValueError'''
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match= "Cannot divide by zero"):
        calc.perform()
