def perform_addition():
    print("=" * 35)
    print("   PYTHON ADDITION CALCULATOR   ")
    print("=" * 35)
    
    try:
        # Prompt user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = num1 + num2
        
        # Display formatted output
        if result.is_integer():
            print(f"\nResult: {int(num1)} + {int(num2)} = {int(result)}")
        else:
            print(f"\nResult: {num1} + {num2} = {result}")
            
    except ValueError:
        print("\nInvalid input! Please enter valid numeric values.")

if __name__ == "__main__":
    perform_addition()
    