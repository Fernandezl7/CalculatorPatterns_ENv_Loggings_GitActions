'''Divide Command'''
from app.command import Command

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            raise ValueError("Unable to divide by 0")
        else:
            print(f"The result of Dividing {self.a} / {self.b} = {self.a / self.b}")

def register():
    return DivideCommand