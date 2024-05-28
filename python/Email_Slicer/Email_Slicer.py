print("\t\t" , "=" * 34)
print("\t\t" , "=" * 4 , "Email Slicer Application" , "=" * 4 )
print("\t\t" , "=" * 34)

print("\n\t==>^ Hint : You Have Only 3 Tries ^<==")
print("\t==>^   For Writing A Vaild Email  ^<==")

tries = 0
while True:

    try:
        user_email = input("\nPlease Enter Your Email : ")
        if '@' not in user_email:
            tries += 1
            if tries == 3:
                raise ValueError("\nSorry , All Tries You Have Is Done :)")
            else:
                print("\nSorry , Please Enter Valid Email -_^")
        
        else:
            username = user_email[:user_email.index('@')]
            domain = user_email[user_email.index('@') + 1 :]
            print(f"\n==> Your Username Is : \'{username}\' \n==> Your Domain Is : \'{domain}\'")
            break
    except ValueError as VE:
        print(VE)
        if tries == 3:
                break
        
print("\n====>" , "Thank You For Using My Application :)" ,"<=====\n")