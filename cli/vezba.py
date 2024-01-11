def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cant divide by 0"
    return x / y

# user input --> functions
operation_dict = {
    "add":add,
    "subtact": subtract,
    "multiply": multiply,
    "divide": divide,
}

def main():
    while True:
        print("Options:")
        print("Enter 'add' for add for addition")
        print("Enter 'subtract' for subtraction ")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' for to end ther program")

        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in operation_dict:
            num1 = float(input("Enter the first number:"))
            num2 = float(input("Enter the second number:"))
            operation = operation_dict[user_input]
            result = operation(num1, num2)
            print("Result: ", result)
        else:
            print("Invalid input")
            




