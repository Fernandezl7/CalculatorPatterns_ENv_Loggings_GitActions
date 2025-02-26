'''Greeting Command'''
from app.command import Command


class GreetCommand(Command):
    def execute(self):
        print("Hello World!")
