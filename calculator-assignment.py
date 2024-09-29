def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y


def display_menu():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")


def calculator():
    while True:
        display_menu()
        choice = input("Enter choice (1-6) or 'q' to quit: ")
        
        if choice == 'q':
            print("Exiting calculator.")
            break
        
       
        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == '1':
                print(f"The result of addition is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of multiplication is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of division is: {divide(num1, num2)}")
            elif choice == '5':
                print(f"The result of modulus is: {modulus(num1, num2)}")
            elif choice == '6':
                print(f"The result of exponentiation is: {exponentiate(num1, num2)}")
        else:
            print("Invalid choice. Please select a valid operation.")

calculator()
