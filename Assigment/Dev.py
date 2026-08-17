def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Example Usage
if __name__ == "__main__":
    num1 = 15
    num2 = 5
    
    print(f"Numbers: {num1} and {num2}\n")
    print(f"Addition:       {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction:    {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    print(f"Division:       {num1} / {num2} = {divide(num1, num2)}")
    