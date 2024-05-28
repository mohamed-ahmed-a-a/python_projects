print("\t\t" , "=" * 34)
print("\t\t" , "=" * 5 , "Calculator Application" , "=" * 5 )
print("\t\t" , "=" * 34)

print("\nIn This Application You Can Use : + | - | * | / | ^ | % \n")

first_num = int(input("\nPlease Enter First Number : "))
second_num = int(input("\nPlease Enter Second Number : "))
operation = input("\nPlease Enter The Operation : ").strip()


final = print(f"\nThe Final Operation : ({first_num} {operation} {second_num})")

choices = ('+' , '-' , '*' , '/' , '^' , '%')


def all_operations():
    if operation  not in choices:
        print("\nInvalid Operation -_^")

    elif operation == '+':
        print(f"\nThe Sum Of Two Numbers Is : {first_num + second_num}")
    elif operation == '-':
        print(f"\nThe Sub Of Two Numbers Is : {first_num - second_num}")
    elif operation == '*':
        print(f"\nThe Mul Of Two Numbers Is : {first_num * second_num}")
    elif operation == '/':
        try:
            print(f"\nThe Div Of Two Numbers Is : {first_num / second_num}")
        except:

            raise ZeroDivisionError("Sorry , Can't Divided By Zero -_^")
    elif operation == '^':
        print(f"\nThe Exp Of Two Numbers Is : {first_num ** second_num}")
    elif operation == '%':
        try:
            print(f"\nThe Mod Of Two Numbers Is : {first_num % second_num}")
        except:

            raise ZeroDivisionError("Sorry , Can't Make A Modules -_^")

all_operations()

print("\n====>" , "Thank You For Using My Application :)" ,"<=====")