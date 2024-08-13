print("\t\t" , "=" * 42)
print("\t\t" , "=" * 4 + ">", "Guess The Number Application" , "<" + "=" * 4 )
print("\t\t" , "=" * 42)

import random


print("\n\t\t ==>^ Please Enter The Range That Do You Want ^<==\n")

start = int(input("Please Enter The Start : "))
end = int(input("Please Enter The End : "))


computer_choice = random.randint(start , end)

# print(computer_choice)

def guess():

    tries = 0
    
    while True:
        user_guess = int(input("\nGuess The Number : "))
        tries += 1

        if user_guess > computer_choice:
            print("Try Again! You guessed too high")

        elif user_guess < computer_choice:
            print("Try Again! You guessed too low")

        else:
            print(f"\nVery Good ^_^ , \'{user_guess}\' Is The Correct Number.")
            print(f"You took {tries} Tries to guess the number.")
            break

    if tries <=3 :
        print(f"You Are Very Fast , You Just Tried {tries} Times ^_^")
    else:
        pass

guess()


print("\n\t"+"==>" , "Thank You For Using My Application :)" , "<==")
