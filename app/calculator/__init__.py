'''Defines Calculator class for performing arithmetic operations'''
from decimal import Decimal
from typing import Callable
from app.calculator.calculations import Calculations
from app.calculator.operations import add, subtract, multiply, divide
from app.calculator.calculation import Calculation

class Calculator:
    @staticmethod
    def _perform_operation(a:Decimal,b:Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        '''CREATE AND PERFORM CALCULATION AND RETRUN RESULT'''
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        # Perform addition by delegating to the _perform_operation method with the add operation
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        # Perform subtraction by delegating to the _perform_operation method with the subtract operation
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        # Perform multiplication by delegating to the _perform_operation method with the multiply operation
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        # Perform division by delegating to the _perform_operation method with the divide operation
        return Calculator._perform_operation(a, b, divide)


