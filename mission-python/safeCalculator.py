def main():
    while True:
        try:
            operand1 = get_integer("Enter first number: ")

            if operand1 == None:
                break

            operator = get_operand("Enter operator (+, -, *, /): ")
            operand2 = get_integer("Enter second number: ")

            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            else:
                result = operand1 / operand2
            
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        else:
            print(f"Result = {result}")

    print("Goodbye!")

def get_integer(prompt):
    while True:
        try:
            value = input(prompt)

            if value.lower() == 'q':
                return None
            
            return int(value)
        except ValueError:
            print("Invalid number.")


def get_operand(prompt):
    while True:
        try:
            value = input(prompt)
            # if value == '+' or value == '-' or value == '*' or value == '/':
            if value in ['+', '-', '*', '/']:
                return value
            else:
                raise ValueError("Invalid operator.")
        except ValueError as e:
            print(e)
main()