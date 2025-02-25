from decimal import Decimal
from typing import Callable
from app.calculator.operations import add, subtract, multiply, divide

class Calculation:
    '''CALCULATION CLASS'''
    def __init__(self, a:Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        self.a = a
        self.b = b
        #store operation as callable that takes two decimals and returns one
        self.operation = operation
    #New instance of calculation
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        return Calculation(a, b, operation)
    @staticmethod
    def perform