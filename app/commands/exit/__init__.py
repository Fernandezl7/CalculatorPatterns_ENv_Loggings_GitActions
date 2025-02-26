'''Exit Command'''
import sys
from app.command import Command


class ExitCommand(Command):
    def execute(self):
        sys.exit("Exiting...Goodbye!!!!!")

def register():
    return ExitCommand
