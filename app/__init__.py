import pkgutil
import importlib
import logging
from app.command import CommandHandler
from app.command import Command

#from app.plugins.menu import MenuCommand
import multiprocessing
#from dotenv import load_dotenv
import os



class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.plugins = []  # List to store the names of loaded plugins
   
    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        #if issubclass(item, (Command)) and item is not Command:  # Added extra condition as it was registering the command twice
                            if plugin_name == "Menu":
                                self.command_handler.register_command(plugin_name, item(self.command_handler))
                            else:
                                self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
            
    def start(self):
        self.load_plugins()
        print("\nOption To Perform Interative Calculation:")
        print("        ")
        self.command_handler.execute_command("Menu")

        choice = input("Choose an option : ")
        while True:   #REPL Read, Evaluate, Print, Loop
            try:
                if choice == 'C':
                    #self.command_handler.execute_command("Menu")
                    choice = input("Choose an option : ")
                    continue
                elif choice == 'Add':
                    a = float(input("   Enter the first number: "))
                    b = float(input("   Enter the second number: "))
                    Add_command = self.command_handler.create_command('Add', a, b)
                    result = self.command_handler.execute_command('Add')
                elif choice == 'Subtract':
                    a = float(input("   Enter the first number: "))
                    b = float(input("   Enter the second number: "))
                    Subtract_command = self.command_handler.create_command('Subtract', a, b)
                    result = self.command_handler.execute_command('Subtract')
                elif choice == 'Multiply':
                    a = float(input("   Enter the first number: "))
                    b = float(input("   Enter the second number: "))
                    Multiply_command = self.command_handler.create_command('Multiply', a, b)
                    result = self.command_handler.execute_command('Multiply')
                elif choice == 'Divide':
                    a = float(input("   Enter the first number: "))
                    b = float(input("   Enter the second number: "))
                    Divide_command = self.command_handler.create_command('Divide', a, b)
                    result = self.command_handler.execute_command('Divide')
                elif choice == 'Exit' or choice == 'E':
                    exit_command = self.command_handler.create_command('Exit')
                    result = self.command_handler.execute_command('Exit')
                elif choice == 'Greet':
                    Greet_command = self.command_handler.create_command('Greet')
                    result = self.command_handler.execute_command('Greet')
                elif choice == 'Menu':
                    result = self.command_handler.execute_command('Menu')
                else:
                    logging.info("Invalid choice. Please select a valid option.")
                    print("Invalid choice. Please select a valid option.")
            except ZeroDivisionError:
                logging.info("Error: Division by zero")
                print("Error: Division by zero.")
            except ValueError as e:
                print(e)
            except Exception as e:
                print(f"An error occurred: {e}")
            print(" ")
            print("Type C : to Continue , Type E : to Exit  ")

            choice = input("")


def start_app():
    app = App()
    app.start()

if __name__ == "__main__":
    multiprocessing.Process(target=start_app).start()
