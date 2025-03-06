'''Menu Command'''
import logging
from app.command import Command
from app.command import CommandHandler

class MenuCommand(Command):
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        logging.info
        self.command_handler.list_commands(f"Listing Below the Available Menu Commands in Calculator Application")

def register():
    return MenuCommand  # Return the class, not an instance