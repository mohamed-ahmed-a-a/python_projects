print("\n\t<-- Welcome To Number Gusser Application -->\n\n")
import random

top_of_range = input("Type a Range : ").strip()

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type Number larger than 0 next time.")
        quit()
else:
    print("Please Enter a number next time.")
    quit()

random_number = random.randint(0,top_of_range)

guesses = 0
while True:
    guesses +=1
    user_guess = input("\nmake a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please Enter a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess < random_number:
        print("try a greater number")
    else:
        print("try a lower number")


print(f"\nYou got it in {guesses} guesses")
print("\n\t<-- Thank You For using My Application :) -->")