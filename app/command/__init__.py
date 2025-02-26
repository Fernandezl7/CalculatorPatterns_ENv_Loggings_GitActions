import importlib
from abc import ABC, abstractmethod

# Command interface definition
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# CommandHandler class
class CommandHandler:
    def __init__(self):
        self.commands = {}  # Dictionary to store command instances
    
    def register_command(self, command_name: str, command_instance: Command):
        self.commands[command_name] = command_instance  # Store command instance by name

    def execute_command(self, command_name: str):
        if command_name in self.commands:
            self.commands[command_name].execute()  # Execute the command instance
        else:
            print(f"No such command: {command_name}")

    def load_plugin(self, plugin_name):
        # Dynamically load plugin from the plugins folder
        try:
            plugin_module = importlib.import_module(f"app.plugins.{plugin_name}")
            command_class = plugin_module.register()  # Ensure register() returns a Command class
            return command_class  # Return the class, not an instance
        except ImportError as e:
            print(f"Failed to load plugin {plugin_name}: {e}")
        except AttributeError:
            print(f"Plugin {plugin_name} is missing the 'register()' function.")
            raise

    def create_command(self, plugin_name, *args):
        command_class = self.load_plugin(plugin_name)  # Load the plugin's command class
        if command_class:
            command_instance = command_class(*args)  # Instantiate the command class
            self.register_command(plugin_name, command_instance)  # Register the instance
            return command_instance
        else:
            raise ValueError(f"Failed to create command: {plugin_name}")
    def list_commands(self):
        print("              ")
        print("Available Calculator Commands:")
        print(" ")

        for key in self.commands:
            print(f"        Type {key} : To Perform {key} Operation ")
        print(" ")


    # Creating a dictionary
    my_Menu_dict = {
        'Greet' : '1',
        'Menu' : '2',
        'Add' : '3',
        'Subtract' : '4',
        'Multiply' : '5',
        'Divide' : '6',
        'Exit' :  '7'
    }