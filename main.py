import sys
from decimal import Decimal, InvalidOperation
from app.calculator import Calculator

class OperationCommand:
    def __init__(self, calculator, operation_name, a, b):
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        # Retrieve the operation method from the Calculator class using getattr
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            return operation_method(self.a, self.b)
        else:
            raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(a, b, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command = OperationCommand(Calculator(), operation_name, a_decimal, b_decimal)
        result = command.execute()
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Interactive Calculator Mode:")
    while True:
        # Get input from the user
        try:
            a = input("Enter the first number (or type 'exit' to quit): ")
            if a.lower() == 'exit':
                break
            
            b = input("Enter the second number: ")
            operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

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
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"An error occurred: {e}")
if __name__ == '__main__':
    main()
