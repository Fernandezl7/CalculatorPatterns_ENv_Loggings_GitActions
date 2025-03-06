'''Exit Command'''
import sys
import logging
from app.command import Command


class ExitCommand(Command):
    def execute(self):
        logging.info("Exiting...Goodbye!!!!!")
        sys.exit("Exiting...Goodbye!!!!!")

def register():
    return ExitCommand