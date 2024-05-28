print("\t\t" , "=" * 42)
print("\t\t" , "=" * 4 + ">", "Guess The Number Application" , "<" + "=" * 4 )
print("\t\t" , "=" * 42)

# First in First out 
print("\n\tThe Operation That You Can Do On Queue Is ")
print("\t==>\'Enqueue\' | \'Dequeue\' | \'Size\' | \'is empty\'\n")


class queue:
    def __init__(self ) -> None:
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self , item):
        self.items.insert( 0 ,item)
    def dequeue(self):
        if len(self.items) < 1:
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


one = queue()

def operations():

    while True:
        user_input = input("\nPlease Enter The Operation : ").strip().capitalize()

        if user_input == "Enqueue" :

            the_input = input("Please Enter The Element : ").strip()

            one.enqueue(the_input)

            print(f"\n\'{the_input}\' Is Inserted Successfully ")
            
            print(f"The Queue Elements : {one}")


        elif user_input == "Dequeue" :

            one.dequeue()
            print(f"The Queue Elements : {one}")


        elif user_input == "Size" :

            print(f"\nThe Size Of Queue Is : {one.size()} Element")


        elif user_input == "Is empty":
            
            print(f"\nIs The Queue Empty : {one.is_empty()}")
        

        else:
            print("\nPlease Enter A Valid Operation -_^")
        exit = input("\nDo You Want To Continue (Y/N): ").strip().capitalize()
        if exit == "N":
            break
        if exit != "Y":
            print("\nInvalid Choice -_^")       
            break


operations()


print("\n\t"+"==>" , "Thank You For Using My Application :)" , "<==\n")