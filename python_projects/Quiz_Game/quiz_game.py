print("\n\t<-- Welcome to My Computer Quiz -->\n")

playing = input("Do You Want to play? ")

if playing.lower() != "yes" and playing.lower() != "y":
    quit() 

print("Okay! Let's Play :)\n")


def questions():
    
    score = 0

    answer = input("What CPU stands for? ").strip().lower()
    if answer == "centeral proccessing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What GPU stands for? ").strip().lower()
    if answer == "graphichs proccessing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What RAM stands for? ").strip().lower()
    if answer == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What PSU stands for? ").strip().lower()
    if answer == "power supply":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What IP stands for? ").strip().lower()
    if answer == "internet protocol":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")


    print(f"\nYou Got : {str((score/5) * 100)} %.\n")

questions()

print("\t<-- Thank You for using my Application ^_^ -->\n")