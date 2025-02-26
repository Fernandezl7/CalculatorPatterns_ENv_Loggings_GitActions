from decimal import Decimal
from typing import Callable
from app.calculator.operations import add, subtract, multiply, divide
class Calculation:
    '''CALCULATION CLASS'''
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        self.a = a
        self.b = b
        #store operation as callable that takes two decimals and returns one
        self.operation = operation
    #New instance of calculation
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        return Calculation(a, b, operation)
    def perform(self) -> Decimal:
        '''PERFORM STORED CALCULATION & RETURN RESULT'''
        return self.operation(self.a, self.b)
    def __repr__(self):
        '''RETURN SIMPLIFIED STRING REPRESENTATION OF CALCULATION'''
        return f"Calculation ({self.a}, {self.b}, {self.operation.__name__})"
    