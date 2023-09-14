def add(a, b):
    """
    This function takes two numbers and returns their sum

    Parameters:
    a (int): Te first number
    b (int): The second number

    Returns:
    int: The sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    This function takes two numbers and returns their difference

    Parameters:
    a (int): Te first number
    b (int): The second number

    Returns:
    int: The difference of a and b
    """
    return a - b

def multiply(a, b):
    """
    This function takes two numbers and returns their multiplication

    Parameters:
    a (int): Te first number
    b (int): The second number

    Returns:
    int: The multiplication of a and b
    """
    return a * b

def divide(a, b):
    """
    This function takes two numbers and returns their division

    Parameters:
    a (int): Te first number
    b (int): The second number

    Returns:
    int: The division of a and b
    """
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is the first number?: "))
for operand in operations:
    print(operand)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What is the second number?: "))

calculator_function = operations[operation_symbol]
answer = calculator_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")