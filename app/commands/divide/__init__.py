'''Divide Command'''
import logging
from app.command import Command

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        try:
            if self.b == 0:
                raise ValueError("Unable to divide by 0")
            print(f"The result of Dividing {self.a} / {self.b} = {self.a / self.b}")
            logging.info(f"The result of dividing {self.a} / {self.b} = {self.a / self.b}")
        
        except ValueError as e:
            logging.error(f"Error: {e}")
            raise 

def register():
    return DivideCommand