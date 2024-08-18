# Calculator Application
print("\n\tWelcome to My Simple Calculator Application")

operator = input ("\nEnter an Operator ( + - / * ): ").strip()

try:
    num1 = float(input("\nEnter The 1st Number : ").strip())
    num2 = float(input("Enter The 2st Number : ").strip())
    if operator == "+":
        print(f"\nSum Result : {num1+num2:.2f}")

    elif operator == "-":
        print(f"\nSubstraction Result : {num1-num2:.3f}")

    elif operator == "*":
        print(f"\nMultiplication Result : {num1*num2:.3f}")

    elif operator == "/":
        
        try:
            print(f"\nDivision Result : {num1/num2:.3f}")
        except ZeroDivisionError:
            print("\n\tCan't Divided By Zero :(")

    else:
        print(f"\n\t{operator} is not a valid operator -_^")

except ValueError:
    print("\n\tPlease Enter A Number Only!")


print('\n\tThank You For Using My Application :)\n')