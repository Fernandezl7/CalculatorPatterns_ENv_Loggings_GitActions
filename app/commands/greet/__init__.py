'''Greetings Command'''
import logging
from app.command import Command


class GreetCommand(Command):
    def execute(self):
        logging.info("Hello! Welcome To Interactive Calculato")
        print("     Hello! Welcome To Interactive Calculator")
def register():
    return GreetCommand
