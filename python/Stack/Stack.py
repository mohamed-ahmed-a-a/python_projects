print("\t\t" , "=" * 42)
print("\t\t" , "=" * 4 + ">", "Guess The Number Application" , "<" + "=" * 4 )
print("\t\t" , "=" * 42)

print("\n\tThe Operation That You Can Do On Queue Is ")
print("\t==>\'Push\' | \'Pop\' | \'Peek\' | \'Size\' | \'is empty\'\n")

# Last In First Out
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self , item):
        return self.items.append(item)
    
    def pop(self):
        if len(self.items) < 1:
            return None 
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if len(self.items) < 1:
            return None 
        return self.items[-1]

        

one = Stack()

def operations():

    while True:
        user_input = input("\nPlease Enter The Operation : ").strip().capitalize()

        if user_input == "Push" :

            the_input = input("Please Enter The Element : ").strip()

            one.push(the_input)

            print(f"\n\'{the_input}\' Is Inserted Successfully ")
            
            print(f"The Stack Elements : {one.items}")


        elif user_input == "Pop" :

            one.pop()
            print(f"The Stack Elements : {one.items}")


        elif user_input == "Size" :

            print(f"\nThe Size Of Stack Is : {one.size()} Element")


        elif user_input == "Is empty":
            
            print(f"\nIs The Stack Empty : {one.is_empty()}")


        elif user_input == "Peek":
            
            print(f"\nThe Deleted Item Is : {one.peek()}")
        

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