print("\t\t" , "=" * 40)
print("\t\t" , "=" * 4 , "Rock Paper Scissor Application" , "=" * 4 )
print("\t\t" , "=" * 40)

import random

choices = ("Rock"  , "Paper" , "Scissor")

print("\nPlease Choose : Rock | Paper | Scissor ")

user_input = input("Please Enter Your Choice : ").strip().capitalize()

computer_choice =random.choice(choices)

print(f"\nYou Choose : {user_input}")
print(f"Computer Choose : {computer_choice}")

def inputs():
    if user_input not in choices:
        print("\nInvalid Choice -_-\n")

    elif user_input == computer_choice:
        print("\nIt's A Tie ^_^\n")

    elif (user_input == "Rock"  and computer_choice == "Scissor") or \
        (user_input == "Paper" and computer_choice == "Rock") or \
        (user_input == "Scissor"  and computer_choice == "Paper"): 
        print("\nYou Win :)\n")
    else:
        print("\nComputer Win -_^\n")    

inputs()

print("==>" , "Thank You For Using My Application :)" ,"<==")