# Calculator Application
print("\n\tWelcome to My Simple Calculator Application")

operator = input ("\nEnter an Operator ( + - / * ): ")

try:
    num1 = float(input("\nEnter The 1st Number : "))
    num2 = float(input("Enter The 2st Number : "))
    if operator == "+":
        print(f"Sum Result : {num1+num2:.2f}")

    elif operator == "-":
        print(f"Substraction Result : {num1-num2:.3f}")

    elif operator == "*":
        print(f"Multiplication Result : {num1*num2:.3f}")

    elif operator == "/":
        
        try:
            print(f"Division Result : {num1/num2:.3f}")
        except ZeroDivisionError:
            print("\n\tCan't Divided By Zero :(")

    else:
        print(f"\n\t{operator} is not a valid operator -_^")

except ValueError:
    print("\n\tPlease Enter A Number Only!")


print('\n\tThank You For Using My Application :)\n')