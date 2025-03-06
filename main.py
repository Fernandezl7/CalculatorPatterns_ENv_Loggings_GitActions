import logging.config
import os
import socket
import logging
import sys
from dotenv import load_dotenv
from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app import App

class OperationCommand:
    def __init__(self, calculator, operation_name, a, b):
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.set_hostname_in_env()

    def get_computer_name(self):
        return socket.gethostname()

    def set_hostname_in_env(self):
        computer_name = self.get_computer_name()
        os.environ['HOSTNAME'] = computer_name
        logging.info(f"Hostname set to: {computer_name}")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info('Environment variables loaded')
        return settings

    def get_environment_variable(self):
        return self.settings.get('ENVIRONMENT', 'Not set')

    def get_hostname_variable(self):
        return self.settings.get('HOSTNAME', 'Not set')

    def print_env_variables(self):
        print(f"ENVIRONMENT: {self.get_environment_variable()}")
        print(f"HOSTNAME: {self.get_hostname_variable()}")

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Application started")
        logging.info("Logging configured")

    def execute(self):
        # Retrieve the operation method from the Calculator class using getattr
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            return operation_method(self.a, self.b)
        else:
            logging.error(f"Unknown operation: {self.operation_name}")
            raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(a, b, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command = OperationCommand(Calculator(), operation_name, a_decimal, b_decimal)
        logging.info(f"Performing {operation_name} Operation")
        result = command.execute()
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
        logging.error(f"Invalid number input: {a} or {b} is not a valid number")
    except ZeroDivisionError:
        print("Error: Division by zero.")
        logging.error("Error: Division by zero")
    except ValueError as e:
        print(e)
        logging.error(e)
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")

def main():
    print("Interactive Calculator Mode:")
    while True:
        try:
            a = input("Enter the first number (or type 'exit' to quit): ").strip()
            if a.lower() == 'exit':
                break
            
            b = input("Enter the second number: ").strip()
            operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

            # Validate inputs
            a_decimal = Decimal(a)
            b_decimal = Decimal(b)
            
            if operation not in ['add', 'subtract', 'multiply', 'divide']:
                print("Invalid operation! Please enter one of: add, subtract, multiply, divide.")
                continue

            # Perform the calculation and print the result
            calculate_and_print(a, b, operation)
        
        except InvalidOperation:
            print("Invalid number input, please enter valid numbers.")
            logging.error("Invalid number input in user input.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
            logging.error("User attempted division by zero.")
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"Unexpected error in main(): {e}")

if __name__ == '__main__':
    main()
