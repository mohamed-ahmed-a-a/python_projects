print("\n\t<-- Welcome To Adventure Game -->\n")

name = input("Type Your Name : ").strip().capitalize()
print("Welcome" , name , "To This Advanture :)\n")

answer = input(
    "You are on a dirt road , it has come to an end and you can go \
left or right. Which way would you like to go ? ").strip().lower()

if answer == "left":
    answer = input("\nYou come to a river , you can walk around \
it or swim accross?(walk/swim)").strip().lower()
    
    if answer == "swim":
        print("\nYou swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("\nYou walked for many miles, ran out of water and you lost the game")
    else:
        print("Not A Valid Option. You lose -_-")  


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you to cross it or head back (cross/back) ? ").strip().lower()

    if answer == "back":
        print("\nYou go back and lose.")
    elif answer == "cross":
        answer = input("\nYou cross the bridge and meet a stranger. Do you talk to them(yes/no)? ").strip().lower()
        
        if answer == "yes":
            print("You talk to stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("\nNot A Valid Option. You lose -_-")
    else:
        print("\nNot A Valid Option. You lose -_-")

else:
    print("\nNot A Valid Option . You lose -_^")


print("\n\tThank you for tring" , name)